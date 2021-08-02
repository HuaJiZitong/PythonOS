from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*
import platform
import requests
def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    print()
def qing():
    system("clear")
print("    \033[41m  \033[42m  \033[0m")
print("    \033[44m  \033[43m  ")
b("\033[92m    欢迎使用")
sleep(1)
print("©Copyright 2019 月高工作室")
sleep(3)
qing()
for i in range(30):
print("\033[94m欢迎")
sleep(0.05)
qing()
print("\033[0m欢迎")
sleep(0.05)
qing()
lay_mp3("baba.mp3")
while 1:
    print(ctime)
    print("0.退出系统")
    print("1.命令提示符")
    print("2.系统属性")
    print("3.时间")
    print("4.屏保")
    print("5.护眼模式")
    prog=int(input("输入应用编号"))
    qing()
    if prog==0:
        play_mp3("goodbye.mp3")
        print("正在退出系统......")
        sleep(2)
        break
    elif prog==1:
        while 1:
            cmd=input("C:\Admin>")
            if cmd!="exit":
                os.system(cmd)
            else:
                break
    elif prog==2:
        print("Pan 1.0")
        print("版权所有©2019 HOTM workshop,保留所有权利。")
        print("Service Pack 1")
        print("    \033[44m__|__\033[0m")
        print("    \033[44m  |  \033[0m")
    elif prog==3:
        for i in range(11):
            print(ctime())
            sleep(1)
            qing()
    elif prog==4:
        for i in range(100):
            for j in range(0,7):
                print("\033[4"+str(j)+"m")
                sleep(1)
                qing()
        print("\033[0m")
    elif prog==5:
        print("\033[32m已打开！")
    else:
        print("程序不存在")
    sleep(6.5)
    qing()
    continue