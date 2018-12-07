# -*- coding: utf-8 -*-
'运营-电池-检查电池表单数据'

__author__ = 'Hardy'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class CheckBattery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_battery(self):
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
        #####
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"电池").click()
        driver.find_element_by_id("customer__search_footable").click()
        driver.find_element_by_id("customer__search_footable").clear()
        driver.find_element_by_id("customer__search_footable").send_keys("13636035190")
        time.sleep(2)
        #校验列表无数据
        content = driver.find_element_by_id(u"test-table__table-wrap").text
        self.assertEqual(content,u"无数据")
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=test-table__table-wrap | ]]
        # driver.find_element_by_id("test-table__table-wrap").click()
        driver.find_element_by_id("customer__search_footable").click()
        driver.find_element_by_id("customer__search_footable").clear()
        # driver.find_element_by_id("customer__search_footable").send_keys("")  #Keys.ENTER
        # driver.find_element_by_id("customer__search_footable").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"电池").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(u"//*[@id='operation-battery']//p").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(u"//*[@id='pagination']/div/div/ul/li[last()-1]/a").click()  #翻页倒一
        driver.implicitly_wait(10)
        #校验表单字段
        th_last = driver.find_element_by_xpath(u"//*[@id='test-table__table-wrap']/table/thead/tr/th[last()-1]").text
        print(th_last)
        self.assertEqual(th_last,u"出厂时间")
        time.sleep(2)
        #校验表单里的数据，用户列存在数据：181***860
        td_phone = driver.find_element_by_xpath(u"//*[@id='test-table__table-wrap']/table/tbody/tr[last()]//a").text  #容易报错
        print(td_phone)
        self.assertEqual(td_phone,u"18194082860")
        time.sleep(2)
        js = "var q = document.documentElement.scrollTop=0"
        driver.execute_script(js)
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='扫描时间'])[1]/following::th[1] | ]]
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='扫描时间'])[1]/following::th[1]").click()

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
