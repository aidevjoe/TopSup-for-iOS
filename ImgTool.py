# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 00:40
# @desc    : adb 获取截屏，截取图片


from PIL import Image
import os
import matplotlib.pyplot as plt

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

pull_screenshot()
image = Image.open("./screenshot.png")


# iPhone X
# 用 matplot 查看测试分辨率，切割问题和选项区域
question_im = image.crop((75, 350, 1067, 629)) # iPhone 7P

choices_im = image.crop((100, 630, 1050, 1250))

plt.subplot(221)
im = plt.imshow(image, animated=True)
plt.subplot(222)
im2 = plt.imshow(question_im, animated=True)
plt.subplot(212)
im3 = plt.imshow(choices_im, animated=True)
plt.show()