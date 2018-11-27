#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#####多进程########
#windows
from multiprocessing import Process
import os
def run_proc(name):
	print('run Child process %s (%s)...' % (name,os.getpid()))

#if __name__=='__main__':
#	print('Parent process %s.' % os.getpid())
#	p=Process(target=run_proc,args=('test',))
#	print('Child process will start...')
#	p.start()
#	p.join()	#join()方法可以等待子进程结束后再继续往下运行
#	print('Child process end')
	
####Pool进程池##########
#print('####Pool进程池#######')
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print('Task %s runs %0.2f seconds.' % (name,(end-start)))
	
#if __name__=='__main__':
#	print('Parent process %s.' % os.getpid())
#	p=Pool(4)
#	for i in range(5):
#		p.apply_async(long_time_task,args=(i,))
#	print('Waiting for all subprocesses done...')
#	p.close()
#	p.join()
#	print('All sunbprocess done.')
	
#####子进程####
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

#子进程还需要输入，则可以通过communicate()方法输入
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#####进程间通讯##########
from multiprocessing import Process,Queue
import os,time,random

#写数据进程
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
#读数据进程
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.' % value)
#if __name__=='__main__':
	# 父进程创建Queue，并传给各个子进程：
#	q=Queue()
#	pw=Process(target=write,args=(q,))
#	pr=Process(target=read,args=(q,))
	# 启动子进程pw，写入:
#	pw.start()
	# 启动子进程pr，读取:
#	pr.start()
	# 等待pw 结束:
#	pw.join()
	# pr 进程里是死循环，无法等待其结束，只能强行终止:
#	pr.terminate()
	
####多线程###
print('\n####多线程###')
import time,threading
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n=0
	while n<5:
		n+=1
		print('thread %s >>>%s' % (threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)	
t=threading.Thread(target=loop,name='loopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

######Lock#######
print('\n######Lock#######')
import time,threading
balance=0

lock=threading.Lock()	#创建一个锁

def change_it(n):
	global balance
	balance+=n
	balance-=n
	
def run_thread(n):
	for i in range(100000):
		#先要获取锁
		lock.acquire()
		try:
			# 放心地改吧:
			change_it(n)
		finally:
			# 改完了一定要释放锁:
			lock.release()
			
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

########ThreadLocal###############
import threading
#创建全局ThreadLocal对象
local_school=threading.local()

def process_student():
	#获取当前线程关联的student
	std=local_school.student	#name
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))
	
def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student=name
	process_student()
	
t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread_A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()