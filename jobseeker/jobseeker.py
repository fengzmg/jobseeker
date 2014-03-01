#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import requests
import logging
import random

#class


URL='http://www.recruit.net/search.html'
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',)
class JobItem:
    def __init__(self):
        self.title=''
        self.href=''
        self.company=''
        self.location=''
        self.description=''
        self.source=''
        self.post_time=''


def extract_job_items(html_text):
    pass


def get_jobsearch_result(url, params):
    try:
        user_agent = random.choice(USER_AGENTS)
        logging.info('making http request to { url: %s, user_agent: %s }' % (url, user_agent))
        res=requests.get(URL, headers={'User-Agent': user_agent}, params=params)
        logging.debug(res.text)
        job_items = extract_job_items(res.text)
    except Exception as e:
        logging.error('failed to perform http request to %s due to: %s' % (URL, str(e)))


def get_parser():
    parser = argparse.ArgumentParser(description='Search Jobs for Job Seekers')

    parser.add_argument('-l', '--location', type=str,  help='location of the job search')
    parser.add_argument('-k', '--keyword', type=str, help='keyword of the job search')

    parser.add_argument('search', help='perform search for job seeker')

    return parser

def perform_job_search(keyword, location):
    params={'query': keyword, 'location': location}   
    get_jobsearch_result(URL, params)

def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()

    if args.search and args.keyword and args.location:
        print 'performing searching for job seeks for keyword "%s" at location "%s...."' % (args.keyword, args.location)
        perform_job_search(args.keyword, args.location)

    else:
        print 'incorrect usage:'
        parser.print_help()


def app_config():
    #config the logger
    logging.basicConfig(filename='../logs/jobseeker.log',level=logging.DEBUG)

if __name__ == '__main__':
    app_config()
    command_line_runner()
