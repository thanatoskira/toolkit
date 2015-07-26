#!/usr/bin/env python
# coding=utf-8

import requests
import re

def IP_Scanner(IPList):
    Readfp = set(open(IPList, "r"))
    Savefp = open("OpenPortResult.txt", "a")

    for ip in Readfp:
        ip = ip.strip()
        url = "http://tool.chinaz.com/iframe.ashx?t=port&host=%s&encode=k0ie1|f9J/sphgp0|cJZMt7B2VkK74x8&port=+80,8080,3128,8081,9080,1080,21,23,443,69,22,25,110,7001,9090,3389,1521,1158,2100,1433" % ip
        pattern = re.compile(r':(\d{1,4}) 开放<br/>', re.S)
        print "Scanning Port On IP " + ip + " With Result:"
        content = requests.get(url).text.encode('utf-8')
        result = re.findall(pattern, content)
        Savefp.writelines("IP: %s\n\t" % ip)
        if result:
            print "\t[+]Open Port:",
            Savefp.writelines("Open:")
            for port in result:
                print port + " ",
                Savefp.writelines("%s " % port)
            print
            Savefp.writelines("\n\n")

        else:
            print "\t[-]No Port Open:"
            Savefp.writelines("[-]No Port Open!\n\n")
    Savefp.close()

if __name__ == "__main__":
    iplist = raw_input("IPList File:")
    IP_Scanner(iplist)

