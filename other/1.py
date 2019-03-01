#!/usr/bin/evn python
# -*- coding: utf-8 -*-


import urllib2
import os.path
import time
from bs4 import BeautifulSoup

# url = 'http://lu.shuiqingqing.net/media/photos/1.jpg'
# url = 'http://www.yehualu.pw/photo/1'
# imgName = 'F:\Mode\XX\python\1.img'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

turl = 'http://lu.shuiqingqing.net/media/photos/'
url = 'http://gbxm.sneducloud.com/sxgb/skins/gbCssV2/images/logo.png'

imgName = 'E://Mode//XX//python//img//a.jpg'


response = urllib2.Request(url, headers=headers)
content = urllib2.urlopen(response,timeout=5).read()
with open(imgName, 'wb') as fp:
    fp.write(content)
time.sleep(2)
print content.size




'''
if os.path.exists(imgName):
    pass
else:
    with open(imgName, 'wb') as fp:
        response = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(response).read()
        fp.write(content)
'''