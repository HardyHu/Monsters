# -*- coding: utf-8 -*-
'套餐1814用例-财务-用户费用-大额申请搜索功能'
__author__ = 'Hardy'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class case181401(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_checkCaiWuSouSuo(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        time.sleep(3)
        driver.find_element_by_id("phone").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=phone | ]]
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("phone").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=phone | ]]
        driver.find_element_by_id("wrapper").click()
        driver.find_element_by_id("login-btn").click()  #正式登陆
        time.sleep(3)
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='财务管理'])").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='押金管理'])[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='大额申请'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查看'])[1]/following::td[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='查看'])[1]/following::td[4] | ]]
        driver.find_element_by_id("customer__search_footable").click()
        driver.find_element_by_id("customer__search_footable").clear()
        driver.find_element_by_id("customer__search_footable").send_keys("18680661111")
        driver.find_element_by_id("customer__search_footable").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='»'])/../../li[last()-1]/a").click()  #想了很久才想起用..和last()。。。
        time.sleep(2)
        #(.//*[normalize-space(text()) and normalize-space(.)='»'])/preceding::li[1] //or using this one.
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='同意'])[1]/following::a[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        #寻找同意，表明页面内容正确
        wait_Assert = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='拒绝'])[1]/preceding::span[1]"))

        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='拒绝'])[1]/preceding::span[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='拒绝'])[1]/preceding::span[1] | ]]
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
