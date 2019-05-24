#!/usr/bin/evn python
# coding=utf-8
from bs4 import BeautifulSoup  #BeautifulSoup4模块
import pymysql #mysql-python模块



conn= pymysql.connect(
        host='192.168.3.115',
        # host='211.153.22.29',
        port = 3306,
        user='root',
        passwd='love431',
        db ='alengin',
        )

cursor = conn.cursor()


# 先获取所有上下册的教材
sql_a = "select t.code,t.TERM from base_book_catelog t where LENGTH(t.`CODE`) = 12 "


# 循环获取数据并保存数据
cursor.execute(sql_a)
result = cursor.fetchall()
for i,row in enumerate(result):
    code = row[0]
    term = row[1]
    # print(content)
    # 执行更新操作
    # print(str(id) + ":" + str(newContent))
    # 更新这条语句
    upSql = """ UPDATE base_book_catelog t SET t.TERM = %s WHERE 1 = 1 AND t. CODE LIKE %s """
    code = code + '%'
    upresult = cursor.execute(upSql,(term,code))

    # print(upresult)
    print("当前执行为:" + str(i+1) + "/" + str(len(result)))




cursor.close()
conn.commit()
conn.close()

print("==============================执行完成====================================")