#!/user/bin/env python
#coding=utf-8

import urllib2

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def linkBaidu():
    url = u'http://tieba.baidu.com/f?kw=snh48&ie=utf-8&pn=0'
    try:
        response = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(url,timeout=3)
        http = content.read()
        print http
    except urllib2.URLError:
        print (u"网络地址错误")
        exit()
    with open('./baidu.txt','w')as fp:
        fp.write(http)

    print ("获取url信息 response.geturl():%s" %content.geturl())
    print ("获取返回代码 response.getcode():%s" % content.getcode())
    print ("获取返回信息 response.info():%s" % content.info())
    print ("获取的信息以及保存到当前目录的baidu.txt文件下，请自行查看")

if __name__ == '__main__':
    linkBaidu()