#!/usr/bin/env python
# coding=utf-8

import requests
import re
from urlparse import urlparse
from bs4 import BeautifulSoup
from time import ctime

def Baidu_DomainSearch(SearchDomain, PageCount):
    print "Start Searching..."
    Domains = set() #存放域名列表
    AccessURL = [] #存放各域名下可访问链接
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/39.0'}
    url = "http://www.baidu.com/s?ie=utf-8&tn=baidu&wd=site:%s" % SearchDomain
    pattern = re.compile("([a-zA-Z0-9.]*%s)" % SearchDomain, re.S)
    for times in range(PageCount): #搜索百度的页数
        content = requests.get(url) #获取百度搜索结果site:domain
        soup = BeautifulSoup(content.text) #利用BeautifulSoup对结果进行格式化
        for Tage in soup.body.find_all("h3", "t"):
            SearchURL = Tage.a['href'] #获取结果中的每个链接
            try:
                response = requests.get(SearchURL, headers=headers, timeout=2) #对每个链接进行访问，设置超时时间为2s
                domain = urlparse(response.url).netloc #获取访问目标域名
                print SearchURL
                if domain not in Domains: #判断域名是否存在于Domains集合中
                    Domains.add(domain)
                    try:
                        temp = requests.get("http://" + response.url, headers=headers, timeout=2) #判断http://domain/是否可以访问
                        if temp.reason != "OK": #如果不可以通过域名直接访问则将访问链接地址添加到AccessURL中
                            print "[1]Get " + response.url
                            AccessURL.append(response.url)
                        else: #可以则直接将域名访问地址添加到AccessURL中
                            AccessURL.append("http://" + domain)
                            print "[2]Get http://" + domain
                    except: #请求超时等错误发生也将访问链接地址添加到AccessURL中
                        AccessURL.append(response.url)
                        print "[3]Get " + response.url
                else: #存在于Domains集合中，则跳过之后步骤，直接进入下一次循环
                    continue

                print "[+]Get " + response.url

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
                    print "[-]Wrong " + str(e)
                
        url = soup.body.find_all("a", "n")
        url = "http://www.baidu.com" + url[-1]['href']

    OutPutWithSave(Domains, SearchDomain)


def OutPutWithSave(Domains, SearchDomain):
    print '\nDomain about ' + SearchDomain + ' :\n'
    #fp = open("Domain_result.txt", "a")
    #fp.writelines('----------' + str(ctime()) + '----------\n')
    for domain in Domains:
        print domain
        fp.writelines(domain + "\n")
    print 'Saving in Domain_result.txt\n'
    #fp.close()
        

if __name__ == '__main__':
    try:
        domain = raw_input(r'Search Domain:')
        pagecount = int(raw_input(r'Page Count:'))
        Baidu_DomainSearch(domain, pagecount)
    except (EOFError, KeyboardInterrupt), e:
        print "\nByeBye～"
        exit(0)
