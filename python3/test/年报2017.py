# coding=utf-8
import xlrd
import sys

book = xlrd.open_workbook("000.xlsx")
sheet = book.sheet_by_name("基础小学")

sql = "create table XX_2017("
sql = sql + ""
commentsql = ""
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(7, 7):
        col = sheet.cell(r,1).value
        comment = sheet.cell(r, 2).value
        sql = sql + col + " VARCHAR2(50),"
        # commentsql = commentsql + "comment on column BASE_PRO_T_MAP." + col + " is '" + comment + "';\n"
        # print col
        # print comment


for i in range(0,69):
        col = "X_" + sheet.cell(7, i).value
        sql = sql + col + " VARCHAR2(255),"

# sql = sql + " primary key (ID) )"
print(sql)