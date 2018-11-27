#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
	f=open('/Users/King/Documents/python练习/mydict.py','r')
	print(f.read())
finally:
	if f:
		f.close()

#引入了with 语句来自动帮我们调用close()方法：
with open('/Users/King/Documents/python练习/mydict.py','r') as f:
	print(f.read())
	
f=open('/Users/King/Documents/python练习/mydict.py','r')
for line in f.readlines():
	print(line.strip())

#二进制文件
f=open('/Users/King/Pictures/Saved Pictures/1.jpg','rb')
print(f.read())

#写文件
f=open('/Users/King/Documents/python练习/test.txt','w')
f.write('Hello,Python!')
f.close()
#所以，还是用with语句来得保险：
with open('/Users/King/Documents/python练习/test.txt','w') as f:
	f.write('Hello,Python3!')

	
####StringIO#########
print('####StringIO#########')
from io import StringIO
f=StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())

####ByteIO#########
print('####ByteIO#########')
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

######操作文件和目录#############
import os
print(os.name)
print(os.environ)
print('PATH:',os.environ.get('PATH'))
print('绝对路径:',os.path.abspath('.'))
os.path.join('/Users/King/Documents/python练习','testdir')
#os.mkdir('/Users/King/Documents/python练习/testdir')
#os.rmdir('/Users/King/Documents/python练习/testdir')
print(os.path.split('/Users/king/testdir'))
print(os.path.splitext('/path/test.txt'))

#对文件重命名:
#os.rename('test.txt','test.py')
# 删掉文件:
#os.remove('test.py')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

#######练习##########
#1.利用os 模块编写一个能实现dir -l 输出的程序。

#2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找
#  文件名中包含指定字符串的文件，并打印出相对路径。
def findFile(test):
	for dirpath,dirnames,filenames in os.walk('.'):
		for f in filenames:
			x=os.path.splitext(f)[1]
			if x==test:
				print(os.path.join(dirpath,f))

if __name__=='__main__':
	findFile('.py')
	
	
###########序列化###############
import pickle
d=dict(name='king',age=20,score=99)
print(pickle.dumps(d))
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
#反序列化
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)

#####JSON##########
import json
d=dict(name='king',age=25,score=88)
print(json.dumps(d))

#
json_str='{"age":20,"score":88,"name":"king"}'	#json字符串
print(json.loads(json_str))

#####JSON进阶
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.score=score
		self.age=age
		
def student2dict(std):
		return {
			'name':std.name,
			'age':std.age,
			'score':std.score
		}
		
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
	
s=Student('king',25,88)
print(json.dumps(s,default=student2dict))

print(json.loads(json_str,object_hook=dict2student))