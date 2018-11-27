#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list
L=list(range(100))
print('L=',L)

classmates=['king','lin','Bob']
print(classmates)
print(len(classmates))
print('classmates[0]:',classmates[0])
print('classmates[-1]:',classmates[-1])

#list是可变有序表
classmates.append('Anan')
print(classmates)
classmates.insert(1,'Kiss')
print(classmates)
#pop()删除list末尾的元素
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
#替换元素
classmates[1]='xiaoni'
print(classmates)
#list元素也可以是另一个list
list=['king',['kiss','xiao'],'ni']
print(list)
#tuple不可变列表
t=('king','kiss','lin')
print(t)
t1=(1,)
print(t1)
#来看一个“可变的”tuple：
t2=('a','b',['A','B'])
print(t2)
t2[2][0]='X'
t2[2][1]='Y'
print(t2)

#练习
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print('Apple:',L[0][0])
print('Python:',L[1][1])
print('Lisa:',L[2][2])