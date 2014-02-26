#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

def main():
    parser = argparse.ArgumentParser(description='Search Jobs for Job Seekers')
    
    parser.add_argument('-l','--location', type=str,  help='location of the job search')
    parser.add_argument('-k','--keyword', type=str, help='keyword of the job search')

    args = parser.parse_args()
    parser.print_help()
    
if __name__=='__main__':
    main()
    
