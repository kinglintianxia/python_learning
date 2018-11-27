#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############常用内建模块####################
#(-1-)
#(-1-)####datetime-获取当前日期和时间
from datetime import datetime
now=datetime.now()
print('time:',now)
print('type(now):',type(now))

#获取指定日期和时间
from datetime import datetime
dt=datetime(2017,2,12,9,45,50)
print(dt)

#datetime 转换为timestamp
#时间戳(timestamp)是指格林威治时间1970年01月01日00时00分00秒
#(北京时间1970年01月01日08时00分00秒)起至现在的总秒数
from datetime import datetime
dt=datetime(2017,2,12,10,00,25)
print(dt.timestamp())

#timestamp 转换为datetime
from datetime import datetime
t=1486864825.0
print('本地时间:',datetime.fromtimestamp(t))	#本地时间
print('UTC时间',datetime.utcfromtimestamp(t))	#UTC时间

#str 转换为datetime
from datetime import datetime
cday=datetime.strptime('2017-02-12 10:00:25','%Y-%m-%d %H:%M:%S')
print('str 转换为datetime:',cday)

#datetime 转换为str
from datetime import datetime
now=datetime.now()
print('strftime:',now.strftime('%a,%b %d %H:%M'))

#datetime 加减
from datetime import datetime,timedelta
now=datetime.now()
print('now:',now)
print('now+timedelta(hours=10):',now+timedelta(hours=10))
print('now-timedelta(days=1):',now-timedelta(days=1))
print('now+timedelta(days=2, hours=12):',now+timedelta(days=2, hours=12))

#本地时间转换为UTC 时间
from datetime import datetime,timedelta,timezone
tz_utc_8=timezone(timedelta(hours=8))
now=datetime.now()
print('now:',now)
dt=now.replace(tzinfo=tz_utc_8)		#强制设置为UTC+8:00
print(dt)

#时区转换
# 拿到UTC 时间，并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt:',bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt:',tokyo_dt)


##练习##
import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
	dt_bj=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#	print(dt_bj)
	tz_num=int (re.match(r'UTC([+|-][0-9]{1,2}):00',tz_str).group(1))	#提取7
	print(tz_num)
#	print(type(tz))
	tz_utc=timezone(timedelta(hours=tz_num))
	dt=dt_bj.replace(tzinfo=tz_utc)
	print('timestamp:',dt.timestamp())
to_timestamp('2015-6-1 08:10:30','UTC+7:00')
to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')



###-2-
######collections###########
#collections 是Python 内建的一个集合模块，提供了许多有用的集合类。

#namedtuple
#namedtuple 是一个函数，它用来创建一个自定义的tuple 对象
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print('p.x:',p.x)
print('p.y:',p.y)

#deque
#deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.pop()
print(q)

#defaultdict
#使用dict 时，如果引用的Key 不存在，就会抛出KeyError。
#如果希望key 不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd=defaultdict(lambda: 'N/A')
dd['key1']='abc'
print('key1:',dd['key1'])
print('key2:',dd['key2'])

#OrderedDict
#使用dict 时，Key 是无序的。
#在对dict 做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d=dict([('a',1), ('b',2), ('c',3)])
print('dict:',d)
od=OrderedDict([('a',1),('b',2),('c',3)])
print('OrderedDict',od)

#OrderedDict 的Key 会按照插入的顺序排列，不是Key 本身排序
od=OrderedDict()
od['z']=1
od['y']=2
od['x']=3
print(od)
print(list(od.keys()))

#Counter
#Counter 是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'programming':
	c[ch]+=1
print(c)


###-3-
###base64-是一种用64个字符来表示任意二进制数据的方法
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

#由于标准的Base64 编码后可能出现字符+和/，在URL 中就不能直接作
#为参数，所以又有一种"url safe"的base64 编码，其实就是把字符+和/分
#别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

