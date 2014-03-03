===============================
jobseeker
===============================

.. image:: https://badge.fury.io/py/jobseeker.png
    :target: http://badge.fury.io/py/jobseeker
    
.. image:: https://travis-ci.org/mengfeng/jobseeker.png?branch=master
        :target: https://travis-ci.org/mengfeng/jobseeker

.. image:: https://pypip.in/d/jobseeker/badge.png
        :target: https://crate.io/packages/jobseeker?version=latest


Python App for Job Seekers

* Free software: BSD license
* Documentation: http://jobseeker.rtfd.org.

About Jobseeker.py
--------
jobseeker.py is a project done while I was searching for jobs. I am still using it..(you know what I mean)

jobseeker.py only ask for the minimum set of information to run the job search, such as job keywords, location, company, usage of job agencies...


Features
--------
* One stop shop for all jobs listed in various companies
* Underlying, recruit.net is used as the major source


Sampe Usage
--------

Sample Usage is::
    
    python jobseeker.py search -k python -l singapore -n 2
    ===============================================================================
    ID: 1    Source: JP Morgan Chase                      Posted: 22 days ago
    -------------------------------------------------------------------------------
    Title: CIB Technology - Application Developer (Python for Fixed Income Products) - Associate - Singapore
    Company: JP Morgan Chase                              
    Location: Singapore
    Description: delivery. The individual should have strong knowledge of Python and knowledge of developing in Athena is a plus.   The successful candidate must demonstrate...
    Link: http://www.recruit.net/directjob.html?query=python&location=singapore&jobtitle=CIB+Technology+-+Application+Developer+%28%C3%B6Python%C5%BC+for+Fixed+Income+Products%29+-+Associate+-+%C3%B6Singapore%C5%BC&region=all&s=3201&u=https%2Fjpmchase.taleo.net%2Fcareersection%2Fjobdetail.ftl%3Fjob%3D1374350%26lang%3Den&jobref=3510CFF0B105BCBE
    ===============================================================================


    ===============================================================================
    ID: 2    Source: Seagate                      Posted: 3 days ago
    -------------------------------------------------------------------------------
    Title: Engineer, Firmware Development Engineering
    Company: Seagate                              
    Location: Singapore
    Description: Object Orientated language (C or C++) or Python scripts development. 4) Problem solving and debug skills. 5) An independent thinker and a team player...
    Link: http://www.recruit.net/directjob.html?query=python&location=singapore&jobtitle=Engineer%2C+Firmware+Development+Engineering&region=all&s=2943&u=https%2Fseagate.taleo.net%2Fcareersection%2Fjobdetail.ftl%3Fjob%3D141017%26lang%3Den&jobref=DD9C2723EA85D6B9
    ===============================================================================

The above output is as of 2-Mar-2014.


Usage Reference
--------
usage: jobseeker.py [-h] [-l LOCATION] [-k KEYWORD] [-U] [-c COMPANY]
                    [-n MAX_NO]
                    search

Search Jobs for Job Seekers

positional arguments:
    search                perform search for job seeker

optional arguments:
    -h, --help            show this help message and exit
    -l LOCATION, --location LOCATION     location of the job search
    -k KEYWORD, --keyword KEYWORD        keyword of the job search
    -U, --use_agency                     indicator for where headhunder should be used
    -c COMPANY, --company COMPANY        company name to limit the job search with
    -n MAX_NO, --max_no MAX_NO           max number of jobs to display
