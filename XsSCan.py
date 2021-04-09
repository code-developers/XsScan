#!/usr/bin/env/python

#imports
import mechanize
import sys
import httplib
import argparse
import logging
from urlparse import urlparse

br = machanize.Browser() # initiating the browser
br.addheaders = [
    ('User-agent',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11')
]
br.set_handle_robots(False)
br.set_handle_refresh(False)

payloads = ['<svg "ons>', '" onfocus="alert(1);', 'javascript:alert(1)']
blacklist = ['.png', '.jpg', '.jpeg', '.mp3', '.mp4', '.avi', '.gif', '.svg',
             '.pdf']
xssLinks = []

class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def log(lvl, col, msg):
        logger.log(lvl, col + msg + color.END)


print color.BOLD + color.RED + """
GitHub: https://github.com/code-developers/XsSCan
""" + color.END
print color.BOLD + color.YELLOW + """
Usage: XsSCan.py -u website.com (Not www.website.com OR http://www.website.com)
Comprehensive Scan: python XsSCan.py -u website.com -e
Verbose logging: python XsSCan.py -u website.com -v
Cookies: python XsSCan.py -u website.complex -c name=val name=val
""" + color.END
print color.BOLD + color.BLUE + """
Description: XsSCan is a python tool for finding Cross Site Scripting
vulnerabilities in websites. This tool is the first of its kind.
Instead of just checking one page as most of the tools do, this tool
traverses the website and find all the links and subdomains first.
After that, it starts scanning each and every input on each and every
 page that it found while its traversal. It uses small yet effective
payloads to search for XSS vulnerabilities. XSS in many high
profile websites and educational institutes has been found
by using this very tool.
""" + color.END