#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import requests
import logging
import random
import re
from pyquery import PyQuery as pq
import threading
BASE_URL='http://www.recruit.net'
URL='http://www.recruit.net/search.html'
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',)

CONSOLE_OUTPUT_TEMPLATE='''
===============================================================================
ID: %d    Source: %s                      Posted: %s days ago
-------------------------------------------------------------------------------
Title: %s
Company: %s                              
Location: %s
Description: %80s
Link: %s
===============================================================================
'''

thread_lock = threading.Lock()

class JobItem:
    def __init__(self, title, href, company, location, description, source, post_time):
        self.title = title
        self.href = href
        self.company = company
        self.location = location
        self.description = description
        self.source = source
        self.post_time = post_time


class JobExtractionThread(threading.Thread):
    def __init__(self, threadID, name, url, params, job_items):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url
        self.params = params
        self.job_items = job_items        
    
    def extract_job_items(self, url, params):
        extracted_job_items=[]
        res = perform_http_request(url, params)
        if res is None:
            return []   
        
        d = pq(res.text)
        for index, job_item_pq_obj in enumerate(d('div').filter('.job')):
            
            d_job_item = pq(job_item_pq_obj)

            item_link = d_job_item.find('h2').find('a')
            item_company = d_job_item.find('span').filter('.company')
            item_location = d_job_item.find('span').filter('.location').find('span')
            item_description = d_job_item.find('div').filter('.description')
            item_source = d_job_item.find('div').filter('.source')
            item_post_time = d_job_item.find('div').filter('.time')

            title = item_link.attr.title
            href = item_link.attr.href
            company = item_company.text()
            location = item_location.text()
            description = item_description.text()
            source = item_source.text()
            
            post_time_matches=re.compile('\d+').search(item_post_time.text())
            post_time = post_time_matches.group() if post_time_matches else 'Unknown'

            if title is not None: 
                job_item = JobItem(title, href, company, location, description, source, post_time)
                extracted_job_items.append(job_item) 
        
        return extracted_job_items


    def run(self):
        logging.info("starting " + self.name)
        #thread_lock.acquire()
        retrieved_items = self.extract_job_items(self.url, self.params) 
        #thread_lock.release()
        #print self.name, 'Number of jobs',len(retrieved_items) 
        self.job_items += retrieved_items



def extract_all_job_items(url, params):

        job_items=[]
        res = perform_http_request(url, params)
        if res is None:
            return []   
        
        total_pages = int(re.search(r'totalPages=(\d+)', res.text).group(1))
        logging.info('total_pages:' + str(total_pages))

        threads_pool = []
        for i in range(1, total_pages + 1):
           new_thread_params = params.copy()
           new_thread_params['pageNo'] = i
           #print 'params to start with', params
           new_thread = JobExtractionThread(i, "Thread-" + str(i), url, new_thread_params, job_items)      
           new_thread.start()
           threads_pool.append(new_thread)
        
        #wait for all threads to complete
        for t in threads_pool:
            #t.start()
            t.join()

        return job_items


def perform_http_request(url, params=None):
    try:
        user_agent = random.choice(USER_AGENTS)
        logging.info('making http request to { url: %s, user_agent: %s , params: %s}' % (url, user_agent, params))
        if params:
            res=requests.get(url, headers={'User-Agent': user_agent}, params=params)
        else:
            res=requests.get(url, headers={'User-Agent': user_agent})
        return res

    except Exception as e:
        logging.error('failed to perform http request to %s due to: %s' % (URL, str(e)))
        return None

def get_jobsearch_result(url, params, max_no):
        
        job_items = extract_all_job_items(url, params)
        job_items.sort( key=lambda job_item: int(job_item.post_time) if job_item.post_time.isdigit() else 100 )
        for index, job_item in enumerate(job_items[:max_no]):
            print (CONSOLE_OUTPUT_TEMPLATE % (index+1, job_item.source, job_item.post_time, 
                                                    job_item.title, job_item.company, job_item.location, 
                                                    job_item.description, job_item.href))
            #print index, job_item.title


def get_parser():
    parser = argparse.ArgumentParser(description='Search Jobs for Job Seekers')

    parser.add_argument('-l', '--location', type=str,  help='location of the job search')
    parser.add_argument('-k', '--keyword', type=str, help='keyword of the job search')
    parser.add_argument('-U', '--use_agency', help='indicator for where headhunder should be used', 
                        action='store_true', default=False)
    parser.add_argument('-c', '--company', help='company name to limit the job search with')
    parser.add_argument('-n', '--max_no', type=int, default=20, help='max number of jobs to display')
    parser.add_argument('search', help='perform search for job seeker')

    return parser

def perform_job_search(keyword, location, use_agency, company, max_no):
    job_source = '' if use_agency else  'company'
        
    params={'query': keyword, 'location': location, 'f_source': job_source,
            'f_company': company}   
    get_jobsearch_result(URL, params, max_no)

def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()

    if args.search and args.keyword and args.location:
        print 'performing searching for job seeks for keyword "%s" at location "%s...."' % (args.keyword, args.location)
        
        perform_job_search(args.keyword, args.location, args.use_agency, args.company, args.max_no)

    else:
        print 'incorrect usage:'
        parser.print_help()


def app_config():
    #config the logger
    logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app_config()
    command_line_runner()
