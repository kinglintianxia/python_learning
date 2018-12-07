#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用dict和set

############ dict #################################
# 1. dict 全称 dictionary，在其他语言中也称为 map, 键-值（ key-value）
# 2. dict 可以用在需要高速查找的很多地方
# 3. 需要牢记的第一条就是 dict 的 key 必须是不可变对象
# 在 Python 中，字符串、整数等都是不可变的，因此，可以放心地作为 key。而 list 是可变的，就不能作为 key.
dict={'king':95,'lin':100,'Bob':85} # dict 内部存放的顺序和 key 放入的顺序是没有关系的。
print(dict)
print(dict['king'])
#修改
dict['king']=90
print(dict['king'])
#判断key是否存在
# in
print('king' in dict)
# get
print(dict.get('King'))
print(dict.get('King',-1))

#删除一个key
dict.pop('Bob')
print(dict)

############set####################################
# set 和 dict 的唯一区别仅在于没有存储对应的value
s=set([1,2,3])
print(s)
# add(key)
s.add(4)
print(s)
# remove(key)
s.remove(4)
print(s)

#两个set 交集、并集
s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

########### 再议不可变对象 ##############
# str 是不变对象，而 list 是可变对象。
# list
list = ['c', 'b', 'a']
print ("list.sort: ", list.sort())
# str
str1 = 'abc'
print ("origin str1: ", str1)
print ("str1.replace('a', 'A'): ", str1.replace('a', 'A'))
print ("now str1 = ", str1)
str2 = str1.replace('a', 'A')
print ("str2 = str1.replace('a', 'A'): ", str2)

#练习
key=(1,2,3)
d={key}
print(d)
key=(1,[2,3])
d={key}
print(d)

