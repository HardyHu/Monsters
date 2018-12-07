# -*- coding: utf-8 -*-
'代码文件测试:测试第二行固定用例报告输出，且文本不会出错'

__author__ = 'Hardy'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#########coding begin here