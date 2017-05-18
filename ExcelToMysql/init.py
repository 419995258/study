# coding=utf-8
import MySQLdb
import xlrd


book = xlrd.open_workbook("f:\\test\\excel.xlsx")
sheet = book.sheet_by_name("Sheet1")

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )

cursor = conn.cursor()

sql = "insert into test1(name,age) values(%s,%s)"
'''cursor.execute(sql,('1','2'))'''
# wb = lw(filename='f:\\test\\excel.xlsx')
# ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])  # <worksheet "data">
#
# rows = ws.get_highest_row()  # 最大行数
# columns = ws.get_highest_column()  # 最大列数
#
# data = []
# for rx in range(2, rows + 1):
#         for cx in range(1, columns + 1):
#                 data.append(str(ws.cell(row=rx, column=cx).value))
#                 cursor.execute(sql,
#                     (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
#         data = []
for r in range(1, sheet.nrows):
        name = sheet.cell(r,0).value
        age = sheet.cell(r,1).value


        cursor.execute(sql,(name,age))



cursor.close()
conn.commit()
conn.close()