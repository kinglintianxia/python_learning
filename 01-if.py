#!/usr/bin/env python3
# -*- coding utf-8 -*-

############# 条件判断 #############  
age=3
if age>=18:
	print('Your age is:',age)
	print('Adult')
else:
	print('your age is:',age)
	print('Teenager')

#elif
age=3
if age>=18:
	print('Adult')
elif age>=6:
	print('teenager')
else:
	print('kid')
# if 判断条件还可以简写
x = 0
# 只要 x 是非零数值、非空字符串、非空 list 等，就判断为 True
if x:	
	print ('True')

#输入整数
age=int(input('enter your age:'))
if age>=18:
	print('Adult')
elif age>=6:
	print('teenager')
else:
	print('kid')
	
#练习
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi>32:
	print('very Fat!')
elif bmi>28:
	print('Fat')
elif bmi>18.5:
	print('health!')
else:
	print('thin!')
	