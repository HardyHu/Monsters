# -*- coding: utf-8 -*-
'运营-轨迹热力图，测试热力图日期选择和查询功能，检查地图'

__author__ = 'Hardy'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HotMap(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_hot_map(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("login-btn").click()
        ######
        try:
            driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']")
            element_w = driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button")
            if element_w.is_displayed():
                element_w.click()
            else:print('No Alert Present!')
        except:print('Nothing happend.')
        ######
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"轨迹热力图").click()
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("start-time").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Clear'])[2]/following::th[2]").click()  #开始选择日期2018.06.01 6:00
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='五月'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::td[6]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Clear'])[1]/following::span[9]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='© 2018 AutoNavi'])[1]/following::span[3]").click()
        driver.find_element_by_id("end-time").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[2]/following::th[1]").click()  #开始选择截止日期
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查询'])").click()  #点击查询
        time.sleep(2)
        driver.maximize_window()
        origin = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='恢复默认（查询最近7天）'])[1]/following::div[23]").click()  #尝试拖拽地图，如果地图存在，则可以拖拽
        # target = driver.find_element_by_xpath()
        js = "var q = document.documentElement.scrollTop=0"  #滚动到顶部
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='恢复默认（查询最近7天）'])").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查询'])").click()


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
