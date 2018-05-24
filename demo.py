#!/usr/bin/env python3
# -*- coding: utf-8 -*-python
from PIL import Image
from PIL import ImageChops

image_1 = Image.open("wechat_jump_game\\train_data\\091729.png")
image_2 = Image.open("wechat_jump_game\\train_data\\character.png")

'''diff = ImageChops.difference(image_1, image_2)

if diff.getbbox() is None:
    # 图片间没有任何不同则直接退出
    print("none")
else:
    diff.save("diff.bmp")
    '''

# 把图像对象转换为直方图数据，存在list h1、h2 中
# h1=im.histogram()
# h1=im.histogram()

# print(h1)
# print (im.format, im.size, im.mode)

import numpy as np
from numpy import *

a=arange(36)
b=a.reshape(6,6)
c=b[0,2:4]
print(c)