# -*- coding: utf-8 -*-
__author__ = 'Hardy'
'will add TestSuite/TestSkip & TestCase/TestLoader/TestReporter in the near future'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


#健壮登录模块
class Loginhoutai_TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  #智能等待
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Fullscreen(self):
        # driver = self.driver
        # driver.get("http://119.23.155.83:8090/")
        # driver.find_element_by_id("phone").clear()
        # driver.find_element_by_id("phone").send_keys("18138819495")
        # driver.find_element_by_id("mima").clear()
        # driver.find_element_by_id("mima").send_keys("123456")

        # driver.find_element_by_id("login-btn").click()
        # time.sleep(5)
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='全屏'])[1]/following::input[1]").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日'])[2]/following::td[6]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='to'])[1]/following::input[1]").click()
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日'])[2]/following::td[15]").click()
        # driver.find_element_by_id("date-range-go").click()
        print('This is a test:know myself')
    
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
