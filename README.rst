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
* Muli-Threaded search processing that allows large data set

Sampe Usage
--------

Sample Usage is::
    
    Command line input:

    [1-Single Threaded] python jobseeker.py search -k python -l singapore -n 2
    [2-Multi Threaded]  python multithreaded_jobseeker.py search -k python -l singapore -n 2 
    Command line output
    
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

Another Sample Usage::
    
    Command line input:

    [1-Single Threaded] python jobseeker.py search -k 'python java' -l London -n 4
    [2-Multi Threaded]  python multithreaded_jobseeker.py search -k 'python java' -l London -n 4
    Command line output:


    ===============================================================================
    ID: 1    Source: Google                      Posted: 6 days ago
    -------------------------------------------------------------------------------
    Title: Software Engineer, University Graduate
    Company: Google                              
    Location: London
    Description: , information retrieval and TCP/IP.* Programming experience in one or more of the following: C/C++, Java , Python .Preferred qualifications* MSc or PhD.* Experience in...
    Link: http://www.recruit.net/directjob.html?query=python+java&location=london&jobtitle=Software+Engineer%2C+University+Graduate&region=uk&s=92&u=http%2Fmy.jobs%2Fe02c5439e77c4b37b6d6b6088f7d0b01105&jobref=AD57E29F3D357E19
    ===============================================================================


    ===============================================================================
    ID: 2    Source: BNP Paribas                      Posted: 2 days ago
    -------------------------------------------------------------------------------
    Title: Java Developer - Sierra Reference Data Team
    Company: BNP Paribas                              
    Location: London
    Description: , Javascript, JMock, Hibernate & FIT. We use Python for scripting.   Key Responsibilities The role is for a Java developer to join an established team. This a...
    Link: http://www.recruit.net/directjob.html?query=python+java&location=london&jobtitle=%C3%B6Java%C5%BC+Developer+-+Sierra+Reference+Data+Team&region=uk&s=1570&u=http%2Fwww.bnpparibas.com%2Fen%2Femploi-carrieres%2Foffres%2Fjava-developer-sierra-reference-data-team&jobref=2A0C69276E3560EB
    ===============================================================================


    ===============================================================================
    ID: 3    Source: Google                      Posted: 6 days ago
    -------------------------------------------------------------------------------
    Title: gTech Software Engineer
    Company: Google                              
    Location: London
    Description: infrastructure.Minimum qualifications* BA/BS degree or equivalent practical experience.* Programming experience in C/C++, Java , Javascript, Python or C#.Preferred...
    Link: http://www.recruit.net/directjob.html?query=python+java&location=london&jobtitle=gTech+Software+Engineer&region=uk&s=92&u=http%2Fmy.jobs%2Fd5fa0619e0e9421c90cc9cd1538833a7105&jobref=BCA9C5BC0212FD31
    ===============================================================================


    ===============================================================================
    ID: 4    Source: Google                      Posted: 6 days ago
    -------------------------------------------------------------------------------
    Title: Software Engineer, Privacy
    Company: Google                              
    Location: London
    Description: practical experience.* Experience designing and implementing distributed software systems, preferably in Java , C++, or Python .Preferred qualifications* MS or PhD in...
    Link: http://www.recruit.net/directjob.html?query=python+java&location=london&jobtitle=Software+Engineer%2C+Privacy&region=uk&s=92&u=http%2Fmy.jobs%2Fed55a72c114449218a67f240124f1af3105&jobref=C355562C843158DF
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

Continious Integration - Travis CI build
---------

Travis CI Build: https://travis-ci.org/mengfeng/jobseeker

