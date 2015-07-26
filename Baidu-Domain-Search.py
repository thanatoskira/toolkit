#!/usr/bin/env python
# coding=utf-8

import requests
import re
from urlparse import urlparse
from bs4 import BeautifulSoup
from time import ctime

def Baidu_DomainSearch(SearchDomain, PageCount):
    print "Start Searching..."
    Domains = set()
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/39.0'}
    url = "http://www.baidu.com/s?ie=utf-8&tn=baidu&wd=site:%s" % SearchDomain
    pattern = re.compile("([a-zA-Z0-9.]*%s)" % SearchDomain, re.S)
    for times in range(PageCount):
        content = requests.get(url)
        soup = BeautifulSoup(content.text)
        for Tage in soup.body.find_all("h3", "t"):
            SearchURL = Tage.a['href']
            try:
                response = requests.get(SearchURL, headers=headers, timeout=2)
                domain = urlparse(response.url).netloc
                print "[+]Get " + response.url
                Domains.add(domain)

            except (EOFError, KeyboardInterrupt), e:
                choice = raw_input("Are you Sure to Stop the Scan?(yes/y, default:no)")
                if choice == "yes" or choice == "y":
                    OutPutWithSave(Domains, SearchDomain)
                    print "\nByeBye～"
                    exit(0)

            except Exception, e:
                domain = re.search(pattern, str(e))
                try:
                    domain = domain.group()
                    print "[-]Wrong " + domain
                    Domains.add(domain)
                except Exception, ex:
                    print "[-]Wrong " + e
                
        url = soup.body.find_all("a", "n")
        url = "http://www.baidu.com" + url[-1]['href']

    OutPutWithSave(Domains, SearchDomain)


def OutPutWithSave(Domains, SearchDomain):
    print '\nDomain about ' + SearchDomain + ' :\n'
    fp = open("Domain_result.txt", "a")
    fp.writelines('----------' + str(ctime()) + '----------\n')
    for domain in Domains:
        print domain
        fp.writelines(domain + "\n")
    print 'Saving in Domain_result.txt\n'
    fp.close()
        

if __name__ == '__main__':
    try:
        domain = raw_input(r'Search Domain:')
        pagecount = int(raw_input(r'Page Count:'))
        Baidu_DomainSearch(domain, pagecount)
    except (EOFError, KeyboardInterrupt), e:
        print "\nByeBye～"
        exit(0)
