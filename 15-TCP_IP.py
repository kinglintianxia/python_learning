#！/usr/bin/env python3
# -*- coding: utf-8 -*-

###网络编程######

#TCP编程
#创建一个基于TCP 连接的Socket，
import socket
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立链接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
#接收数据：
buffer=[]
while True:
	#每次接收最多1K字节
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=b''.join(buffer)
#关闭链接
s.close()

#把HTTP 头打印出来，网页内容保存到文件：
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('sina.html','wb') as f:
	f.write(html)
	
	
####服务器编程#####
#编写一个简单的服务器程序，它接收客户端连接，把客户端发过
#来的字符串加上Hello 再发回去。
###见 echo_server.py echo_client.py


#####UDP编程#########
#UDP 则是面向无连接的协议。