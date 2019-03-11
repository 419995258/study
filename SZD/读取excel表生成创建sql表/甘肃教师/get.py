# coding=utf-8
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

book = xlrd.open_workbook("000.xls")
sheet = book.sheet_by_name("b")

sql = ""

# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(0, 94):
        col = sheet.cell(r,0).value
        sql = sql + "\"" + col + "\","
        # print col
        # print comment

print sql