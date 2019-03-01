# coding=utf-8
import xlrd
import sys

book = xlrd.open_workbook("2018NB.xlsx")
sheet = book.sheet_by_name("tj")

# sql = "create table XX_2017("
sql = "create table NB_TJ_2018(id VARCHAR2(255),"
sql = sql + ""
commentsql = ""
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):

print sheet.ncols

for i in range(0,sheet.ncols):
        col = str(sheet.cell(6, i).value)
        col = col[0:-2]
        col = "X_" + col
        sql = sql + col + " VARCHAR2(255),"

sql = sql + " primary key (id) )"
print sql