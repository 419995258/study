#!/user/bin/env python
#coding=utf-8

import urllib2

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib2.urlopen(url,timeout=3)
        http = response.read()
        print http
    except urllib2.URLError:
        print (u"网络地址错误")
        exit()
    with open('./baidu.txt','w')as fp:
        fp.write(http)

    print ("获取url信息 response.geturl():%s" %response.geturl())
    print ("获取返回代码 response.getcode():%s" % response.getcode())
    print ("获取返回信息 response.info():%s" % response.info())
    print ("获取的信息以及保存到当前目录的baidu.txt文件下，请自行查看")

if __name__ == '__main__':
    linkBaidu()