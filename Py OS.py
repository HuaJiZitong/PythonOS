#!/usr/bin/python
# -*- coding: UTF-8 -*-
#加载模块
import random
import time

#声明变量
global passwordpadd, password, passwordadd, power_on

#自定义函数

#开始进入Python的世界
print(time.ctime()+" [ 控制台 ] "+"Python OS Dev 0.0.3")
print(time.ctime()+" [ 控制台 ] "+"开机")
inputpassword = input(time.ctime()+" [ 控制台 ] "+"请输入4位数密码:")
inputpassword = str(inputpassword)
power(inputpassword)
