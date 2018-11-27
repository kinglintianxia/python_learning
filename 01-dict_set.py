#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#使用dict和set
############dict#################################
dict={'king':95,'lin':100,'Bob':85}
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

#练习
key=(1,2,3)
d={key}
print(d)
key=(1,[2,3])
d={key}
print(d)

