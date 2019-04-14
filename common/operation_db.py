import MySQLdb.cursors
import json


class OperationMysql:
    def __init__(self):
        # 打开数据库连接
        self.con = MySQLdb.connect(
            host='100.87.0.121',
            port=3306,
            user='root',
            password='123456',
            db='lvyue_pimp_test',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        # 使用cursor()方法获取操作游标
        self.cur = self.con.cursor()

    # 查询数据库
    def search_one(self,sql):
            self.cur.execute(sql)  # 执行sql语句
            result = self.cur.fetchone()  # 获取查询结果集
            # result = json.dumps(result)  # 转换为字符串
            return result

if __name__ == '__main__':
    om = OperationMysql()
    sql = "select title_name from t_pimp_notice where id = 100"
    res = om.search_one(sql)
    print(type(res),res)