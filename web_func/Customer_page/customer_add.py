from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

from cry_sys.base.broweroperation import BrowserOperation
from cry_sys.base.usebrowser import UseBrowser
from cry_sys.config.log_crm import Log_auto
from cry_sys.db.customerDb.customeroperdb import CustomerOperationDb
from cry_sys.db.handlesql import Dboperation
from cry_sys.util.yaml_operration import YamlOperation


class Case1:

    def __init__(self):
        self.ub = UseBrowser()
        self.co=CustomerOperationDb()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://www.summermori.icu:8080/crm')
        self.log=Log_auto()
        self.yaml_oper=YamlOperation('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\config\\qwe.yaml')
    def case_login(self,name,password):
        self.bo.send_keys(self.yaml_oper.get_data('login','username'),name)
        self.bo.send_keys(self.yaml_oper.get_data('login','password'),password)
        time.sleep(2)
        self.bo.click_element(self.yaml_oper.get_data('login','log'))

    def case1_add(self, **key):
        self.key=key
        time.sleep(2)
        self.bo.case_change(self.yaml_oper.get_data('case_change','frame'))
        time.sleep(2)
        self.bo.click_element(self.yaml_oper.get_data('case_change', 'Customer'))
        time.sleep(2)
        self.bo.case_change(self.yaml_oper.get_data('case_change', 'pframe'))

        time.sleep(2)
        self.bo.click_element(self.yaml_oper.get_data('case_add', 'add'))
        time.sleep(2)
        self.log.set_msg(self.yaml_oper.get_data('case_add', 'add'), 'info')
        self.bo.send_keys(self.yaml_oper.get_data('case_add', 'Customer_name'), key.get('Customer_name',''))
        self.log.set_msg(self.yaml_oper.get_data('case_add', 'Customer_name'), 'info')
        # self.bo.send_keys(self.yaml_oper.get_data('case_add', 'Customer_position'), key.get('Customer_position',''))
        # self.log.set_msg(self.yaml_oper.get_data('case_add', 'Customer_position'), 'info')
        self.bo.execute_script()
        self.bo.send_keys(self.yaml_oper.get_data('case_add', 'Customer_birthday'), key.get('Customer_birthday',''))
        self.log.set_msg(self.yaml_oper.get_data('case_add', 'Customer_birthday'), 'info')
        time.sleep(1)
        self.bo.send_keys(self.yaml_oper.get_data('case_add', 'Creater'), key.get('Creater',''))
        self.bo.send_keys(self.yaml_oper.get_data('case_add', 'Customer_Email'), key.get('Customer_Email',''))
        self.log.set_msg(self.yaml_oper.get_data('case_add', 'Customer_Email'),
                         'info')
        self.bo.click_element(self.yaml_oper.get_data('case_add', 'submit'))
        self.log.set_msg(self.yaml_oper.get_data('case_add', 'Customer_Email'), 'info')
        a = self.bo.alert_text()
        return a



    def check_db_id_name(self):
        page_content = []
        page_content.append(self.key['Customer_name'])
        print(page_content)
        data = self.co.search_customer(
            "select * from customer_info where customer_name='" + self.key['name'] + "'")
        if page_content == self.co.add_customer_db_data(data):
            return True
        return False

# c=Case1()
# c.case_login('admin','123456')
# c.case1_add(Customer_name='离网吧',Customer_birthday='2020-10-10 22:22:22',Customer_Email='877268655@qq.com',Creater='王五')
# c.check_db_id_name()
