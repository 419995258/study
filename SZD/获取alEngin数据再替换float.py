# coding=utf-8
from bs4 import BeautifulSoup  #BeautifulSoup4模块
import pymysql #mysql-python模块



conn= pymysql.connect(
        host='192.168.3.115',
        port = 3306,
        user='root',
        passwd='love431',
        db ='alengin',
        )

cursor = conn.cursor()

sql = "select t.item_id,t.CONTENT from al_res_tiankong_item t where  t.CONTENT like '%float:left;%' "


# 循环获取数据并保存数据
cursor.execute(sql)
result = cursor.fetchall()
for i,row in enumerate(result):
    id = row[0]
    content = row[1]
    # print(content)
    # 执行更新操作
    # print(str(id) + ":" + str(newContent))
    content = content.replace('float:left;','')
    # 更新这条语句
    upSql = """ update al_res_danxuan_choice t set t.CONTENT = %s where t.choice_id = %s """
    upresult = cursor.execute(upSql,(content,id))

    # print(upresult)
    print("当前执行为:" + str(i+1) + "/" + str(len(result)))




cursor.close()
conn.commit()
conn.close()