#!/usr/bin/env ptyhon3
# -*- coding: utf-8 -*-

#####面向对象的高级编程###############

#当我们定义了一个class，创建了一个class 的实例后，我
#们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
	pass

#给实例绑定一个属性：
stu=Student()
stu.name='King'
print(stu.name)

#尝试给实例绑定一个方法：
def set_age(self,age):
	self.age=age
	
from types import MethodType
stu.set_age=MethodType(set_age,stu)	#给实例绑定一个方法
stu.set_age(25)	# 调用实例方法
print(stu.age)	# 测试结果

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
	self.score=score
Student.set_score=MethodType(set_score,Student)

stu1=Student()
stu.set_score(100)
print(stu.score)

stu1.set_score(99)
#print(stu.score)	?99?
print(stu1.score)

######使用__slots__############
class Student1(object):
	__slots__=('name','age') #用tuple定义允许绑定的属性名称

s=Student1()
s.name='Jun'
s.age=25
print(s.name)
print(s.age)
#s.score=99	#'Student1' object has no attribute 'score'

#注意，__slots__定义的属性仅对当前类实例起作用，
#对继承的子类是不起作用的：
class GraduateStudent(Student1):
	pass
g=GraduateStudent()
g.score=100
print(g.score)

####使用@property############
class Student2(object):
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score=value

s=Student2()
s.set_score(60)
print(s.get_score())
#s.set_score(999)

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student3(object):
	@property	#把一个getter方法变成属性，只需要加上@property就可以了
	def score(self):
		return self._score
	#此时，@property本身又创建了另一个装饰器@score.setter，
	#负责把一个setter方法变成属性赋值，
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0~100!')
		self._score=value
		
s=Student3()
s.score=60
print('s.score:',s.score)

####练习#############
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be integer!')
		if value<0:
			raise ValueError('width must >0')
		self._width=value
	#
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height=value
	@property
	def resolution(self):
		return self._width*self._height
		
		
scr=Screen()
scr.width=1024
scr.height=768
print(scr.width)
print(scr.height)
print(scr.resolution)
assert scr.resolution == 786432, '1024 * 768 = %d ?' % scr.resolution


#####多重继承##############

class Animal(object):	#基类
	pass
class Runnable(object):
	def run(self):
		print('running!')
class Flyable(object):
	def fly(self):
		print('flying!')
class Mammal(Animal):	#哺乳类
	pass
class Bird(Animal):		#鸟类
	pass

#各种动物
class Dog(Mammal,Runnable):
	pass
class Bat(Mammal,Flyable):	#蝙蝠
	pass
class Parrot(Bird,Flyable):	#鹦鹉
	pass
class Ostrich(Bird,Runnable):	#鸵鸟
	pass

####定制类############
# __str__
#只需要定义好__str__()方法，返回一个好看的字符串
class Student4(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student4 object (name: %s)' %self.name
print(Student4('KING'))

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，
#就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fibo(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self		#实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>1000:
			raise StopIteration()
		return self.a	# 返回下一个值
#把Fib实例作用于for循环：
for n in Fibo():
	print(n)
	
#__getitem__
#像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
f=Fib()
print('f[0]:',f[0])
print('f[1]:',f[1])
print('f[2]:',f[2])

class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):	# n是索引
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):	# n是切片
			start=n.start
			stop=n.stop
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L
			
#试试Fib的切片：
f=Fib()
print(f[0:5])
print(f[:10])

#__getattr__
#就是写一个__getattr__()方法，动态返回一个属性
class Student(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self, attr):
		if attr=='score':
			return 99
s=Student()
print(s.name)
print(s.score)

#返回函数也是完全可以的：
class Student(object):
	def __getattr__(self, attr):
		if attr=='age':
			return lambda: 25
s=Student()
print(s.age())

#__call__
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
s=Student('KING')
s()

print(callable(Student('KING')))
print(callable(max))
print(callable('str'))

######使用枚举类##############################
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 
'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

from enum import Enum, unique
@unique
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

######使用元类##############################
from Hello import Hello
h=Hello()
h.hello()
print('type(Hello):',type(Hello))
print('type(h)',type(h))

#通过type()函数创建出Hello类，而无需通过class
def fn(self,name='world'):
	print('Hello,%s' % name)
Hello=type('Hello',(object,),dict(hello=fn)) #创建Hello class
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

####metaclass：元类############
#除了使用type()动态创建类以外，
#要控制类的创建行为，还可以使用metaclass。
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']=lambda self,value:	self.append(value)
		return type.__new__(cls,name,bases,attrs)
		
class Mylist(list,metaclass=ListMetaclass):
	pass
L=Mylist()
L.add(1)
print(L)