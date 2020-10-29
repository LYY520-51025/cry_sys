from cry_sys.db.handlesql import Dboperation


class CustomerOperationDb:
    def __init__(self):
        self.dbop=Dboperation(host='www.summermori.icu',user='root',password='123456',database='crm',port=3306,charset='utf8')

    def dele_customer(self,sql):
        self.dbop.delet(sql)

    def search_customer(self,sql):
        data=self.dbop.search(sql)
        return  data
    def add_customer_db_data(self,sql):
        lst=[]
        data = self.dbop.search(sql)
        lst.append(data[0][5])
        lst.append(data[0][10])
        lst.append(data[0][16])
        lst.append(data[0][18])
        return lst


#
# c=CustomerOperationDb()
# c.dbop.get_connection()
# #c.dele_customer("DELETE FROM customer_info WHERE customer_name='ba3ba'")
# a=c.search_customer('select * from customer_info')
# ab=c.add_customer_db_data('select * from customer_info')
# print(ab)
# c.dbop.con_close()

