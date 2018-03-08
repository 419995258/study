#coding=utf-8
__author__ = 'Eagle'
import os
import time
import win32gui
import win32api
import win32con
import SendKeys
from ctypes import *

def Login(qq,pwd):
    a = win32gui.FindWindow(None, "TIM")
    #运行QQ   路径需要是中文
    os.system('"D:\QQ\Bin\QQ.exe"')
    time.sleep(5)
    a= win32gui.FindWindow(None,"QQ") # 获取窗口的句柄，参数1: 类名，参数2： 标题QQ
    loginid= win32gui.GetWindowPlacement(a)
    windll.user32.SetCursorPos(loginid[4][0]+300, loginid[4][1]+273 )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) #按下鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) #放开鼠标
    time.sleep(0.2)
    ###输入账号
    SendKeys.SendKeys(qq)
    time.sleep(0.2)
    ##tab切换
    win32api.keybd_event(9,0,0,0)
    win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)
    SendKeys.SendKeys(pwd)
    #点击回车键登录
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
#读取账号密码文件例如： 1234567----she123456 #账号密码四个- 分隔
fn = "D:\\mi.txt" #此文件可以自定义，但是路径要一定对
#打开账号密码文件
F = open(fn,"r").readlines()
#分隔账号密码，传两个参数，账号密码
for i in F:
    tx = i.split("----")
    Login(tx[0],tx[1])