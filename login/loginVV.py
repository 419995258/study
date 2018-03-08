#coding=utf-8
__author__ = 'Eagle'
import os
import time
import win32gui
import win32api
import win32con
import SendKeys
import subprocess
import xlrd
from ctypes import *

def Login(username,pwd):
    try:
        # 运行QQ   路径不能是中文，由于os.system会阻塞，这里用subprocess
        subprocess.Popen("D:\my\IM\my.exe")
        # os.system('"D:\my\IM\my.exe"')
        time.sleep(3)
        a = win32gui.FindWindow(None, "VV")  # 获取窗口的句柄，参数1: 类名，参数2： 标题QQ
        loginid = win32gui.GetWindowPlacement(a)
        windll.user32.SetCursorPos(loginid[4][0] + 200, loginid[4][1] + 150)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 按下鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 放开鼠标
        time.sleep(0.2)
        ###输入账号
        SendKeys.SendKeys(username)
        time.sleep(0.2)
        ##tab切换
        win32api.keybd_event(9, 0, 0, 0)
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        SendKeys.SendKeys(pwd)
        # 点击回车键登录
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    except Exception, e:
        print ""


book = xlrd.open_workbook("D:\my\IM\\mi.xlsx")
sheet = book.sheet_by_name("Sheet1")
for r in range(0, sheet.nrows):
        username = str(sheet.cell(r,0).value)
        password = str(sheet.cell(r,1).value)
        Login(username,password)