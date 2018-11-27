#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########面向对象编程##############################
#面向对象编程——Object Oriented Programming，简称OOP

####面向过程########
std1={'name':'king','score':98}
std2={'name':'jun','score':91}

def print_score(std):
	print('%s: %s' %(std['name'],std['score']))
print_score(std1)
print_score(std2)


#####面向对象##########
class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s: %s' % (self.name,self.score))
		
king=student('king',98)
jun=student('jun',91)
king.print_score()
jun.print_score()


######访问限制##############
#在Python中，实例的变量名如果以__开头，就变成了一个
#私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	def __init__(self,name,score):
		self.__name=name	#private
		self.__score=score
	def print_score(self):
		print('%s: %s' % (self.__name,self.__score))
lin=Student('lin',98)
lin.print_score()
#仍然可以通过_Student__name来访问__name变量
print(lin._Student__name)

########继承和多态##################

class Animal(object):
	def run(self):
		print('Animal is running...')
class Dog(Animal):
	def run_dog(self):
		print('Dog is running...')
#子类，什么事也没干，就自动拥有了run()方法：
dog=Dog()
dog.run()
dog.run_dog()


####获取对象信息##########################
print(type(123))
print(type('king'))
print(type(abs))
print(type(abs)==type(123))

a=Animal()
d=Dog()
print(isinstance(d,Dog))
print(isinstance(d,Animal))

#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance(b'a', bytes))

#使用dir()
print(dir('ABC'))

#配合getattr()、setattr()以及hasattr()
#我们可以直接操作一个对象的状态：
class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x'))
print('obj.x=',obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print('hasattr: power',hasattr(obj,'power'))
print('getattr: power',getattr(obj,'power'))