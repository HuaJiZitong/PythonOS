import time
import webbrowser

from easygui import *

import module


#声明变量
#global passwordpadd, password, passwordadd, power_on

#系统项模块
def out(message):
   print(time.ctime()+" [ 控制台 ] "+message)
   return

def exit(message): 
   msgbox(msg='message', title='Python OS', ok_button='终止程序')

#功能项模块
def login(password):
   if password == "123456":
      module.out("登录成功")
      module.out("本次启动时长1秒")
   else:  
      module.out("密码错误")
      exit()
   return

def search(message):
   webbrowser.open("https://www.baidu.com/s?ie=utf-8&word="+message)

def menulist():
   act = {"1.百度一下"}
   #打印act存储的菜单列表
   msg = "菜单："+str(act)
   module.out(msg)
   message = input("请选择程序（错误则返回）：")
   return(message)

def menu(message):
   if message == "1":
      while True:
         act = input("请输入要问的问题，exit退出")
         if act != "exit":
            module.search(act)
         else:
            exit(0)
      
   elif message == 'exit':
      break
   else:
      module.menulist()