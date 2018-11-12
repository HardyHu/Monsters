# -*- coding: utf-8 -*-
__author__ = 'Hardy'
'测试中控已绑数据、并查看已绑车辆的信息查询'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class Car(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_car(self):
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
        except:print('Element is None~')
        ######
        driver.find_element_by_link_text(u"中控").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(u"//*[@id='operation-battery']/div[1]/section//li[2]/a").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='G5000000015'])//following::td[text()=1111]").click()
        register_time = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册时间:'])/following::div[1]")
        ActionChains(driver).double_click(register_time).perform()

        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册时间:'])[1]/following::div[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='注册时间:'])[1]/following::div[1] | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册时间:'])/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='G5000000015'])/../../td[@class][last()]/a").click()
        time.sleep(2)
        #校验句柄
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                driver.implicitly_wait(10)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
                driver.find_element_by_id("date").click()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='«'])[1]/following::th[1]").click()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='«'])[2]/following::th[1]").click()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='»'])[3]/following::span[text()='2018']").click()  #选择2018年
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='»'])[2]/following::span[text()='11月']").click()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日'])[1]/following::td[text()='12']").click()  #选择2018.11.12完成
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日期'])[1]/following::button[1]").click()
                time.sleep(2)
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查询'])[1]/following::button[1]").click()
                driver.close()

        # driver.switch_to_window(now_handle)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        driver.switch_to_window(now_handle)
        driver.find_element_by_id("operation-battery").click()
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
