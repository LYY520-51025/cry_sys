import sys
#执行目录，从根目录开始
# from cry_sys.base.broweroperation import BrowserOperation
# from cry_sys.base.usebrowser import UseBrowser
# from cry_sys.config.log_crm import Log_auto
# from cry_sys.web_func.Customer_page.customer_add import Case1
sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\demo')
from cry_sys.web_func.Customer_page.customer_add import Case1
import unittest
from HTMLTestRunner import HTMLTestRunner
from cry_sys.util.excel_operration import opertion
import time

class MyTestCase1(unittest.TestCase):


    def setUp(self) -> None:
        self.case1=Case1()
        self.opertion1 = opertion('C:/Users/Administrator/PycharmProjects/demo/cry_sys/config/asd.xlsx', 'add')


    def test_case_1_add(self):
        self.case1.case_login(self.opertion1.get_cell(1,3),self.opertion1.get_cell(1,4))
        a=self.case1.case1_add(Customer_name=self.opertion1.get_cell(1,5),Customer_position=self.opertion1.get_cell(1,6),Customer_birthday=self.opertion1.get_cell(1,7),Creater=self.opertion1.get_cell(1,8),Customer_Email=self.opertion1.get_cell(1,9))
        self.assertEqual(self.opertion1.get_cell(1,1), a)


    def tearDown(self) -> None:
        self.case1.bo.quit()



if __name__ == '__main__':

    ###生成HTML报告report
    #创建套件
    suit1=unittest.TestSuite()
    #创建case
    tset_case1=unittest.TestLoader().loadTestsFromTestCase(MyTestCase1)
    #添加case
    suit1.addTest(tset_case1)
    print(time.localtime())
    now_time=time.strftime('%y-%m-%d',time.localtime())
    with open('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\report\\Customer+sreport'+now_time+'.html','wb+') as file:
        runner=HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description=None)

    # 运行case
        runner.run(suit1)