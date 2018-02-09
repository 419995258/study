#!/usr/bin/evn python
# -*- coding: utf-8 -*-


import urllib2
import os.path
from bs4 import BeautifulSoup
import time
import requests
import sys
import re
from Crypto.Cipher import AES

reload(sys)
sys.setdefaultencoding('utf-8')


# url = 'http://lu.shuiqingqing.net/media/photos/1.jpg'
# url = 'http://www.yehualu.pw/photo/1'
# imgName = 'F:\Mode\XX\python\1.img'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

home_url = "http://www.yemalu.es/videos?" + "page="
video_url = "http://www.yemalu.es/"
videos = []   # 所有视频的连接地址
videosSrc = []   # 所有视频的下载地址

class Video(object):
    href = None     #链接
    title = None     #名字


# 循环获取所有页面的数据1-29
def getAllVideos():
    for i in range(0,1):
        print home_url + bytes(i)
        # 获取页面的所有标题信息(对编码进行转换，否则乱码)
        home_data = requests.get(home_url + bytes(i))
        home_data.encoding = 'utf-8'
        home_data = home_data.text
        fileName = 'home_data'+ bytes(i) + time.strftime('%Y-%m-%d', time.localtime()) + '.txt'
        # with open(fileName, 'w') as fp:
            # 先写进txt看看
            # fp.write(home_data.encode('utf-8'))
        # 对当前页面进行数据提取
        # 对获取到的文本进行解析
        soup = BeautifulSoup(home_data, 'lxml')
        # 从解析文件中通过select选择器定位指定的元素，返回一个列表
        video_href = soup.select("div.well-sm > a")
        for n in video_href:
            videos.append(n.get("href"))

# 获取某一个视频中的下载地址
def getVideos():
    for x in videos:
        videoShowUrl = video_url + x
        videoShowGet = requests.get(videoShowUrl)
        videoShowGet.encoding = 'utf-8'
        videoShowGet = videoShowGet.text
        soup = BeautifulSoup(videoShowGet, 'lxml')
        # 下载地址
        videoSource = soup.find('div',attrs={'class': 'video-container'})
        videoSource = videoSource.find("source").get("src")
        # video名字
        videoTitle = soup.find('h4',attrs={'class': 'visible-xs big-title-truncate m-t-0'}).get_text()
        # 把视频的数据保存起来
        video = Video()
        video.href = videoSource
        video.title = videoTitle
        videosSrc.append(video)

# 开始进行下载操作
def downloadVideos():
    for video in videosSrc:
        print video.title + ":" + video.href
        url = video.href[0:-10] + '500kb/hls/'
        # url = "http://newvideoserver.top/uploads/20180206/ZxDzJrU7pL/500kb/hls/"
        home_url = "F://Mode//XX//python//video//"
        name = video.title
        m3u8Name = home_url + name + '.m3u8'
        m3u8Name = m3u8Name.decode('utf-8', 'ignore')
        keyUrl = url + "key.key"
        key = ""
        # 保存m3u8文件
        try:
            if os.path.exists(m3u8Name):
                pass
            else:
                print ("正在获取：" + name)
                getLog("正在获取：" + name)
                response = urllib2.Request(url + "index.m3u8", headers=headers)
                content = urllib2.urlopen(response, timeout=10).read()
                responseKey = urllib2.Request(keyUrl, headers=headers)
                key = urllib2.urlopen(responseKey, timeout=10).read()
                print key
                getLog(key)
                with open(m3u8Name, 'wb') as fp:
                    fp.write(content)
                time.sleep(2)

        except Exception, e:
            print (url + ":网络地址错误/暂时没有资源/超时")
            print e
            getLog(url + ":网络地址错误/暂时没有资源/超时")
            time.sleep(2)
        # 读取m3u8文件
        m3u8 = open(m3u8Name, 'rb')
        movies_url = []
        for line in m3u8.readlines():
            if '.ts' in line:
                movies_url.append(line[:-1])
            else:
                continue
        m3u8.close()
        # 下载所有的ts文件
        for i in movies_url:
            # print i
            try:
                if os.path.exists(home_url + i):
                    pass
                else:
                    print ("正在获取：" + i)
                    getLog("正在获取：" + i)
                    response = urllib2.Request(url + i, headers=headers)
                    content = urllib2.urlopen(response, timeout=10).read()
                    with open(home_url + i, 'wb') as fp:
                        fp.write(content)
                        # time.sleep(2)

            except Exception, e:
                print (url + ":网络地址错误/暂时没有资源/超时")
                print e
                time.sleep(2)

            # ts视频被AES加密了，所以需要解密，使用pyCrypto的解密
                # ts视频被AES加密了，所以需要解密，使用pyCrypto的解密
            raw = file(home_url + i, 'rb').read()
            iv = raw[0:16]
            data = raw[16:]
            if key != "":
                plain_data = AES.new(key, AES.MODE_CBC, iv).decrypt(data)
                with open(home_url + i, 'wb') as fp:
                    fp.write(plain_data)

        # 合并ts文件

        print home_url
        os.chdir(home_url)
        shell_str = '+'.join(movies_url)
        # name = name.decode('utf-8','ignore')
        # 把titile里的符号等都用正则表达式去除
        name = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), name)
        name = name.decode('utf-8').encode('gbk') + '.ts'
        shell_str = 'copy /b ' + shell_str + ' ' + name
        print shell_str
        os.system(shell_str)
        # 删除ts和m3u8文件
        os.system('del /Q *.ts')
        os.system('del /Q *.m3u8')




