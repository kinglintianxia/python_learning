#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数
#函数别名
a=abs
print(a(-1))

#练习
print(hex(255))

#########自定义函数##########################
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-2))
#加入参数类型检查
def my_Abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
#print(my_Abs('A'))

#空函数
def nop():
	pass
	
import math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
r=move(100,100,60,math.pi/6)
print(r)

##########练习#######################################
def quadratic(a,b,c):
	det=b*b-4*a*c
	if (det<0):
		print('choose another a,c')
	else:
		x1=(-b+math.sqrt(det))/(2*a)
		x2=(-b-math.sqrt(det))/(2*a)
		return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))


#########函数的参数################################################
#位置参数
def power(x):
	return x*x
print ('5*5:',power(5))
# x^n次方
def power(x,n=2):
	s=1
	while n>0:
		n-=1
		s*=x
	return s
print('5^2:',power(5,2))
print('5^3:',power(5,3))
#默认参数
#def power(x,n=2):
print(power(5))

#可变参数
def calc(*num):	# *num
	sum=0
	for n in num:
		sum+=n*n
	return sum
print(calc(1,2,3))
print(calc())

nums=[1,2,3]
print(calc(*nums))

#关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
print(person('king',24))
print(person('king',24,love='kiss lin'))
print(person('king',24,love='kiss lin',job='nav'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('king',24,**extra))

#命名关键字参数
def person(name, age, **kw):
	if 'city' in kw:
		# 有city参数
		pass
	if 'job' in kw:
		# 有job参数
		pass
	print('name:', name, 'age:', age, 'other:', kw)
	
print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

#限制关键字参数的名字
def person(name,age,*,city,job):
	print(name,age,city,job)
print(person('Jack', 24, city='Beijing', job='Engineer'))
#带默认参数
def person(name,age,*,city='Beijing',job):
	print(name,age,city,job)
print(person('Jack',24,job='Engineer'))

#参数组合
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

#是通过一个tuple和dict，你也可以调用上述函数
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
#
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)