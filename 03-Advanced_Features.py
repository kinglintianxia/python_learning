#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########高级特性#############################
#构造一个1, 3, 5, 7, ..., 99的列表
odd=[]	#list
n=1
while n<=99:
	odd.append(n)
	n+=2
print(odd)

######切片###############
print('######切片###############')
l=['king','kiss','lin','xiao','ni']
print('list=',l)
slice=l[0:3]
slice=l[:3]	#第一个索引是0，还可以省略：
print('l[0:3]',slice)
#倒切片
slice1=l[-2:]	#后两个
print('l[-2:]',slice1)
slice2=l[-2:-1]	#倒数第二个	
print('l[-2:-1]',slice2)
#倒序 ['ni', 'xiao']
print('l[::-1][:2]',l[::-1][:2])


##
L=list(range(100))
print('L=',L)
print('L[:10]',L[:10])
print('L[-10:]',L[-10:])
#前11-20个数：
print('L[10:20]',L[10:20])
#前10个数，每两个取一个：
print('L[:10:2]',L[:10:2])
#所有数，每5个取一个：
print('L[::5]',L[::5])

#tuple 切片
t=tuple(range(10))
print(t[:3])

print('ABCDEF'[:3])

######迭代###############
print('######迭代###############')
# dict就可以迭代
d={'a':1,'b':2,'c':3}
for key in d:	#迭代key
	print('key:',key)
for value in d.values():#迭代value
	print('value:',value)
for k,v in d.items():#迭代key&value
	print('k:%s,v:%d' %(k,v))
#字符串也是可迭代对象
for ch in 'ABC':
	print(ch)
#判断一个对象是可迭代对象通过collections模块的Iterable类型
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,v in enumerate(['A','B','C']):
	print(i,v)
for x, y in [(1,2),(3,4),(5,6)]:
	print(x,y)
	
######列表生成式 []########################
print('######列表生成式 []########################')
L=[x*x for x in range(1,11)]
print(L)
#for循环后面还可以加上if判断
L=[x*x for x in range(1,11) if x%2==0]
print(L)
#使用两层循环，可以生成全排列
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)
#把一个list中所有的字符串变成小写：
L=['Hello','WorlD','IBM','Apple']
print([s.lower() for s in L])

#####练习#################
L1=['Hello',24,'IBM','Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

########生成器generator ()###########################
print('########生成器generator ()##########')
g=(x*x for x in range(1,10))
for n in g:
	print(n)
	
#著名的斐波拉契数列（Fibonacci）
def fibo(num):
	n,a,b=0,0,1
	while n<num:
		print(b)
		a,b=b,a+b
		n+=1
	print('Done')
#生成器generator function
fibo(6)
def fibo_g(num):
	n,a,b=0,0,1
	while n<num:
		yield b
		a,b=b,a+b
		n+=1
	print('Done')
for n in fibo_g(6):
	print(n)

###练习：杨辉三角#############
def yanghui(num):
	L=[1]
	n=0
	while n<num:
		yield L
		L.append(0)		# L=[1,0]
		L=[L[i-1]+L[i] for i in range(len(L))]
		n+=1
for n in yanghui(10):
	print(n)

#########迭代器#########################################
print('#########迭代器#############')
#可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：
#可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

#生成器都是Iterator对象，
#但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))