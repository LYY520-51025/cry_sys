# -*- coding: utf-8 -*-
# @Time    : 2020-10-26 10:26
# @Author  : baiping
# @qq      :376706275
from selenium import webdriver
import time

class UseBrowser:

    driver = None

    def __init__(self):
        #py文件在后台运行
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver=webdriver.Chrome('C:\\Users\\Administrator\\PycharmProjects\\demo\\cry_sys\\chromedriver.exe',chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        UseBrowser.driver = self.driver


    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()


