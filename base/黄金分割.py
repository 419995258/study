#!/user/bin/env python
#coding=utf-8

class fuct(object):
    '''返回一个黄金分割数列'''
    def __init__(self):
        self.fList = [0,1]
        self.main()

    def main(self):
        listLen = raw_input("请输入黄金分割的数列长度")
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print("数列为%r"%self.fList)

    def checkLen(self,lenth):
        '''检查输入的长度是否符合要求'''
        lenList = map(str,range(3,51))
        if lenth in lenList:
            print("输入的长度符合要求，继续运行")
        else:
            print("只能输入3-50的数字！")
            exit()


if __name__ == '__main__':
    f = fuct()