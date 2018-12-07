#!/usr/bin/env python3
# -*- coding utf-8 -*-

#循环
names=['king','lin']
for name in names:
	print(name)

#计算1-10的整数之和
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum+=x
print(sum)
# range(5) = [0,5)
# range(5)生成的序列是从 0 开始小于 5 的整数
print(list(range(5)))

#1+2+...+100
sum=0
for x in range(101):
	sum+=x
print(sum)

#100以内奇数之和
sum=0
n=99
while n>0:
	sum+=n
	n-=2
print(sum)

#练习
list=['king','jun','lin']
for name in list:
	print('Hello:',name)
