# coding=utf-8
import MySQLdb
import xlrd


book = xlrd.open_workbook("f:\\test\\data.xlsx")
sheet = book.sheet_by_name("Sheet1")

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )

cursor = conn.cursor()

sql = "insert into test1(Keyword,C1,UT) values(%s,%s,%s)"


# 循环获取数据并保存数据
for r in range(1, sheet.nrows):
        Keyword = sheet.cell(r,0).value
        C1 = sheet.cell(r,1).value
        UT = sheet.cell(r, 2).value

        cursor.execute(sql,(Keyword,C1,UT))



cursor.close()
conn.commit()
conn.close()