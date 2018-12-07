#!/usr/bin/env python3	# 第一行注释是为了告诉 Linux/OS X 系统，这是一个 Python 可执行程序，Windows 系统会忽略这个注释.
## -*- coding: utf-8 -*- # 第二行注释是为了告诉 Python 解释器，按照 UTF-8 编码读取源代码，
# 申明了 UTF-8 编码并不意味着你的.py 文件就是 UTF-8 编码的，必须并且要确保文本编辑器正在使用 UTF-8 without BOM 编码.
# coding: utf-8	

#########输出:print()##################################
#打印字符串
print('hello_world')

#打印多个字符串
print('The quick brown fox,','jumps over,','the lazy dog')

#打印整数/计算结果
print(300)
print(100+200)
print('100+200=',100+200)

##########输入:input()##################################
name=input('Please input your name:')
print('hello',name)

#练习
print('1024*768=',1024*768)
