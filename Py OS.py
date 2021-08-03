#!/usr/bin/python
# -*- coding: UTF-8 -*-
#加载模块
import random
import time

#声明变量
global passwordpadd, password, passwordadd, power_on

#自定义函数
def power(inputpasswords):
    fo = open("password.txt","r+") 
    password = fo.read(4)
    print(password)
    strs = str(password)
    awa = len(strs)
    print(awa)
    if awa == 4:
        if inputpasswords == password:
            print(time.ctime()+" [ 控制台 ] "+'本次启动时长1秒')
    else:
        print(time.ctime()+" [ 控制台 ] "+'第一次启动，设置新用户')
        fo.write(inputpasswords)
        print(time.ctime()+" [ 控制台 ] "+"密码设置成功")

#开始进入Python的世界
print(time.ctime()+" [ 控制台 ] "+"Python OS Dev 0.0.2")
print(time.ctime()+" [ 控制台 ] "+"开机")
inputpassword = input(time.ctime()+" [ 控制台 ] "+"请输入4位数密码:")
inputpassword = str(inputpassword)
power(inputpassword)
