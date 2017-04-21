#!/user/bin/env python
#coding=utf-8

import urllib2
import re
try:
    response = urllib2.urlopen("http://www.xczxcs.cn/views/001_index.html#/home")
    http = response.read()
    movieList = re.findall('ui-sref.*',http)
except urllib2.URLError:
    exit()
with open('./movie','w') as fp:
    for movie in movieList:
        movie.decode('utf-8')
        fp.write(movie + '\n')