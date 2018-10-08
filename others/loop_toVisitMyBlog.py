# -*- coding: utf8 -*-
'Only used for personal actions'
__author__ = 'Hardy'
#Or you will need import others,import here
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# driver.implicitly_wait(30)

# n = 2
for i in range(3):
	i += 1
	driver.get("https://blog.csdn.net/qq_17195161/article/details/82665843")
	driver.maximize_window()
	yuedu = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[1]/span[2]'))
	yuedu.click()
	# driver.quit()  #quit进程未完全关闭导致 报错：目标计算机积极关闭
	#现在不关闭browser，改为循环处理窗口,,,,功能等同于 refresh()
	# try:
	# 	refresh()
	# 	tim.sleep(2)
	# except:
	# 	continue
	
	now_windows = driver.current_window_handle
	all_windows = driver.window_handles

	for handle in all_windows:
		if handle == now_windows:
			pass
		else:

			driver.switch_to_window(handle)
			driver.close()
	driver.switch_to_window(now_windows)
	print('打开新窗口的同时，旧窗口已经打开过： %s次' % i)
	time.sleep(10)
driver.quit()
print('We have reopened this page %s times,and now completed~' % i)
