# -*- coding: utf8 -*-
"""
os遍历目录，输出每个代码文件的注释内容
"""
__author__ = 'Hardy'

from initialize import *
import os,time,re,json
import xlwt

testdoc = """There was a young lady named Bright,\
      whose speed was far faster than light;\
      She started one day \
      In a relative way,\
      And returned on the previous night."""

size = len(testdoc)
print(size)

# fout = open('newfile','wt')
# fout.write(testdoc)
# fout.close()

# fout = open('newfile','wt')
# print(testdoc,file=fout,sep='',end='')  #171
# offset = 0
# chunk = 100
# while True:
# 	if offset > size:
# 		break
# 	fout.write(testdoc[offset : offset+chunk])
# 	offset+=chunk
# fout.close()

# try:
# 	fout = open('funclist','xt')
# 	fout.write('stomp stomp stomp')
# except FileExistsError:
# 	print('relativity already exists!That was a close one.')  #已存在异常处理，存在则不会写入数据

filelist = os.listdir('d:/SoftALL/StorageCloneHere/initialize')
# print(filelist)

# print(filelist[:-4])  #过滤后的目录数据结果
filelist = filelist[:-4]
d = {}
# casefilehere = 'D:/SoftALL/StorageCloneHere/initialize/case_HD181400.py'  #case*.py 用例or用例路径

# # result = re.match()
# fopen = open(casefilehere,'rb')
# lines = fopen.readlines()

# print(lines[1].decode('utf-8'))
# for line in lines:
# 	print(line)
print(len(filelist))
if len(filelist) == 0:
	print('error')

for file in filelist:
	casefilehere = 'D:/SoftALL/StorageCloneHere/initialize/' + file
	# print(casefilehere)
	try:
		fopen = open(casefilehere,'rb')
		# if not fopen:
		# 	break
		# else:
		# 	continue
		lines = fopen.readlines()
		# print(lines)
		result = []
		for line in lines:
			line = line.strip()
			# if not line or line.startswith('#'):  
			# 	continue
			result.append(line)
		# result.sort()    #不是数字和明确的字母，不要用sort排序。。。坑
		# print(result)

		value = result[1].decode('utf-8')
		d.setdefault(file,value)
		fopen.close()
	except FileExistsError:
		print('file exists error!')

	# casefilehere = 'D:/SoftALL/StorageCloneHere/initialize/case_HD181400.py'
	# fopen = open(casefilehere,'rb')
	# lines = fopen.readlines()
	# value = lines[1].decode('utf-8')
	# d.setdefault(file,value)
	
	# fopen.close()

print('d =',d)  #数据都存在于字典里，接下来就是导出

#xlwt的使用
#
#
#style格式
def set_style(name, height,color, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.name = name
    # 是否为粗体
    font.bold = bold
    # 设置字体颜色
    font.colour_index = color
    # 字体大小
    font.height = height
    # 字体是否斜体
    font.italic = False
    # 字体下划,当值为11时。填充颜色就是蓝色
    font.underline = 0
    # 字体中是否有横线struck_out
    font.struck_out =False  #字中间横线
    # 定义格式
    style.font = font

    return style


#处理字典数据
# 参考 sheet1.write('行号','列号','值')
#记住一定要关闭该文件
def dicttoExcel(d):
	workbook = xlwt.Workbook('D:/自动化功能.xlsx')  #创建xlsx文件，会覆盖
	sheet1 = workbook.add_sheet(u'完成功能V1.0.3')  #创建新表单，默认名：sheet1
	ll = list(d.keys())
	for i in range(len(ll)):
		sheet1.write(i+2,1,ll[i])  #在该列持续加行
		value = list(d.values())
		sheet1.write(i+2,2,value[i])
	#注意第一行，set_style(字体，大小（x*20)，颜色，加粗（默认False））
	x = '自动化程序名'
	y = '实现内容'
	z = '备注'
	lname = '自动化功能.xlsx'
	sheet1.write(1,1,x,set_style('微软雅黑',280,0x40,True))  #0x40表示黑色
	sheet1.write(1,2,y,set_style('微软雅黑',280,0x40,True))
	sheet1.write(1,3,z,set_style('微软雅黑',280,0x40,True))

	# for j in range(0,len(d)):
	# 	m = 0
	# 	ls = list(d[j].values)
	# 	for k in ls:
	# 		sheet1.write(j+1,m,k)
	# 		m += 1
	print(' ')
	workbook.save('D:/自动化功能.xlsx')
	print('功能清单%s输出完成！'% lname)

if __name__ == '__main__':
	d = d
	dicttoExcel(d)







