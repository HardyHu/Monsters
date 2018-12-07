# -*- coding: utf-8 -*-
'运营-换电柜，测试换电柜的禁用与最低电量设置'

__author__ = 'Hardy'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestGuiZi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "chrome://about/"  #最酷的URL
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Guizi(self):
        driver = self.driver
        driver.get("http://119.23.155.83:8090/")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18138819495")
        driver.find_element_by_id("mima").clear()
        driver.find_element_by_id("mima").send_keys("123456")
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("login-btn").click()
        driver.maximize_window()
        ######
        try:
            driver.find_element_by_xpath(u"//*[@id='modal_city'][@class='modal in']")
            element_w = driver.find_element_by_xpath(u"//*[@id='modal_city']/div/div/div[2]/button[text() = '深圳市']/../..//button")
            if element_w.is_displayed():
                element_w.click()
            else:print('No Alert Present!')
        except:print('Nothing happend.')
        ######
        driver.find_element_by_link_text(u"换电柜").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='»'])/../../li[last()-1]/a").click()
        time.sleep(2)
        ##判断点击前是否都是失连
        # check_status = driver.find_element_by_xpath()
        # for i in range(1,7):
        #     i = str(i)
        #     check_status = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='远程'])/../../../tbody/tr/td[last()-1]/span"+'['+ i +']')
        #     status_text = check_status.text
        #     print(status_text)
        #     if status_text == '远程控制':print('Element Exist!')
        #     else:
        #         print('Element error')   ###待优化
        #         return False

        driver.find_element_by_link_text(u"远程控制").click()
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        #在另一个窗口的
        now_windows = driver.current_window_handle
        all_windows = driver.window_handles

        for handle in all_windows:
            if handle != now_windows:
                driver.switch_to_window(handle)
                print('Now Page-Huandiangui')
                find_pic = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='正常'])[1]/preceding::div[1]")
                ActionChains(driver).move_to_element(find_pic).perform()
                img_here = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='正常'])[1]/preceding::div[1]/img[1]")
                img_src = img_here.get_attribute('src')
                print(img_src)
                if img_src != '':
                    pass
                else:
                    break
                # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='正常'])[1]/preceding::div[1]").click()  #need to capture the img_src,Actually,i wanna enough time to do it,however i donnot have.
                ##校验换电柜是否失连
                # GuiZi_status = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='3号舱'])/../div/i[1]"))
                # if GUiZi_status.is_displayed():
                #     continue
                # else:
                #     break
                ##
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='3号舱'])/../div/i[1]").click()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='启 用'])[1]/following::button[1]").click()  #禁用此舱
                # time.sleep(3)
                try:
                    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()   #由于confirm是两秒自动关闭，所以try
                except exception as e:print('button unvisible!')

                # driver.implicitly_wait(10)  #失误
                # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='最低允许外借电量'])/following::input[1]").click()  #is not clickable,so comment it
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='最低允许外借电量'])/following::input[1]").clear()
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='最低允许外借电量'])/following::input[1]").send_keys("30")
                driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='最低允许外借电量'])[1]/following::button[1]").click()
                time.sleep(2)
                driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
                driver.close()


        driver.switch_to_window(now_windows)  #切换回原窗口
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
