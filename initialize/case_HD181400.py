# -*- coding: utf8 -*-
'运营-套餐管理，列表有数据，新建套餐，且可创建成功'

__author__ = 'Hardy'
# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class case181403TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_taocanNorepeatingCreate(self):
        ddriver = self.driver
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
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"套餐管理").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='套餐管理'])[2]/following::button[1]").click()  #点击创建套餐啊
        
        
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=login-btn | ]]
        seeds = '1234567890'
        random = []
        for i in range(4):
        	random.append(i)
        return random  #随机数，像这种小功能也可封装起来，以后直接调用
        random_use = "".join(random)  #转换成字符串，并新定义一个参数
        print(random_use)

        driver.find_element_by_name("name").clear()
        package_name = 'hardy_random' + random_use    
        print(package_name)
        driver.find_element_by_name("name").send_keys(package_name)  #传入随机值
          #不可重复使用
        driver.find_element_by_id("disabled_when_1_select").click()
        Select(driver.find_element_by_id("disabled_when_1_select")).select_by_visible_text(u"次卡套餐")
        driver.find_element_by_id("disabled_when_1_select").click()
        driver.find_element_by_id("disabled_when_1_select").click()
        driver.find_element_by_name("count").click()
        driver.find_element_by_name("count").clear()
        driver.find_element_by_name("count").send_keys("1")
        driver.find_element_by_name("price").click()
        driver.find_element_by_name("price").clear()
        driver.find_element_by_name("price").send_keys("")
        driver.find_element_by_name("count").click()
        driver.find_element_by_name("price").click()
        driver.find_element_by_name("price").clear()
        driver.find_element_by_name("price").send_keys("0.01")
        driver.find_element_by_name("limitTimes").click()
        driver.find_element_by_name("limitTimes").clear()
        driver.find_element_by_name("limitTimes").send_keys("")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='* 可拥有数量：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='* 有效天数：'])[1]/following::select[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='* 有效天数：'])[1]/following::select[1]").click()  #下拉选择，option
        driver.find_element_by_name("duration").click()
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("3")
        driver.find_element_by_name("remark").click()
        driver.find_element_by_name("remark").clear()

        mark = 'printPrint' + random_use
        driver.find_element_by_name("remark").send_keys(mark)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='提示：套餐名称超出长度'])[1]/following::button[1]").click()  #创建button
        time.sleep(2)
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
