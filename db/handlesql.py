import pymysql
class Dboperation:
    def __init__(self,host,user,password,database,port,charset):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.charset=charset
        # 创建链接
    def get_connection(self):
        try:
            self.conn = pymysql.Connection(host=self.host, user=self.user, password=self.password,database=self.database, port=self.port, charset=self.charset)
            return self.conn
        except Exception as e:
            print(e,'connect error')
    def search(self,sql):
        # 创建游标
        cur = self.conn.cursor()
        try:

            #sql
            #sql='SELECT * FROM customer_info'

            #执行sql
            cur.execute(sql)
            #游标的fetchall获取数据
            res=cur.fetchall()

            #打印数据
            print(res)
            return res
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            #关闭游标，关闭连接
            cur.close()




    def update(self,sql):
        # 创建游标
        cur = self.conn.cursor()
        try:

            # sql
            #sql = "UPDATE customer_info SET customer_name='李qw王' WHERE customer_id=1"

            # 执行sql
            cur.execute(sql)
            self.conn.commit()
            # 游标的fetchall获取数据


            # 打印数据

        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 关闭游标，关闭连接
            cur.close()





    def delet(self,sql):
        # 创建游标
        cur = self.conn.cursor()
        try:

            # sql#sql = "DELETE FROM customer_info WHERE customer_name='温庆心'"

            # 执行sql
            cur.execute(sql)
            self.conn.commit()
            # 游标的fetchall获取数据

            # 打印数据

        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 关闭游标，关闭连接
            cur.close()



    def add(self,sql):
        # 创建游标
        cur = self.conn.cursor()
        try:

            # sql
            #sql = "INSERT INTO customer_info ( customer_name,customer_email,birth_day,customer_addman ) VALUES ( 'ba3ba','877268655@qq.com','2018-05-05 22:22:22','die' );"

            # 执行sql
            cur.execute(sql)
            self.conn.commit()
            # 游标的fetchall获取数据

            # 打印数据

        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 关闭游标，关闭连接
            cur.close()
    def con_close(self):
        self.conn.close()
# c=Dboperation(host='localhost',user='root',password='123456',database='crm',port=3307,charset='utf8')
# c.get_connection()
# #c.update("UPDATE customer_info SET customer_name='李qw王' WHERE customer_id=1")
# c.delet("DELETE FROM customer_info WHERE customer_name='ba3ba'")
# c.add("INSERT INTO customer_info ( customer_name,customer_email,birth_day,customer_addman ) VALUES ( 'ba3ba','877268655@qq.com','2018-05-05 22:22:22','die' );")
# c.search('SELECT * FROM customer_info')
# c.con_close()