# 下载测试
def downTest():
    # url = "http://newvideoserver.top/uploads/20180206/ZxDzJrU7pL/index.m3u8"
    url = "http://newvideoserver.top/uploads/20180205/DMJq6Jz27c/500kb/hls/"
    home_url = "F://Mode//XX//python//video//"
    name = "tttttt"
    m3u8Name = home_url + name + '.m3u8'
    m3u8Name = m3u8Name.decode('utf-8','ignore')
    keyUrl = url + "key.key"
    key = ""
    # 保存m3u8文件
    try:
        if os.path.exists(m3u8Name):
            pass
        else:
            print ("正在获取：" + name)
            response = urllib2.Request(url+"index.m3u8", headers=headers)
            content = urllib2.urlopen(response, timeout=10).read()
            responseKey = urllib2.Request(keyUrl, headers=headers)
            key = urllib2.urlopen(responseKey, timeout=10).read()
            print key
            with open(m3u8Name, 'wb') as fp:
                fp.write(content)
            time.sleep(2)

    except Exception, e:
        print (url + ":网络地址错误/暂时没有资源/超时")
        print e
        time.sleep(2)
    # 读取m3u8文件
    m3u8 = open(m3u8Name, 'rb')
    movies_url = []
    for line in m3u8.readlines():
        if '.ts' in line:
            movies_url.append(line[:-1])
        else:
            continue
    m3u8.close()
    # 下载所有的ts文件
    for i in movies_url:
        # print i
        try:
            if os.path.exists(home_url + i):
                pass
            else:
                print ("正在获取：" + i)
                response = urllib2.Request(url + i, headers=headers)
                content = urllib2.urlopen(response, timeout=10).read()
                with open(home_url + i, 'wb') as fp:
                    fp.write(content)
                # time.sleep(2)

        except Exception, e:
            print (url + ":网络地址错误/暂时没有资源/超时")
            print e
            time.sleep(2)
        print home_url + i

        # ts视频被AES加密了，所以需要解密，使用pyCrypto的解密
        raw = file(home_url + i, 'rb').read()
        iv = raw[0:16]
        data = raw[16:]
        if key != "":
            plain_data = AES.new(key, AES.MODE_CBC, iv).decrypt(data)
            with open(home_url + i, 'wb') as fp:
                fp.write(plain_data)





        # 合并ts文件

    print home_url
    os.chdir(home_url)
    shell_str = '+'.join(movies_url)
    # name = name.decode('utf-8','ignore')
    name = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), name)
    name = name.decode('utf-8').encode('gbk') + '.ts'
    shell_str = 'copy /b ' + shell_str + ' ' + name
    print shell_str
    os.system(shell_str)
    # 删除ts和m3u8文件
    # os.system('del /Q *.ts')
    # os.system('del /Q *.m3u8')

def getLog(text):
    fileName = "log.txt"
    with open(fileName, 'a') as fp:
        fp.write(text.encode('utf8'))
        fp.write("\n\n\n\n\n ")



if __name__ == '__main__':
    getAllVideos()
    getVideos()
    downloadVideos()
    # downTest()


'''
if os.path.exists(imgName):
    pass
else:
    with open(imgName, 'wb') as fp:
        response = urllib2.Request(url, headers=headers)
        content = urllib2.urlopen(response).read()
        fp.write(content)
'''