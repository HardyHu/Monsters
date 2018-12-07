# -*- coding: utf-8 -*-
'运营-业务统计，里选择日期，并有对应数据'

__author__ = 'Hardy'
##Python3.7.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Business(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_business(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("phone").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=phone | ]]
        driver.find_element_by_id("login-btn").click()
        # time.sleep(2)
        # Abnormal_popup = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']"))  #校验class属性
        ####
        # if self.element_exist("//*[@id='modal_city'][@class='modal in']"):  #处理异常弹窗
        #     Abnormal_popup = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']"))
        #     if Abnormal_popup.is_displayed():
        #         Abnormal_popup.click()
        #         click_times += 1
        #         print('Element Exist!')

        ####
        try:
            driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']")  #定位弹窗已经block的class属性
            driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button").click()  #存在弹窗就关闭窗口
        except NoSuchElementException:pass
        finally:print('继续后续操作')
        # if Abnormal_popup != '':
        #     print('遇到弹窗！')
        #     driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button").click()  #注意外双引内单引
        # else:
        #     print("Nothing goes bad!")
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='业务统计'])").click()
        time.sleep(5)
        WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置'])[2]/following::input[1]"))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置'])[2]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='日'])[1]/following::tr[1]/td[1]").click()  #选择行第一列第一的日期，以免出错
        time.sleep(3)  #点击后等待
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='单柜用户数'])[4]/following::td[1]").click()  #确认表单KA字段
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='单柜用户数'])[4]/following::td[1] | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='单柜用户数'])[3]/following::td[1]").click()  #确认表单南方字段
        
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='单柜用户数'])[3]/following::td[1] | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='|'])[1]/following::img[1]").click()
        driver.find_element_by_id("logout").click()  #退出登录
    
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
