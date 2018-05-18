# coding=utf-8
import xlrd
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

book = xlrd.open_workbook("data.xlsx")
sheet = book.sheet_by_name("a")

str = ""
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(87, 175):
        col = sheet.cell(r,0).value
        str = str + "\"" + col + "\","
        # print col
        # print comment

print(str)