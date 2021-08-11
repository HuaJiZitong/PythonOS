import time
import module
from easygui import *
#声明变量
#global passwordpadd, password, passwordadd, power_on
def out(message):
   print(time.ctime()+" [ 控制台 ] "+message)
   return

def login(password):
   if password == "123456":
      module.out("登录成功")
      module.out("本次启动时长1秒")
   else:  
      module.out("密码错误")
      exit()
   return

def exit(message):
   msgbox(msg='message', title='Py OS 退出页面', ok_button='终止程序')