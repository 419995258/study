#!/user/bin/env python
#-*- coding:utf-8 -*-
#
#
# # # def addAll():
# #     num = 0
# #     if(num != 100):
# #         num += 1
# #         print num
# #     else:
# #         print ("ok")
# #         print num
#
# # if num != 100:
# #         num += 1
# #         print num
# # else:
# #         print ("ok")
# #         print num
# # for i in range(1,5):
# #     print i
# #     if num != 5:
# #         print num
# #         num = num + 1
# #         print num
# #     else:
# #         print("ok")
# #         print num
# # for i in range(0,6):
# #     num = num + 1
# #     if i != 4:
# #         print("ok")
# #     elif i>1 :
# #         print("no")
#
# class tryInput(object):
#     def __init__(self):
#         self.len = 10
#         self.numList = self.createList()
#         # self.getNum()
#
#     def createList(self):
#         print("创建一个长度为%d的数字列表" %self.len)
#         numList = []
#         while len(numList) < 10:
#             n = raw_input("请输入一个整数")
#             try:
#                 num = int(n)
#             except ValueError:
#                 print("输入错误，输入要求是一个整数")
#             continue
#             numList.append(num)
#             print("现在的列表为：")
#             print(numList)
#
#         return numList
#
#     # def getNum(self):
#     #     print("当前列表为")
#     #     print(self.numList)
#     #     inStr = None
#     #     while inStr != 'EXIT':
#     #         print("输入exit退出程序")
#     #
# ti = tryInput()

