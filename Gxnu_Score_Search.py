#!/usr/bin/env python
# coding=utf-8

#author:phantomer
#github:https://github.com/rootphantomer
#weibo:http://weibo.com/527819757

import urllib2
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def post(user,passwd):
    fp = open("Score.txt", "w")
    login_url="http://www.dean.gxnu.edu.cn/jwxt/index.php/api/user/login"

    data={}
    data['phone']="+8613512345678"
    data['username']=user
    data['password']=passwd
    post_data=urllib.urlencode(data)
    req=urllib2.urlopen(login_url,post_data)
    content=req.read()
    sid=content[56:82]
    data2={}
    data2['session_id']=sid
    url2="http://www.dean.gxnu.edu.cn/jwxt/index.php/api/chengji/getyxcj"
    sessionid="PHPSESSID="+sid
    post_data2=urllib.urlencode(data2)
    req2=urllib2.Request(url2,post_data2)
    req2.add_header('Cookie',sessionid)
    resp=urllib2.urlopen(req2)
    content2=json.loads(resp.read().encode('utf-8'))
    print "课程名称\t\t成绩\t年度/学期\t性质\t学分\t绩点"
    fp.writelines("课程名称\t\t成绩\t年度/学期\t性质\t学分\t绩点\n")
    for subject  in content2['msg']:
        print subject['kcmc'] + "\t\t" + subject['cj'] + "\t" + subject['ndxq'][:-1] + "/" + subject['ndxq'][-1] + "\t\t" + subject['bk'] + "\t" + subject['cx'] + "\t" + subject['jd']
        fp.write(subject['kcmc'] + "\t\t" + subject['cj'] + "\t" + subject['ndxq'][:-1] + "/" + subject['ndxq'][-1] + "\t\t" + subject['bk'] + "\t" + subject['cx'] + "\t" + subject['jd'] + "\n")
    fp.close()


def main():
    user=raw_input("Enter your Number:")
    passwd=raw_input("Enter your Passwd:")
    grade=post(user,passwd)

if __name__=='__main__':
    main()
