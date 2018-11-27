#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####正则表达式#######

#re模块
import re
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
	print('ok')
else:
	print('failed')
	
###切分字符串####
#正常切分,无法识别连续的空格
print('a b  c'.split(' '))

#正则表达式
print(re.split(r'\s+','a b  c'))	#以\s+表示至少有一个空格
print(re.split(r'[\s\,]+','a,b c  d'))	#至少有一个空格或逗号
print(re.split(r'[\s\,\;]+','a,b;; c  d'))	#至少有一个空格或逗号

#####分组######
#用()表示的就是要提取的分组（Group）
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print('m.group(0):',m.group(0))
print('m.group(1):',m.group(1))
print('m.group(2):',m.group(2))

t='19:05:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print(m.groups())

#####贪婪匹配#######
print(re.match(r'^(\d+)(0*)$','1020300').groups())
#让\d+采用非贪婪匹配（也就是尽可能少匹配）
#加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$','1020300').groups())

######编译######
import re
# 编译:
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

#####练习########
#版本1
re_email1=re.compile(r'^([\w\.\-]+)@(\w+).(com+)$')
email1='someone@gmail.com'
email2='bill.gates@microsoft.com'
def Match(email):
	if re_email1.match(email):
		print('Match (%s) OK!' % email)
	else:
		print('Match (%s) Failed' % email)
Match(email1)
Match(email2)

#版本2
re_email2=re.compile(r'^([\w\.\-\s\<\>]+)@(\w+).([\w\.]+)$')
email3='<Tom Paris> tom@voyager.org'

def Match1(email):
	if re_email2.match(email):
		print('Match1 (%s) OK!' % email)
		print('name:',re.split(r'[\<\>]',email)[1])
	else:
		print('Match1 (%s) Failed' % email)
Match1(email3)