#!/usr/bin/env python3
# -*- coding utf-8 -*-
# coding: utf-8

# 在计算机内存中，统一使用 Unicode 编码，
# 当需要保存到硬盘或者需要传输的时候，就转换为 UTF-8 编码

############## 字符串和编码 ###############
print('包含中文的str')

########### ord()获取字符的整数表示 ############
print(ord('A'))
print(ord('中'))

########### chr()把编码转换为对应的字符 ########
print(chr(66))
print(chr(25991))

#十六进制写str
# 字符的整数编码
print('\u4e2d\u6587')

#encode()可以编码为指定的bytes
print('encode()可以编码为指定的bytes:')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#decode()把bytes变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

############### len()计算字符长度 ###############
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

############### 格式化输出 ###############
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('heoll,%s' %'world')
print('Hi,%s,you have $%d.' %('King',1000000))

#格式长度控制
print('%2d-%02d' %(3,1))
print('%0.2f' %3.1415926)
print('Age:  %s. Gender: %s' %(25,True))
print('Growth rate: %d%%' %7)

#练习
print('Growth rate:%2.1f%%' % ((85-72)/72))