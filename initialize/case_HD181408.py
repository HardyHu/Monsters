# -*- coding: utf-8 -*-
__author__ = 'Hardy'
'测试新增押金，及列表筛选功能'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from random import randrange
import unittest, time, re

class CashPledge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cash_pledge(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("login-btn").click()
        driver.maximize_window()
        ######
        try:
            driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']")
            element_w = driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button")
            if element_w.is_displayed():
                element_w.click()
            else:print('No Alert Present!')
        except:print('Nothing happend.')
        ######
        num = randrange(100,672)
        input_name = 'AutoTestRandom' + str(num)
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"押金管理").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='创建押金'])[1]").click()  #(.//*[normalize-space(text()) and normalize-space(.)='创建押金'])/following::i/preceding::button[3]
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(input_name)
        driver.find_element_by_name("num").clear()
        driver.find_element_by_name("num").send_keys("1")
        driver.find_element_by_name("deposit").clear()
        driver.find_element_by_name("deposit").send_keys("671")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='添加'])").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='全部'])[2]").click()  
        #(.//*[normalize-space(text()) and normalize-space(.)='全部'])/following::span[contains(@class,'select2-selection__arrow')]  --contains()用法
        driver.find_element_by_id("select2-select_groupcode-container").click()
        time.sleep(2)
        driver.find_element_by_id("select2-select_groupcode-container").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='|'])[1]/following::img[1]").click()
        driver.find_element_by_id("logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
