#!/user/bin/env ptthon
#coding=utf-8

import random

class selectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input("请输入要测试的次数")
            try:
                num = int(numStr)
            except ValueError:
                print("请输入一个整数")
                continue
            else:
                break
        ball = [0,0,0,0,0,0,0,0,0,0]
        ballAdd = [0,0,0,0,0,0,0,0,0,0]
        for i in xrange(num):
            n = random.randint(1,10)
            ball[n-1] += 1
        for i in range(1,11):
            print("获取第%d号球的概率是:%r"%(i,ball[i-1]*100.0/num)),
            #
            print "%"

        print ball
        addAll = 0
        for i in range(0,ball.__len__()):
            ballAdd[i] = ball[i] * 100 / num
            addAll += ballAdd[i]
        print "总概率是：",addAll,"%"
if __name__ == '__main__':
    selectBall()