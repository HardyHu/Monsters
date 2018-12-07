# -*- coding: utf-8 -*-
'代理商-大额提交：提交涉及到的文本输入、字符判断、错误提示、文件操作、表单记录等功能'

__author__ = 'Hardy'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestBigAmount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_big_amount(self):
        driver = self.driver
        #代理商后台
        driver.get("http://119.23.155.83:83/?nsukey=saNgAVOmUN4kqIsyyCTT%2FGVFrkl%2Bc3Nyy8iFyeoFSg87d5NfBnRW%2FdYCELXxuCNQJJQQMCexYwfCtJ%2BaFhagLFgqz3PuOCT06pHF%2BmKU3xg2Hy2f3HFnVbKlco%2B3dIjoQKecWd%2F%2BYPZgRNF%2FtQJZr%2FZgp2djNGJp7OnzDqGoqgt2FWC23CDwrt944QyBiaUjXiYXTit7drVeoDouaRUDQg%3D%3D#/group")
        driver.find_element_by_xpath(u"//*[@id='app']//input[1][@type='text']").clear()
        driver.find_element_by_xpath(u"//*[@id='app']//input[1][@type='text']").send_keys("18138819495")
        driver.find_element_by_xpath("//*[@id='app']//input[1][@type='password']").clear()
        driver.find_element_by_xpath("//*[@id='app']//input[1][@type='password']").send_keys("111111")
        driver.find_element_by_id("btn_login").click()
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
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='大额充值'])").click()  #点击进入大额充值
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='城市：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='成都市'])").click()   #选择成都市

        seeds = '1234567890'
        random = []
        for i in range(3):
        	random.append(i)
        return random  #随机数，像这种小功能也可封装起来，以后直接调用
        random_use = "".join(random)  #转换成字符串，并新定义一个参数
        print(random_use)
        text = '城市名称'
        input_CityName = text + random_use
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='代理商公司名称:'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='代理商公司名称:'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='代理商公司名称:'])[1]/following::input[1]").send_keys(input_CityName)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='实际付款人名称：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='实际付款人名称：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='实际付款人名称：'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='实际付款人名称：'])[1]/following::input[1]").send_keys(u"李小白")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='支付金额(元)：'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='支付金额(元)：'])[1]/following::input[1]").send_keys("1.5")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数量：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数量：'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='数量：'])[1]/following::input[1]").send_keys("150")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='申请记录'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='付款凭单：'])[1]/following::button[1]").click()
        driver.find_element_by_name("file").clear()
        driver.find_element_by_name("file").send_keys("")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查看范例'])[1]/following::button[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='查看范例'])[1]/following::button[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='提示'])[1]/following::button[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1] | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='充值电池押金'])[1]/following::div[1]").click()

        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='代理商后台'])[2]/following::i[1]").click()
        driver.find_element_by_link_text(u"退出").click()
    
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
