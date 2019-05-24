# -*- coding: utf-8 -*-
import urllib2
import json
import time

try:
    '''response = urllib2.urlopen('https://api.douban.com/v2/book/1220562')
    html = response.read()
    print html
    hjson = json.loads(html)
    print hjson
    print hjson['id']
    print hjson['rating']['max']
    print hjson['tags'][0]['name']

    fileName = u'获取豆瓣内容' + time.strftime('%Y-%m-%d', time.localtime()) + '.txt'.encode('GBK')
    with open(fileName, 'w') as fp:
        fp.write(hjson['id'].encode('utf-8') + "\n")
        fp.write(str(hjson['rating']['max']).encode('utf-8') + "\n")
        fp.write(hjson['tags'][0]['name'].encode('utf-8') + "\n")'''

    response = urllib2.urlopen('http://api.douban.com/v2/movie/top250')
    html = response.read()
    html = html.encode('utf-8').decode('unicode_escape')
    print html
    hjson = json.loads(html)
    print hjson['count']

except urllib2.URLError:
    exit()



