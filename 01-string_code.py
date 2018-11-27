#!/usr/bin/env python3
# -*- coding utf-8 -*-

#字符串和编码
print('包含中文的str')
#ord()获取字符的整数表示
print(ord('A'))
print(ord('中'))
#chr()把编码转换为对应的字符
print(chr(66))
print(chr(25991))
#十六进制写str
print('\u4e2d\u6587')

#encode()可以编码为指定的bytes
print('encode()可以编码为指定的bytes:')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#decode()把bytes变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#len()计算字符长度
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

#格式化输出
print('heoll,%s' %'world')
print('Hi,%s,you have $%d.' %('King',1000000))
#格式长度控制
print('%2d-%02d' %(3,1))
print('%0.2f' %3.1415926)
print('Age:  %s. Gender: %s' %(25,True))
print('Growth rate:%d %%' %7)

#练习
print('Growth rate:%2.1f %%' % ((85-72)/72))