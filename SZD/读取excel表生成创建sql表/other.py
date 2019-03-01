# coding=utf-8
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')



book = xlrd.open_workbook("000.xls")
sheet = book.sheet_by_name("a")
str = "create table TJ_STAT_BASE_TEACHER_INFO(ID VARCHAR2(50) not null,AREA_ID VARCHAR2(50),PROVINCE_ID VARCHAR2(50),CITY_ID VARCHAR2(50),COUNTY_ID VARCHAR2(50),"
commentsql = "comment on table TJ_STAT_BASE_TEACHER_INFO is '统计——教师表';\n"
# 循环获取数据并保存数据，获取从第2行到30的数据
# for r in range(2, sheet.nrows):
for r in range(63, 71):
        # str = str + "col" + bytes(r) + " VARCHAR2(200),"
        comment = sheet.cell(3, r).value
        commentsql = commentsql + "comment on column TJ_STAT_BASE_TEACHER_INFO.col" + bytes(r-2) + " is '" + comment + "';\n"
        print comment

print commentsql