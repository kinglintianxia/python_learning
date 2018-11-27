#!/usr/bin/env python3
#-*- coding: utf-8 -*-
try:
	print('try...')
	r=10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')

#可以有多个except来捕获不同类型的错误：
try:
	print('try...')
	r=10/int('a')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error.')
finally:
	print('finally...')
print('END')

#记录错误
#Python内置的logging模块可以非常容易地记录错误信息：
# err_logging.py
import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('2')
	except Exception as e:
		logging.exception(e)
main()
print('END')

#####调试##################
#断言
print('#####断言####')
def foo(s):
	n=int(s)
	assert n!=0, 'n is zero!'
	return 10/n
def main():
	foo(0)
#main()

print('###logging###')
#logging
import logging
logging.basicConfig(level=logging.INFO)
s='1'
n=int(s)
logging.info('n=%d' % n)
print(10/n)

print('###pdb###')
#pdb
s='1'
n=int(s)
print(10/n)

#pdb.set_trace()
import pdb
s=0
pdb.set_trace()	#断点
print(10/s)
