# -*- coding: utf8 -*-
'导入对应测试用例，执行测试，并输出报告'
__author__ = 'Hardy'

import unittest
from unittest import TestSuite
from HTMLTestRunner import HTMLTestRunner
import discover,os,time
from initialize import test_calc  #doc-file

# now = time.strftime("%Y-%m-%H_%M_%S",time.localtime(time.time()))
# report_path = 'D:/SoftALL/StorageCloneHere/report/' + now + 'report.html'
# print(report_path)
'''测试建立导入方法(使用TestSuite)'''
# all_case=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
# suite=unittest.TestSuie()
# suite.addTests(all_case)
# --------------------- 

#用例路径
# case_path=os.path.split(os.path.realpath(__file__))[0]



#打开一个report文件，以便将测试结果写入其中
if __name__ == '__main__':
	case_path = os.getcwd()
	all_case = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)  #pattern暂时使用test*，等调试完成切换成case*
	suite=unittest.TestSuite()
	suite.addTests(all_case)

	now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
	reportPath = 'D:/SoftALL/StorageCloneHere/report/' + now + 'report.html'

	with open(reportPath,'wb') as f:
		runner=HTMLTestRunner(stream=f,
			title='Test Result',
			description=u'result here:',
			verbosity=2)   #must be 2 to view full result
		runner.run(suite)
		f.close()
# --------------------- 

# def test_writepreviw(self):
# 	print('This is a test.')

# 	'''测试执行测试
# 	'''

# 	'''测试输出完整报告，并包含图片结果
# 	'''

# def all_cases():
# 	case_path = os.getcwd()

# 	discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)  #pattern暂时使用test*，等调试完成切换成case*
# 	return discover

# 	# def test_inputCases():
# 	# 	print(os.listdir(os.getcwd()))

# def run():
# 	now = time.strftime("%Y-%m-%H_%M_%S",time.localtime(time.time()))
# 	report_path = 'D:/SoftALL/StorageCloneHere/report/' + now + 'report.html'
# 	with open(report_path,'wb') as f:
# 		runner = HTMLTestRunner(stream=f,title='interface report',description="result:")  #,verbosity=2
# 		runner.run(all_cases())
# 	f.close()


# if __name__ == '__main__':
# 	runner..
#   runner.run