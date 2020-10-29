




import pymysql
class reserch:

    def search_all(self):
        try:
            #创建链接
            conn=pymysql.Connection(host='localhost', user='root', password="123456",
                             database='jspxcms', port=3307,charset='utf8')
            #创建游标
            cur=conn.cursor()

            #sql
            sql='SELECT * FROM cms_ad_slot'

            #执行sql
            cur.execute(sql)

            #游标的fetchall获取数据
            res=cur.fetchall()

            #打印数据
            print(res)
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            #关闭游标，关闭连接
            cur.close()
            conn.close()