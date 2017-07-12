#!/user/bin/env python
#-*- coding:utf-8 -*-

class printTable(object):
    """打印99乘法表"""
    def __init__(self):
        x = 10
        print x, "开始打印乘法表"
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('%rX%r=%r '%(j,i,j*i)),
                # print j, "*",i,"= ",j*i,
            print('\n')
if __name__ == '__main__':
    pt = printTable()
