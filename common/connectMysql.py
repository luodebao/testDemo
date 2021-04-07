import pymysql
# 引入readConfig的包
from conf import readConfig


# import json

# 定义一个公共类
class ConnectMysql():
    def select_db(selct_sql):
        db = pymysql.connect(
            # 调用readConfig中的方法get_mysql方法给数据库连接赋值
            host=readConfig.ReadConfig.get_mysql("host"),  # 本地数据库
            port=int(readConfig.ReadConfig.get_mysql('port')),
            user=readConfig.ReadConfig.get_mysql("user"),  # 账号
            password=readConfig.ReadConfig.get_mysql("password"),  # 密码
            db=readConfig.ReadConfig.get_mysql("db")  # 数据库名称
        )
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出DictCursor
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        # 使用 execute() 执行sql
        cursor.execute(selct_sql)
        while True:
            # fetchone(),单个显示
            data = cursor.fetchone()
            if data is None:
                break
            print(data)
        # data = cursor.fetchmany(2)
        # print(type(data))
        # print(type(data))
        # 全部data = cursor .fetchall()
        # 多个data = cursor.fetchmany()
        # 关闭游标
        cursor.close()
        db.commit()
        # 关闭数据库连接
        db.close()
        return data

    # 查询的sql添加
    select_sql = "select score  from student,sc,course where student.sid = sc.sid and sc.cid = course.cid and cname = 'physics' "
    print(select_db(select_sql))

    def insert_db(insert_sql):
        db = pymysql.connect(
            # 调用readConfig中的方法get_mysql方法给数据库连接赋值
            host=readConfig.ReadConfig.get_mysql("host"),  # 本地数据库
            port=int(readConfig.ReadConfig.get_mysql('port')),
            user=readConfig.ReadConfig.get_mysql("user"),  # 账号
            password=readConfig.ReadConfig.get_mysql("password"),  # 密码
            db=readConfig.ReadConfig.get_mysql("db")  # 数据库名称
        )
        # 创建游标
        cursor = db.cursor()
        try:
            cursor.execute(insert_sql)
            db.commit()
        except Exception as e:
            print("插入数据错误".format(e))
            # 回滚
            db.rollback()
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()

    # 插入的sql添加
    insert_sql = "INSERT INTO student VALUES('4','利好','1997-07-05','英语'，'99')"  # INSERT INTO student VALUES[('4','lisi','7','物理','8'),('5','lisi33','75','化学','78')]
    print(insert_db(insert_sql))

    # 更新数据库
    def update_db(update_sql):
        db = pymysql.connect(
            # 调用readConfig中的方法get_mysql方法给数据库连接赋值

            host=readConfig.ReadConfig.get_mysql("host"),  # 本地数据库
            port=int(readConfig.ReadConfig.get_mysql('port')),
            user=readConfig.ReadConfig.get_mysql("user"),  # 账号
            password=readConfig.ReadConfig.get_mysql("password"),  # 密码
            db=readConfig.ReadConfig.get_mysql("db")  # 数据库名称
        )
        # 创建游标
        cursor = db.cursor()
        try:
            cursor.execute(update_sql)
            db.commit()
        except Exception as e:
            print("更新数据错误".format(e))
            # 回滚
            db.rollback()
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()

    # 更新的sql添加
    update_sql = ""  # update student set birthday = 3 where id = 1
    print(update_db(update_sql))

    # 删除数据库
    def delete_db(delete_sql):
        db = pymysql.connect(
            # 调用readConfig中的方法get_mysql方法给数据库连接赋值
            host=readConfig.ReadConfig.get_mysql("host"),  # 本地数据库
            port=int(readConfig.ReadConfig.get_mysql('port')),
            user=readConfig.ReadConfig.get_mysql("user"),  # 账号
            password=readConfig.ReadConfig.get_mysql("password"),  # 密码
            db=readConfig.ReadConfig.get_mysql("db")  # 数据库名称
        )
        # 创建游标
        cursor = db.cursor()
        try:
            cursor.execute(delete_sql)
            db.commit()
        except Exception as e:
            print("删除数据错误".format(e))
            # 回滚
            db.rollback()
        finally:
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            db.close()

    # 删除的sql添加
    delete_sql = ""  # delete_sql = "delete from student where id = 2"#
    print(delete_db(delete_sql))


if __name__ == 'main':
    select_sql = ConnectMysql.select_db(
        "select score  from student,sc,course where student.sid = sc.sid and sc.cid = course.cid and cname = 'physics'")
