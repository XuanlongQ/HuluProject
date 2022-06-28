# test mysql is useful

import pymysql
import yaml

# 打开数据库连接
def open_db(host, user_name, password, db_name,port):
    # 打开数据库连接
    db = pymysql.connect(host =host , user = user_name, password = password, database= db_name,port = port)
    return db


# 获取游标
def get_cursor(db):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return cursor


# 执行sql(创建、修改、删除)
def sql_commit(db, cursor, sql, param=None):
    try:
        # 执行sql语句
        cursor.execute(sql, param)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
        return False

    return True

# 查询
def sql_fetch(cursor, sql):
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return results


# 关闭数据库连接
def close_db(db, cursor):
    cursor.close()
    db.close()
    
    
if __name__ == "__main__":
    file = open('pro/conf/config.yaml', 'r', encoding="utf-8")
    file_data = file.read()                 
    file.close()
    
    data = yaml.load(file_data,Loader=yaml.FullLoader) 
    print(data["DB"]["host"],type(data["DB"]["host"]))
    
    host =  data["DB"]["host"]
    user_name = data["DB"]["userName"]
    password = data["DB"]["passWord"]
    db_name = data["DB"]["dbName"]
    port = data["DB"]["port"]

    db = open_db(host,user_name,password,db_name,port)
    print(db)
    # 获取游标
    cursor = get_cursor(db)
    print(cursor,type(cursor))

    try:
    	sql = "select * from users"
	    results = sql_fetch(cursor, sql)
	    print(results) 
    except:
        print("error")
    finally:
       close_db(db, cursor)
