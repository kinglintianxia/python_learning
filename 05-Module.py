#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#表示模块的文档注释，
#任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'

__author__='King'	#使用__author__变量把作者写进去

import sys

def test():
	#sys模块有一个argv变量，用list存储了命令行的所有参数
	args=sys.argv
	if len(args)==1:
		print('Hello world!')
	elif len(args)==2:
		print('Hello,%s!' % args[1])
	else:
		print('Too many arguments!')
	
if __name__=='__main__':
	test()
	
#有了Pillow，处理图片易如反掌。随便找个图片生成缩略图
from PIL import Image
im=Image.open('1.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')