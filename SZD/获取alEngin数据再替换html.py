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
        db ='alengin2',
        )

cursor = conn.cursor()

# 单选选项
sql = "select t.CHOICE_ID,t.CONTENT from al_res_danxuan_choice t where  t.CONTENT like '<html%' "



# 循环获取数据并保存数据
cursor.execute(sql)
result = cursor.fetchall()
for i,row in enumerate(result):
    id = row[0]
    content = row[1]

    try:

        # print(content)
        # 执行更新操作
        soup = BeautifulSoup(content, 'lxml')
        sp = soup.select("body > div > p ")
        newContent = sp[0]
        # print(str(id) + ":" + str(newContent))
        # 更新这条语句
        upSql = """ update al_res_danxuan_choice t set t.CONTENT = %s where t.choice_id = %s """
        # upSql = """ update al_res_danxuan_item t set t.CONTENT = %s where t.ITEM_ID = %s """
        upresult = cursor.execute(upSql, (str(newContent), id))
        # print(upresult)
        print("当前执行为al_res_danxuan_choice:" + str(i + 1) + "/" + str(len(result)))
    except Exception as e:
        print("异常id为:",id)


# 单选题目
sql = "select t.ITEM_ID,t.CONTENT from al_res_danxuan_item t where  t.CONTENT like '<html%' "
# 循环获取数据并保存数据
cursor.execute(sql)
result = cursor.fetchall()
for i,row in enumerate(result):
    id = row[0]
    content = row[1]

    try:

        # print(content)
        # 执行更新操作
        soup = BeautifulSoup(content, 'lxml')
        sp = soup.select("body > div > p ")
        newContent = sp[0]
        # print(str(id) + ":" + str(newContent))
        # 更新这条语句
        # upSql = """ update al_res_danxuan_choice t set t.CONTENT = %s where t.choice_id = %s """
        upSql = """ update al_res_danxuan_item t set t.CONTENT = %s where t.ITEM_ID = %s """
        upresult = cursor.execute(upSql, (str(newContent), id))
        # print(upresult)
        print("当前执行为al_res_danxuan_item:" + str(i + 1) + "/" + str(len(result)))
    except Exception as e:
        print("异常id为:",id)





cursor.close()
conn.commit()
conn.close()

print("==============================执行完成====================================")