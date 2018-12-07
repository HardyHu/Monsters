# -*- coding: utf-8 -*-
'运营-绑定电池-解绑操作，及领取新电池及发送验证码操作'

__author__ = 'Hardy'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class BoundByElectric(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bound_by_electric(self):
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
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(u"绑定电池").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("search_form-input-user_phone").clear()
        driver.find_element_by_id("search_form-input-user_phone").send_keys("13636035190")
        driver.find_element_by_id("search_form-input-user_phone").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='解绑'])[1]").click()  #click 解绑
        driver.find_element_by_name("unbind_form-select-authphone").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Close'])").click()  #调戏并关闭弹窗
        driver.implicitly_wait(10)
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='您希望将哪颗电池绑定到该用户？'])[2]/input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='您希望将哪颗电池绑定到该用户？'])[2]/input").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='您希望将哪颗电池绑定到该用户？'])[2]/input").send_keys("xxx1111")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='绑定新电池'])[2]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_name("unbind_form-select-authphone").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=unbind_form-select-authphone | ]]
        Select(driver.find_element_by_name("unbind_form-select-authphone")).select_by_visible_text("Bill (17373112580)")
        # driver.find_element_by_name("unbind_form-select-authphone").click()
        driver.find_element_by_link_text(u"获取验证码").click()
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element_by_name("unbind_form-input-smscode").clear()
        driver.find_element_by_name("unbind_form-input-smscode").send_keys("888888")
        driver.find_element_by_id("auth_btn").click()
        driver.implicitly_wait(10)
        Authorization_Code = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='* 授权码不正确'])")  #授权码错误
        ActionChains(driver).double_click(Authorization_Code).perform()   #校验验证码错误
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='获取验证码'])[1]/following::p[3] | ]]
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='获取验证码'])[1]/following::p[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Okay！'])[1]/following::button[1]").click()
        driver.find_element_by_link_text("demi").click()
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
