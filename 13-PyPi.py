#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#常用第三方模块

###PIL：Python Imaging Library，###################
#已经是Python 平台事实上的图像处理标准库了。

#图像缩放操作
from PIL import Image
# 打开一个jpg 图像文件
img=Image.open('1.png')	
# 获得图像尺寸:
width,height=img.size
print('Original image size: %sx%s' % (width,height))
# 缩放到50%:
img.thumbnail((width//2,height//2))
print('Resize image to: %sx%s' % (width//2,height//2))
# 把缩放后的图像用jpeg 格式保存:
img.save('thumbnail.jpg','jpeg')

#模糊效果
from PIL import Image,ImageFilter
img1=Image.open('1.png')
img2=img1.filter(ImageFilter.BLUR)
img2.save('blur.jpg','jpeg')

#生成字母验证码图片：
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def rndChar():
	return chr(random.randint(65,90))
#随机颜色1：
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2：
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
	
#240x60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建Font对象
font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')


#########virtualenv###################################
#virtualenv 就是用来为一个应用创建一套“隔离”的Python 运行环境。
