# coding=utf-8
import MySQLdb   #安装exe文件





conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='news',
        )

cursor = conn.cursor()

sql = "insert into news(title,href,source,creTime,content) values(%s,%s,%s,%s,%s)"


# 循环获取数据并保存数据
for i in range(0, 3):
        cursor.execute(sql,("title2" + bytes(i),"/static/file/img/time.jpg","source"+bytes(i),"2018-05-22 17:40:00","content"+bytes(i)));
        print i



cursor.close()
conn.commit()
conn.close()