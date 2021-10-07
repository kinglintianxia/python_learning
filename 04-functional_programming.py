#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数式编程

##### 高阶函数Higher-order function #######
def add(x,y,f):	# 传入函数
	print(f(x)+f(y))
add(-5,6,abs)

########map/reduce########################
#map()
def f(x):
	return x*x
L1=[1,2,3,4,5,6,7,8,9]
r=map(f,L1)
print(list(r))
L2=map(str,L1)
print(list(L2))
#reduce()
#序列求和
from functools import reduce
def add(x,y):
	return x+y
	
a=reduce(add,[1,3,5,7,9])
print(a)

#如果要把序列[1, 3, 5, 7, 9]变换成整数13579,reduce就可以派上用场：
def fn(x,y):
	return x*10+y
b=reduce(fn,[1,3,5,7,9])
print(b)

#str2int
from functools import reduce 
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
		'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]	#dict取值
	return reduce(fn,map(char2num,s))
print(str2int('13579'))

#####练习########
#1
#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
	return name.upper()[0]+name.lower()[1:]
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#2
#接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
	def power(x,y):
		return x*y
	return reduce(power,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#3
#利用map和reduce编写一个str2float函数，
#把字符串'123.456'转换成浮点数123.456：
from functools import reduce 
def str2float(s):
	def f1(x,y):
		return x*10+y
	def f2(x,y):
		return x/10+y
	def ctoi(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
		'5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':0}[c]
	#s[::-1][:s.find('.')+1] 倒序切片
	return reduce(f1,map(ctoi,s[:s.find('.')]))+reduce(f2,map(ctoi,s[::-1][:s.find('.')+1]))
print('str2float(\'123.456\') =', str2float('123.456'))


######filter####################
#，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。

#在一个list中，删掉偶数，只保留奇数
def is_odd(num):
	return num%2
L=list(filter(is_odd,[1,2,4,5,6,9,10,15]))
print(L)

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

##########用filter 求素数#######
#先构造一个从3开始的奇数序列：
def odd_iter():
	n=1
	while True:
		n+=2
		yield n

#定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	it=odd_iter()	#初始序列
	while True:
		n=next(it)	# 返回序列的第一个数 
		yield n
		it=filter(lambda x,m=n: x%m>0,it) # 构造新序列
		
for n in primes():
	if n<100:
		print(n)
	else:
		break
		
######练习##############
#利用filter()滤掉非回数：
print('#利用filter()滤掉非回数:')
def is_palindrome(n):
	s=str(n)
	return s==s[::-1]
output = filter(is_palindrome, range(1, 100))
print(list(output))

####sorted 排序算法#######################
L=sorted([36,5,-12,9,-21])
print(L)
#sorted()函数也是一个高阶函数，它还可以接收一个key函数
print(sorted([36,5,-12,9,-21],key=abs))
#再看一个字符串排序的例子：
L=sorted(['bob', 'about', 'Zoo', 'Credit'])
print(L)
#实现忽略大小写的排序：
L=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(L)
#行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
L=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print(L)

#######练习#################
#按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower()	#取'bob'
L2 = sorted(L, key=by_name)
print(L2)

#按成绩排序
def by_score(t):
	return t[1]	#取 75
#print(by_score(('Bob', 75)))
L2 = sorted(L, key=by_score)
print(L2)

#########返回函数###################################
#函数作为返回值
def lazy_sum(*args):
	def sum():
		s=0
		for n in args:
			s+=n
		return s
	return sum
f=lazy_sum(1, 3, 5, 7, 9)
print(f())

#####匿名函数lambda x: x * x#####################
L=list(map(lambda x: x*x,[1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)
f=lambda x: x*x
print(f)
print(f(5))

#########装饰器######################################
def now():
	print('2017.1.13')
f=now
f()
print(now.__name__)
print(f.__name__)

#这种在代码运行期间动态增加功能的方式，
#称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2017.1.13')
now()

#要自定义log的文本：
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2017.1.13')
now()
print(now.__name__)

##一个完整的decorator的写法
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
#者针对带参数的decorator：
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
########练习###########
#调用的前后打印出'begin call'和'end call'
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call %s():' % func.__name__)
		def ret(*args, **kw):
			return func(*args, **kw)
		print('end call %s:' % func.__name__)
	return wrapper
@log
def now():
	print('2017.1.13')
now()

###########偏函数###########################
#int()函数还提供额外的base参数，默认值为10。
#如果传入base参数，就可以做N进制的转换：
def int2(x,base=2):
	return int(x,base)
print(int2('1000000'))

#functools.partial就是帮助我们创建一个偏函数的，
#不需要我们自己定义int2()
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))
#但也可以在函数调用时传入其他值：
print(int2('1000000',base=10))