import platform as p
import random
import time
from os import *
from tkinter import *
from webbrowser import *

from easygui import *
from pyperclip import *

#开始进入Python的世界
global power_on_time, user, password, login_user, login_password
print(('启动时间：' + time.ctime()))
power_on_time = random.randint(5, 30)
#time.sleep(power_on_time)
print((time.ctime() + '本次启动时长' + str(power_on_time) + '秒'))
c=buttonbox(msg='请选择', title='Py OS启动页面', choices=('登录', '注册/重置'))
if c=="注册/重置":
        if ccbox(msg='第一次使用Py OS，设置新用户Administrator', title='Py OS注册页面', choices=('下一步','返回')):
            master = Tk()
            Label(master, text="用户名：").grid(row=0)
            Label(master, text="密码：").grid(row=1)
            e1 = Entry(master)
            e2 = Entry(master)
            e1.grid(row=0, column=1, padx=10, pady=5)
            e2.grid(row=1, column=1, padx=10, pady=5)
            e1.insert(0, "Administrator")
            def show():
                user = e1.get()
                password = e2.get()
                login_user = user
                login_password = password
                print("用户名：%s" % user)
                print("密码：%s" % password)
                print("用户名：%s" % login_user)
                print("密码：%s" % login_password)
            Button(master, text="确认信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
            Button(master, text="退出", width=10, command=master.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)
            mainloop()
        else:
            msgbox(msg='您取消了注册，请重新运行程序来启动', title='Py OS Error页面', ok_button='终止程序')
elif c=="登录":
    master = Tk()
    Label(master, text="用户名：").grid(row=0)
    Label(master, text="密码：").grid(row=1)
    e3 = Entry(master)
    e4 = Entry(master)
    e3.grid(row=0, column=1, padx=10, pady=5)
    e4.grid(row=1, column=1, padx=10, pady=5)
    e3.insert(0, "Administrator")
    def show():
        login_user = e3.get()
        login_password = e4.get()
        print("用户名：%s" % login_user)
        print("密码：%s" % login_password)
    Button(master, text="确认信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(master, text="退出", width=10, command=master.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)
    mainloop()
else:
    msgbox(msg='遇到无法处理的问题请重新启动Py OS', title='Py OS Error页面', ok_button='终止程序')

if login_user == user and login_password == password :
    msgbox(msg='登录成功', title='Py OS 引导页面', ok_button='进入桌面')
else:
    msgbox(msg='遇到无法处理的问题请重新启动Py OS', title='Py OS Error页面', ok_button='终止程序')