print('\n######base64练习#######')
###练习-请写一个能处理去掉=的base64 解码函数：
#Base64 编码的长度永远是4的倍数，因此，需要加上=把Base64 字符串
#的长度变为4 的倍数，就可以正常解码了
import base64
def safe_base64_decode(s):
	l=len(s)%4
	if l:
		s=s+b'='*(4-l)
	return base64.b64decode(s)

print(safe_base64_decode(b'YWJjZA=='))
print(safe_base64_decode(b'YWJjZA'))



###=4=
#struct
#Python提供了一个struct 模块来解决bytes和其他二进制数据类型的转换
import struct
#struct 的pack 函数把任意数据类型变成bytes：
#>表示字节顺序是big-endian，也就是网络序，I 表示4 字节无符号整数
print(struct.pack('>I',10240099))

#unpack 把bytes 变成相应的数据类型：
#据>IH 的说明:
#后面的bytes 依次变为I：4 字节无符号整数和 H：2字节无符号整数。
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))

#bmp 文件,文件头
s =b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH',s))


###-4-
###hashlib-hashlib 提供了常见的摘要算法，如MD5，SHA1 等等。
#摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函
#数，把任意长度的数据转换为一个长度固定的数据串（通常用16 进制
#的字符串表示）。
# MD5
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('MD5:',md5.hexdigest())

#SHA1
import hashlib
sha1=hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print('sha1:',sha1.hexdigest())

###练习
#(1)根据用户输入的口令，计算出存储在数据库中的MD5 口令：
import hashlib
def calc_md5(password):
	md5=hashlib.md5()
	md5.update((password+'king').encode('utf-8'))
	print('(%s) md5: %s' % (password,md5.hexdigest()))
	return md5.hexdigest()
calc_md5('123456')
calc_md5('888888')
calc_md5('password')

db={
	'king':'daf6a3aa3684e0bde3b928600b38bb35',
	'bob':'1521f87a935e069c8cf0750d747bf6ed',
	'lin':'78d2800db76f1e4b319d77b0fac89bef'
	}
	
def login(user,password):
	if db[user]==calc_md5(password):
		print('%s Login (%s) True' % (user,password))
	else:
		print('%s Login (%s) False' % (user,password))
login('king','123456')


###-5-
###itertools-非常有用的用于操作迭代对象的函数#######
import itertools
#count()会创建一个无限的迭代器
naturels=itertools.count(1)
for n in naturels:
	if n<=10:
		print('count() ',n)
	else:	#安全退出
		break
#cycle()会把传入的一个序列无限重复下去
cs=itertools.cycle('king')
n=0
for c in cs:
	n+=1
	if n<9:
		print('cycle() ',c)
	else:
		break
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可
#以限定重复次数：
ns=itertools.repeat('A',3)
for n in ns:
	print('repeat() ',n)
	
#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函
#数根据条件判断来截取出一个有限的序列：
nat=itertools.count(1)
ns=itertools.takewhile(lambda x: x<=10,nat)
print(list(ns))

###itertools 提供的几个迭代器操作函数更加有用：
#(1)
#chain()-可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC','XYZ'):
	print(c)
	
#(2)
#groupby()-把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby('AAABBCCAAA'):
	print(key,list(group))
#如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key,group in itertools.groupby('AAaaBbCc',lambda c:c.upper()):
	print(key,list(group))
	
	
###-6-
######XML###########
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print('sax:start_element: %s,attrs: %s' % (name,str(attrs)))
	def end_element(self,name):
		print('sax:end_element: %s' % name)
	def char_data(self,text):
		print('sax:char_data: %s' % text)
xml=r'''<?xml version="1.0"?>
<ol>
	<li><a href="/python">Python</a></li>
	<li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)

####练习#######



#####HTMLParser############
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
#parser.feed('''<html>
#<head></head>
#<body>
#<!-- test html parser -->
#    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
#</body></html>''')

#####urllib###############
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))
	
