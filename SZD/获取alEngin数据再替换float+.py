#!/usr/bin/evn python
# coding=utf-8
import pymysql #mysql-python模块

# UPDATE al_res_danxuan_item t set t.CONTENT = replace(t.CONTENT,'/alres','/alEngin');
# UPDATE al_res_danxuan_choice t set t.CONTENT = replace(t.CONTENT,'/alres','/alEngin');
# UPDATE al_res_zhuguan_item t set t.CONTENT = replace(t.CONTENT,'/alres','/alEngin');
# UPDATE al_res_tiankong_item t set t.CONTENT = replace(t.CONTENT,'/alres','/alEngin');
# UPDATE al_res_danxuan_item t set t.HOWTO = replace(t.HOWTO,'/alres','/alEngin');
# UPDATE al_res_zhuguan_item t set t.HOWTO = replace(t.HOWTO,'/alres','/alEngin');
# UPDATE al_res_tiankong_item t set t.HOWTO = replace(t.HOWTO,'/alres','/alEngin');





'''填空题'''
def tianKongItem():
    sql = """select t.item_id,t.CONTENT from al_res_tiankong_item t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_tiankong_item t set t.CONTENT = %s where t.item_id = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_tiankong_item:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)

'''单选题'''
def danXuanItem():
    sql = """select t.item_id,t.CONTENT from al_res_danxuan_item t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_danxuan_item t set t.CONTENT = %s where t.item_id = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_danxuan_item:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)

'''多选题'''
def duoXuanItem():
    sql = """select t.item_id,t.CONTENT from al_res_duoxuan_item t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_duoxuan_item t set t.CONTENT = %s where t.item_id = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_duoxuan_item:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)

'''主观题'''
def zhuGuanItem():
    sql = """select t.item_id,t.CONTENT from al_res_zhuguan_item t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_zhuguan_item t set t.CONTENT = %s where t.item_id = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_zhuguan_item:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)


'''单选题选项'''
def danXuanChoice():
    sql = """select t.CHOICE_ID,t.CONTENT from al_res_danxuan_choice t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_danxuan_choice t set t.CONTENT = %s where t.CHOICE_ID = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_danxuan_choice:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)

'''多选题选项'''
def duoXuanChoice():
    sql = """select t.CHOICE_ID,t.CONTENT from al_res_duoxuan_choice t where  t.CONTENT like '%align=left%' or  t.CONTENT like '%align="left"%'  """

    # 循环获取数据并保存数据
    cursor.execute(sql)
    result = cursor.fetchall()
    for i, row in enumerate(result):
        id = row[0]
        content = row[1]
        try:
            # 执行更新操作
            content = content.replace('align=left', '')
            content = content.replace('align="left"', '')
            # 更新这条语句
            upSql = """ update al_res_duoxuan_choice t set t.CONTENT = %s where t.CHOICE_ID = %s """
            cursor.execute(upSql, (content, id))
            print("当前执行为al_res_duoxuan_choice:" + str(i + 1) + "/" + str(len(result)))
        except Exception as e:
            print("异常id为:", id)


if __name__ == '__main__':
    conn = pymysql.connect(
        host='192.168.3.115',
        # host='211.153.22.29',
        port=3306,
        user='root',
        passwd='love431',
        db='alengin2',
    )

    cursor = conn.cursor()

    # 题目
    tianKongItem()
    danXuanItem()
    duoXuanItem()
    zhuGuanItem()

    # 选项
    danXuanChoice()
    duoXuanChoice()

    print("==============================执行完成====================================")


    cursor.close()
    conn.commit()
    conn.close()