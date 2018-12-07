# -*- coding: utf-8 -*-
'运营-用户，测试用户列表，表单及数据准确性'

__author__ = 'Hardy'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class CheckUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_user(self):
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
        driver.find_element_by_link_text(u"用户").click()
        # time.sleep(5)
        driver.implicitly_wait(10)
        # driver.find_element_by_link_text("150").click()  #列表会增加，所以会报错
        #判断不为空
        user_text = driver.find_element_by_xpath(u"//*[@id='operation-user']/div[1]/div[2]/div[1]").text
        user_num = user_text.split('：')[1]
        self.assertNotEqual(user_num,u"null")
        driver.find_element_by_link_text("2").click()
        driver.implicitly_wait(10)
        #等待固定内容
        wait_yimada = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宝安易马达2323'])"))

        driver.find_element_by_id("customer__search_footable").clear()
        driver.find_element_by_id("customer__search_footable").send_keys("13636035190")
        driver.find_element_by_id("search-form").submit()
        ActionChains(driver).double_click(driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='用户'])[3]/following::h5[1]")).perform()  #数据1
        check_onlyone = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='用户'])[3]/following::h5[1]").text
        check_onlyone = check_onlyone.split('：')[1]  #must be str
        self.assertEqual(check_onlyone,'1')
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='用户'])[3]/following::h5[1] | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='用户'])[3]/following::h5[1] | ]]
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='用户'])[3]/following::h5[1]").click()
        driver.find_element_by_link_text("NEW-HARDY").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(0)'])/following::li[3]//input").click()  #健壮定位
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='获取授权码'])").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='获取授权码'])/../../div/input").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='获取授权码'])/../../div/input").send_keys('12315')

        #check //*[@id="wrapper"]/div[2][contains(@style,'display: block;')] 异常弹窗
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='你想要把用户13636035190放在哪个群组里面？'])[1]/following::div[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='确定更换'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"//*[@id='wrapper']/div[2][contains(@style,'display: block;')]").click()
        time.sleep(2)

        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='确定更换'])/following::button").click()
        # driver.find_element_by_id("customer__search_footable").click()
        driver.implicitly_wait(10)

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
