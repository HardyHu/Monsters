# -*- coding: utf-8 -*-
__author__ = 'Hardy'
'测试分布图，中控-scooter，及换电柜细点测试'
'''涉及到js操作、切片无元素点控操作、句柄处理'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class Scattergram(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_scattergram(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("login-btn").click()
        driver.maximize_window()
        ######
        # try:
        #     driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']")
        #     element_w = driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button")
        #     if element_w.is_displayed():
        #         element_w.click()
        #     else:print('No Alert Present!')
        # except:print('Element is None~')
        ######
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"分布图").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::div[@class='amap-locate']").click()  #定位map-locate
        # time.sleep(2)
        rollToSmallMap = "var q = document.documentElement.scrollTop=10000"
        driver.execute_script(rollToSmallMap)
        
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::img[2]")  #.click()  #click HuiZhou
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath(u"//*[@id='lmt2-display']//ul/li[2]/a/span/small").click()  #turn another tab
        time.sleep(5)
        scoll2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])/following::div[@class='amap-zoom-cursor']")  #定位第二个定位
        ActionChains(driver).drag_and_drop_by_offset(scoll2,0,70).perform()  #改进拖动滚动条
        ######
        # js = "var q = document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        time.sleep(5)  #five seconds must be waited!!
        #去成都看雪

        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::canvas[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::div[12]").click()  #step 1
        # time.sleep(5)
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::div[18]").click()  #step 2
        # #check this img
        # driver.implicitly_wait(10)
        # wait_img = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='(0)'])[1]/following::div[9]/div[last()-1]//img"))
        # wait_img.click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='分布图'])[2]/following::button[1]").click()  #check refresh_button
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='© 2018 AutoNavi'])[1]/following::div[12]").click()
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
