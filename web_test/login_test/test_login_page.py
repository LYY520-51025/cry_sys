import sys
#执行目录，从根目录开始
from cry_sys.base.broweroperation import BrowserOperation
from cry_sys.base.usebrowser import UseBrowser
from cry_sys.config.log_crm import Log_auto

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\demo')
import unittest
from HTMLTestRunner import HTMLTestRunner
from cry_sys.util.excel_operration import opertion
from cry_sys.web_func.usermanager.login_page import Case

from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    def setUp(self) -> None:
        self.case=Case()

        self.opertion = opertion('C:/Users/Administrator/PycharmProjects/demo/cry_sys/config/asd.xlsx', 'login')
    def test_case_1_login_right(self):
        self.case.case_login(self.opertion.get_cell(1,3),self.opertion.get_cell(1,4))
        a=self.case.case_1_login_right()
        self.assertEqual(self.opertion.get_cell(1,1),a)
    def test_case_2_login_null_name(self):
        self.case.case_login(self.opertion.get_cell(2,3),self.opertion.get_cell(2,4))
        a = self.case.case_2_login_null_name()
        self.assertEqual(self.opertion.get_cell(2,1),a)
    def test_case_3_login_null_password(self):
        self.case.case_login(self.opertion.get_cell(3,3),self.opertion.get_cell(3,4))
        a=self.case.case_3_login_null_password()
        self.assertEqual(self.opertion.get_cell(3,1),a)
    def test_case_4_login_null_password_name(self):
        self.case.case_login(self.opertion.get_cell(4,3),self.opertion.get_cell(4,4))
        a=self.case.case_4_login_null_password_name()
        self.assertEqual(self.opertion.get_cell(4,1), a)
    def test_case_5_login_erro_password(self):
        self.case.case_login(self.opertion.get_cell(5,3),self.opertion.get_cell(5,4))
        a=self.case.case_5_login_erro_password()
        self.assertEqual(self.opertion.get_cell(5,1),a)
    def test_case_6_login_erro_name(self):
        self.case.case_login(self.opertion.get_cell(6,3),self.opertion.get_cell(6,4))
        a=self.case.case_6_login_erro_name()
        self.assertEqual(self.opertion.get_cell(6,1),a)
    # def test_case_7_add(self):
    #     self.case.case_login(self.opertion1.get_cell(1,3),self.opertion1.get_cell(1,4))
    #     self.bo.case_change()
    #     a=self.case.case_add(self.opertion1.get_cell(1,5),self.opertion1.get_cell(1,6),self.opertion1.get_cell(1,7),self.opertion1.get_cell(1,8),self.opertion1.get_cell(1,9))
    #     self.assertEqual(self.opertion1.get_cell(1,1), a)
    # def test_case_8_modefly(self):
    #     self.case.case_login(self.opertion2.get_cell(1,3),self.opertion2.get_cell(1,4))
    #     self.case.case_change()
    #     a=self.case.case_modefiy(self.opertion2.get_cell(1,5))
    #     self.assertEqual(self.opertion2.get_cell(1,1),a)
    def tearDown(self) -> None:
        time.sleep(4)
        self.case.ub.quit()



if __name__ == '__main__':

    ###生成HTML报告report
    #创建套件
    suit=unittest.TestSuite()
    #创建case
    tset_case=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    #添加case
    suit.addTest(tset_case)
    print(time.localtime())
    now_time=time.strftime('%y-%m-%d',time.localtime())
    with open('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\report\\login+sreport'+now_time+'.html','wb+') as file:
        runner=HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description=None)

    # 运行case
        runner.run(suit)