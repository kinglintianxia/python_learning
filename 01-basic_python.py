#!/usr/bin/env python3
#-*- coding: utf-8 -*-

##########python 基础##############################
#print absolute value of an integer
a=100
if a>=0:
	print(a)
else:
	print(-a)
	
###########数据类型和变量#################################

#转义字符\
print('I\'m ok.')
print('I\'m learning-\nPython.')
print('\\\n\\')

# r表示内部字符串不转义
print('\\\t\\')
print(r'\\\t\\')	# 不转义

#Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

#布尔值
print('True:',True)
print('3>2:',3>2)
print('3>5:',3>5)

# and 与运算
print('True and True:',True and True)
print('True and Fase:',True and False)
# or 或运算
print('True or True:',True or True)
print('True or False:',True or False)
print('5>3 or 1>3:',5>3 or 1>3)
# not 非运算
print('not True:',not True)
print('not False:',not False)
print('not 1>2:',not 1>2)
# None
print ("None:", None)

#输入数字
age=int(input("Please input your age:"))
if age>=18:
	print('adult')
else:
	print('teenager')
	
#变量
a='ABC'
b=a
a='XYZ'
print('a:',a)	# 'XYZ'
print('b:',b)	# 'ABC'

#除法
print('9/3:',9/3)
# 地板除.整数的地板除//永远是整数，即使除不尽。
print('9//3:',9//3)
print('10%3:',10%3)

#练习
n=123
print(n)
f=456.789
print(f)
s1='Hello world'
print(s1)
s2='Hello,\'Adam\''
print(s2)
s3=r'Hello ,\\Bart'
print(s3)
s4=r'''Hello
Lisa!'''
print(s4)
