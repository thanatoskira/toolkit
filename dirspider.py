#!/usr/bin/env python
# coding=utf-8

author = "thanat0s"
DirBuster_version = 0.1

import argparse
import sys


banner = """
    ____  _      ____             __           
   / __ \(_)____/ __ )__  _______/ /____  _____
  / / / / / ___/ __  / / / / ___/ __/ _ \/ ___/
 / /_/ / / /  / /_/ / /_/ (__  ) /_/  __/ /    
/_____/_/_/  /_____/\__,_/____/\__/\___/_/     
                                               
"""                                              

if __name__ == '__main__':
    print banner
    if len(sys.argv) == 1:
        sys.exit("usage:\n\tpython %s -h" % sys.argv[0])
    parser = argparse.ArgumentParser(description="DirBuster v{} - Framework for Web Directory Scan".format(DirBuster_version), version=DirBuster_version, usage='',fromfile_prefix_chars='@', epilog="Time to go~")
    mgroup = parser.add_argument_group("DirBuster", "Options for DirBuster")
    mgroup.add_argument("-u","--url =",metavar="URL",dest="URL",help="The Target URL(eg:http://www.baidu.com/)")
    mgroup.add_argument("-w","--write",dest="OutFile", type=argparse.FileType('w'),metavar="filename", default=sys.stdout, help="Specify file to log to (stdout by default).")
    mgroup.add_argument("-f","--file =",dest="InFile", type=argparse.FileType('r'),metavar="filename", default=sys.stdin, help="The path of directory file.")
    args = parser.parse_args() 
