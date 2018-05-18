# coding=utf-8
import xlrd
import sys

book = xlrd.open_workbook("data.xlsx")
sheet = book.sheet_by_name("a")

sql = "create table BASE_PRO_T_MAP("
sql = sql + " ID       VARCHAR2(50) not null,"
commentsql = "comment on table BASE_PRO_T_MAP is '项目教师MAP';\n"
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(2, 30):
        col = sheet.cell(r,1).value
        comment = sheet.cell(r, 2).value
        sql = sql + col + " VARCHAR2(50),"
        commentsql = commentsql + "comment on column BASE_PRO_T_MAP." + col + " is '" + comment + "';\n"
        # print col
        # print comment

sql = sql + " primary key (ID) )"
print(sql)
print(commentsql)