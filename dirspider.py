#!/usr/bin/env python
# coding=utf-8

author = "thanat0s"
DirBuster_version = "0.1"

import argparse
import sys
import random
import requests
import urlparse
from time import ctime

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

def Scanner(URL, InFile=open('Dictionary.lst','r').readlines(), OutFile=open('Scan.output', 'a')):
    parser = urlparse.urlparse(URL)
    if parser.netloc == '':
        sys.exit("\033[1;31m[-]The URL is incorrect!(eg:http://www.baidu.com)\033[0m")
    URL = (parser.scheme == "http" or parser.scheme == "https") and parser.scheme + "://" + parser.netloc + '/' or "http://" + parser.netloc + '/'
    exist = '' #存放返回值200的URL
    wrong = '' #存放服务器内部错误的URL
    redirect = '' #重定向的URL
    print "Result:"
    for urlpath in InFile:
        while urlpath.startswith('/'):
            urlpath = urlpath[1:]
        try:
            url = URL + urlpath.strip()
            status = requests.get(url).status_code
            if status not in range(400, 418):
                print  "\033[1;33mFound %s\tStatus: %s\033[0m" % (url, str(status))
                if status in range(200, 207):
                    exist += url + '\t' + str(status) +  '\n'
                if status == 500:
                    wrong += url + '\t' + str(status) + '\n'
                if status in range(300, 308):
                    redirect += url + '\t' +  str(status) + '\n'
        except (IOError, EOFError, KeyboardInterrupt), e:
            choice = raw_input('Are you Sure to Stop the Scan?(yes/y,default:no)')
            if choice == 'yes' or choice == 'y':
                break 
    OutFile.write('Target: ' + parser.netloc + "\t\tTime: " + ctime() + '\nExist:\n' + exist + '\nWrong:\n' + wrong + '\nRedirect\n' + redirect + '\n----------------------------------------------------------------\n\n')
    OutFile.close()
    print 'GoodBye～'







if __name__ == '__main__':
    Banners().printBanner()
    parser = argparse.ArgumentParser(description="DirBuster v{} - T00l for Web Directory Scan".format(DirBuster_version),version=DirBuster_version,usage='dirbuster.py -u [target url] [dirbuster options] ',fromfile_prefix_chars='@', epilog="Time to go~")
    mgroup = parser.add_argument_group("DirBuster", "Options for DirBuster")
    mgroup.add_argument("-u","--url=",metavar="URL",dest="URL",help="The Target URL(eg:http://www.baidu.com/)")
    mgroup.add_argument("-w","--write",dest="OutFile", type=argparse.FileType('w'),metavar="filename", default=sys.stdout, help="Specify file to log to (stdout by default:Scan.output)")
    mgroup.add_argument("-f","--file=",dest="InFile", type=argparse.FileType('r'),metavar="filename", default=sys.stdin, help="The Specify file of Directory file.(default:Dictionary.lst)")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    Scanner(args.URL)
