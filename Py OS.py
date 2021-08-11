#!/usr/bin/python
# -*- coding: UTF-8 -*-
#加载自定义模块 module
import module

#Welcome to PyOS world
module.out("Python OS Dev 0.0.5")
module.out("开机")
module.out("请输入密码")
inputpassword = input()
module.login(inputpassword)
