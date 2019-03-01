# coding=utf-8
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

book = xlrd.open_workbook("000.xls")
sheet = book.sheet_by_name("a")

sql = "create table tp_pro_teacher("
sql = sql + ""
commentsql = "comment on table tp_pro_teacher is '项目用户成绩表';\n"
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(55, 67):
        col = sheet.cell(r,1).value
        comment = sheet.cell(r, 2).value
        sql = sql + col + " VARCHAR2(255),"
        commentsql = commentsql + "comment on column tp_pro_teacher." + col + " is '" + comment + "';\n"
        # print col
        # print comment

sql = sql + " primary key (ID) )"
print sql
print commentsql