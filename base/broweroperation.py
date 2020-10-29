# -*- coding: utf-8 -*-
# @Time    : 2020-10-26 10:26
# @Author  : baiping
# @qq      :376706275
import time

from selenium.webdriver.common.alert import Alert

from cry_sys.util.yaml_operration import YamlOperation


class BrowserOperation:

    def __init__(self,driver):
        self.yaml_oper=YamlOperation('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\config\\qwe.yaml')
        self.driver =driver


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, 'element not find')

    # def get_text(self,xpath):
    #     try:
    #         text=self.driver.find_element_by_xpath(xpath).text
    #     except Exception as e:
    #         print(e, 'element not find')
    #     return text

    def case_change(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)
        # self.driver.switch_to.frame(self.yaml_oper.get_data('case_change', 'frame'))
        # time.sleep(2)
        # self.driver.find_element_by_xpath(self.yaml_oper.get_data('case_change', 'Customer')).click()
        # self.driver.switch_to.parent_frame()
        # self.driver.switch_to.frame(self.yaml_oper.get_data('case_change', 'pframe'))
        # time.sleep(1)
    def change_window(self):
        win = self.driver.window_handles
        self.driver.switch_to.window(win[-1])
        a=self.driver.title
        return a
    def alert_text(self):
        alert = Alert(self.driver)
        a = alert.text
        return a

    def execute_script(self):
        self.driver.execute_script(self.yaml_oper.get_data('case_add', 'execute_script'))

    def quit(self):
        self.driver.quit()



# if __name__=='__main__':
#     ub=UseBrowser()
#     bo=BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_keys('//*[@id="UserName"]','admin')
#     bo.send_keys('//*[@id="Password"]','admin')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UseBrowser.quit()
