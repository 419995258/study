#!/usr/bin/evn python
# -*- coding: utf-8 -*-


import requests
import time
from bs4 import BeautifulSoup


class New(object):
    title = None  # 新闻标题
    href = None     #新闻链接
    queryTime = None  #查询时间
    source = 'baidu' #来源

class GetTiebaInfo(object):
    def __init__(self):
        print("开始查询新闻")
        self.getTXnews()

    def getTXnews(self):
        url = "http://news.baidu.com/"
        # 请求腾讯新闻的URL，获取其text文本
        wbdata = requests.get(url).text
        # 对获取到的文本进行解析
        soup = BeautifulSoup(wbdata, 'lxml')
        # 保存页面内容
        fileName = u'获取新闻页面内容文件' + time.strftime('%Y-%m-%d', time.localtime()) + '.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            fp.write(soup.encode('utf8'))
        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
        news_titles = soup.select("ul.focuslistnews > li > a")
        news_titles2 = soup.select("ul.hotwords > li > a")
        news_titles.extend(news_titles2)
        #
        # # 对返回的列表进行遍历
        news = []
        for n in news_titles:
            # 提取出标题和链接信息
            title = n.get_text()
            href = n.get("href")
            new = New()
            new.title = title
            new.href = href
            new.queryTime = time.strftime('%Y-%m-%d', time.localtime())
            news.append(new)

        # 保存新闻到文件
        self.saveNewsToText(news)
        # 保存新闻到数据库
        # self.saveNewsToSql(news)
        # print(news)


    def saveNewsToText(self,news):
        fileName = u'获取百度新闻页面内容' + time.strftime('%Y-%m-%d', time.localtime()) + '.txt'.encode('GBK')
        with open(fileName, 'w') as fp:
            for new in news:
                fp.write("标题：%s \n "% (new.title.encode('utf8')))
                fp.write("链接：%s \n "% (new.href.encode('utf8')))
                fp.write("查询时间：%s \n " % (new.queryTime.encode('utf8')))
                fp.write("新闻来源：%s \n " % (new.source.encode('utf8')))
                fp.write("\n\n\n\n\n ")




if __name__ == '__main__':
    # url = u'http://news.qq.com/a/20170504/012032.htm'
    # url = u'http://tieba.baidu.com/f?kw=snh48&ie=utf-8&pn=0'
    GTI = GetTiebaInfo()