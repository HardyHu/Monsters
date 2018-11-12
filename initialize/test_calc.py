# -*- coding: utf8 -*-

import unittest
class TestclsforNewsuite(unittest.TestCase):
	def setUp(self):
		self.a = 7
		self.b = 7

	def tearDown(self):
		print('ALL test over!')

	def calc(a,b,self):
		print('a * b = ',self.a * self.b)

# def calc(a,b):
# 	print("a * b = ",a*b)

	# calc(a,b)