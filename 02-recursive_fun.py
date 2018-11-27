#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######递归函数###############################
#求 n!
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(1))
print(fact(5))
print(fact(100))

##尾递归
def fact_iter(num,product=1):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
	
print('5!=',fact_iter(5))
#print('1000!=',fact(1000))

#练习:汉诺塔的移动
def move(n, a, b, c):
    if n == 1:	#n=1,一步成功，返回
        print('move', a, '-->', c)
        return
	#其他情况 n>=2
    move(n-1, a, c, b)	#先把顶上n-1个从a借助c挪到b
    print('move', a, '-->', c) #再把最大的盘从a挪到c
    move(n-1, b, a, c)	#最后把顶上n-1个从b借助a挪到c

move(4, 'A', 'B', 'C')

