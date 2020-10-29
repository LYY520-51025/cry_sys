from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

from cry_sys.base.broweroperation import BrowserOperation
from cry_sys.base.usebrowser import UseBrowser
from cry_sys.config.log_crm import Log_auto
from cry_sys.util.yaml_operration import YamlOperation




class Case:

    def __init__(self):
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://www.summermori.icu:8080/crm')
        self.log=Log_auto()
        self.yaml_oper=YamlOperation('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\config\\qwe.yaml')
    def case_login(self,name,password):
        self.bo.send_keys(self.yaml_oper.get_data('login','username'),name)
        self.bo.send_keys(self.yaml_oper.get_data('login','password'),password)
        time.sleep(2)
        self.bo.click_element(self.yaml_oper.get_data('login','log'))

    def case_1_login_right(self):
        a=self.bo.change_window()
        return a
    def case_2_login_null_name(self):
        a = self.bo.alert_text()
        return a
    def case_3_login_null_password(self):
        a = self.bo.alert_text()
        return a
    def case_4_login_null_password_name(self):
        a = self.bo.alert_text()
        c=a[0:4]+a[11:19]
        return c
    def case_5_login_erro_password(self):
        a = self.bo.alert_text()
        return a
    def case_6_login_erro_name(self):
        a = self.bo.alert_text()
        return a
    # def case_add(self,Customer_name,Customer_position,Customer_birthday,Creater,Customer_Email):
    #     self.bo.case_change()
    #     self.bo.click_element(self.yaml_oper.get_data('case_add','add'))
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','add'), 'info')
    #     self.bo.send_keys(self.yaml_oper.get_data('case_add','Customer_name'),Customer_name)
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','Customer_name'),'info')
    #     self.bo.send_keys(self.yaml_oper.get_data('case_add','Customer_position'),Customer_position)
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','Customer_position'),'info')
    #     self.bo.execute_script()
    #     self.bo.send_keys(self.yaml_oper.get_data('case_add','Customer_birthday'),Customer_birthday)
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','Customer_birthday'),'info')
    #     time.sleep(1)
    #     self.bo.send_keys(self.yaml_oper.get_data('case_add','Creater'),Creater)
    #     self.bo.send_keys(self.yaml_oper.get_data('case_add','Customer_Email'),Customer_Email)
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','Customer_Email'),
    #                      'info')
    #     self.bo.click_element(self.yaml_oper.get_data('case_add','submit'))
    #     self.log.set_msg(self.yaml_oper.get_data('case_add','Customer_Email'),'info')
    #     a=self.bo.alert_text()
    #     return a

    # def case_modefiy(self,ipone):
    #     self.driver.find_element_by_xpath(self.yaml_oper.get_data('case_modefiy','edit')).click()
    #     self.log.set_msg(self.yaml_oper.get_data('case_modefiy','edit'),
    #                      'info')
    #     self.driver.find_element_by_xpath(self.yaml_oper.get_data('case_modefiy','ipone')).clear()
    #     self.log.set_msg(self.yaml_oper.get_data('case_modefiy','ipone'),'info')
    #     self.driver.find_element_by_xpath(self.yaml_oper.get_data('case_modefiy','ipone')).send_keys(ipone)
    #     self.log.set_msg(
    #         self.yaml_oper.get_data('case_modefiy','ipone'),
    #         'info')
    #     self.driver.find_element_by_xpath(self.yaml_oper.get_data('case_modefiy','submit')).click()
    #     self.log.set_msg(
    #         self.yaml_oper.get_data('case_modefiy','submit'),
    #         'info')
    #     alert = Alert(self.driver)
    #     a = alert.text
    #     alert.accept()
    #     time.sleep(4)
    #     return a

# case=Case()
#
# case.case_login('admin','123456')
#
# case.case_add('1','1','1','1','z')
# case.case_modefiy()

