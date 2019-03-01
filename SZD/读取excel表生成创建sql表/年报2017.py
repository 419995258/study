# coding=utf-8
import xlrd
import sys

book = xlrd.open_workbook("000.xls")
sheet = book.sheet_by_name("a")

# sql = "create table XX_2017("
sql = "create table NB_XX_2017("
sql = sql + ""
commentsql = ""
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):

for i in range(3,68):
    col = str(sheet.cell(5, i).value)
    col = "X_" + col
    sql = sql + col + " VARCHAR2(255),"

# for i in range(0,62):
#         col = str(sheet.cell(6, i).value)
#         col = col[0:-2]
#         col = "X_" + col
#         sql = sql + col + " VARCHAR2(255),"

sql = sql + " primary key (X_1) )"
print sql