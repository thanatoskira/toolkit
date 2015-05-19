#!/usr/bin/env python
# coding=utf-8

author = "thanat0s"
DirBuster_version = "0.1"

import argparse
import sys
import random
import requests
import urlparse

class Banners:
    banner1 = """
    ____  _      ____             __           
   / __ \(_)____/ __ )__  _______/ /____  _____
  / / / / / ___/ __  / / / / ___/ __/ _ \/ ___/
 / /_/ / / /  / /_/ / /_/ (__  ) /_/  __/ /    
/_____/_/_/  /_____/\__,_/____/\__/\___/_/     
                                               
"""                                              

    banner2 = """
< Welcome to DirBuster >
 ----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
"""
    def printBanner(self):
        banners = [self.banner1,self.banner2]
        print random.choice(banners)

def Scanner(url):
    parser = urlparse.urlparse(url)
    if parser.netloc == '':
        sys.exit("\033[1;31;40m[-]The URL is incorrect!\033[0m")
    url = (parser.scheme == "http" or parser.scheme == "https") and parser.scheme + "://" + parser.netloc + '/' or "http://" + parser.netloc + '/'
#    url = parser.path == '/' and url or url + "/"
    print url




if __name__ == '__main__':
    Banners().printBanner()
    parser = argparse.ArgumentParser(description="DirBuster v{} - T00l for Web Directory Scan".format(DirBuster_version),version=DirBuster_version,usage='dirbuster.py -u [target url] [dirbuster options] ',fromfile_prefix_chars='@', epilog="Time to go~")
    mgroup = parser.add_argument_group("DirBuster", "Options for DirBuster")
    mgroup.add_argument("-u","--url=",metavar="URL",dest="URL",help="The Target URL(eg:http://www.baidu.com/)")
    mgroup.add_argument("-w","--write",dest="OutFile", type=argparse.FileType('w'),metavar="filename", default=sys.stdout, help="Specify file to log to (stdout by default).")
    mgroup.add_argument("-f","--file=",dest="InFile", type=argparse.FileType('r'),metavar="filename", default=sys.stdin, help="The Specify file of Directory file.")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    Scanner(args.URL)
