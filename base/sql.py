# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/25  17:24
# 文件           :sql.py
# IDE            :PyCharm

import pymysql
import yaml


def get_sql_yaml(path="base/sql.yaml", param_hl=""):
    with open(path, "r") as f:
        data = yaml.load(stream=f)
    return data.get(param_hl)


def select_sql(query_sql, db_name):
    # 数据库连接
    db = pymysql.connect(*get_sql_yaml("sql.yaml", "mysql"), db_name)
    # 游标
    cursor = db.cursor()

    cursor.execute(query=query_sql)

    # 返回的是元组数据
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


def update_sql(query_sql, db_name):
    # 打开数据库连接
    # pymysql.connect("ip", "name", "pwd", "db")
    db = pymysql.connect(*get_sql_yaml("sql.yaml", "mysql"), db_name)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    try:
        # 执行sql语句
        cursor.execute(query_sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭指针
    cursor.close()
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    print(select_sql(query_sql="select uname from user where id=1", db_name="test1"))
    update_sql(query_sql="insert into user values(null,'h','l',null)", db_name="test1")
