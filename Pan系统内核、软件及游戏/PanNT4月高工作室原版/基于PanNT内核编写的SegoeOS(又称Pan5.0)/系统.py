# Segoe OS 2020                                                                                                                             
#  +============导库============+
from  time  import *
from random import *
from xes.ext import *
from xes.map import *
from   math  import *
from xes.AIspeak import *
import requests
import json
import os
import sys
import shutil
import platform
import urllib.request
import urllib.parse
import datetime 
import re
'''
更新日志:
Beta1.0:2020.4.30 初始版本
1.0:2020.5.4 公测人员已满，结束公测
'''
#  +============初始化============+
area = "中文"          #语言
name = "未登录"        #用户姓名初始
gc   = 10              #金币数，gold coin的缩写
virsion = 1            #版本号
eyeshield = "关"       #护眼模式
vip = 0                #会员等级，顶级为SVIP-12
gender = "未知"        #性别
interview = 0          #个人数据采访
login = 0              #成功登录
register = 0           #是否注册
tel = "未知"           #电话
password = ""          #密码
YouKe = 0              #是否游客
JI_HUO = 0             #是否激活
fuHuoBi = 0            #复活币
ad = 1                 #广告
jsb = {}               #记事本
jsbr = {}              #记事本回收站
jsbrc = {}             #记事本内容找回
smm = None             #输密码
passport = None        #应用验证
scale = 15             #加载条专用
syh = "n"              #双用户
easyjy=0               #是否禁用简易模式

#定义函数
def qing():            #清屏函数
    os.system('clear')
def computerfailure(cause):
    print("\033[44m")
    print("\033[31m:(  Error")
    print("\033[36m您的电脑遇到问题，需要重新启动。")
    print("\033[34m原因可能是:{}".format(cause))
    print("\033[33m我们正在为您收集某些错误信息，然后为您重新启动")
    print("\033[31m(准备中)")
    sleep(2)
    for e in range(100):
        print("\033[1A\033[31m(完成",e+1,"%)")
        sleep(0.1)
    print("\033[1A\033[31m(已完成)        ")
    sleep(1)
    qing()
    sleep(1)
    qing()
    print("\033[0m")
    print("\033[0m\033[?25l")
    for i in range(5):
        print("\033[1A_")
        sleep(0.3)
        print("\033[1A ")
        sleep(0.3)
    qing()
    sleep(0.5)
    print(r"C:\Users\SogoeOS>if(suc){shutdown -r -t 0}")
    sleep(0.1)
    qing()
    print("\033[32m      SegoeOS     ")
    spt  ("\033[33m___________________")
    qing()
    error = randint(1,10)
    if error == 5:
        print("\033[31m问题修复失败！请重新运行程序~")
        quit()
    else:
        print("\033[0m\033[32m恭喜，问题修复成功！")
        sleep(3)
        qing()
def spt(text):         #逐字输出函数1
    sys.stdout.write('\r'+' '*0+'\r')
    sys.stdout.flush()
    for df in text:
        sys.stdout.write(df)
        sys.stdout.flush()
        sleep(0.1)
    print()
def dlp(text):         #登录输出
    sys.stdout.write('\r'+' '*0+'\r')
    sys.stdout.flush()
    for df in text:
        sys.stdout.write(df)
        sys.stdout.flush()
        sleep(0.01)
def spt2(text,time):         #逐字输出函数2
    sys.stdout.write('\r'+' '*0+'\r')
    sys.stdout.flush()
    for df in text:
        sys.stdout.write(df)
        sys.stdout.flush()
        sleep(time)
    print()
def f(line):
    for i in range(len(line)):
        print("\r"+line[0:i:1], end="")
        sleep(0.03)
    print("")
def dh(this):
    print(this)
    sleep(0.5)
    qing()
def shutdown():        #快速关机函数
    print("\033[?25l\033[8m")
    qing()
    quit()
def wang_password():
    global password,tel,gender,name
    wmm = input("\033[0m\033[?25l\033[33m你是否忘记了密码（yes/no）")
    if wmm == "yes":
        xm2 = input("\033[36m请输入你的姓名：")
        xb2 = input("\033[34m请输入你的性别：")
        sjh2 = input("\033[32m请输入你的电话：")
        if xm2 == name and xb2 == gender and sjh2 == tel:
            print("\033[32m找回了你的密码：",password)
            sleep(2)
            geng = input("\033[35m你要不要更改密码（yes/no）：")
            if geng == "yes":
                mm1 = input("\033[33m请输入新密码：")
                mm2 = input("\033[36m请再次输入新密码：")
                if mm1 == mm2:
                    password = mm1
                    print("\033[34m密码更改成功~")
                    sleep(2)
                else:
                    print("\033[31m第一次输入的和第二次不一致。")
                    sleep(2)
        else:
            print("\033[31m输入有误，无法找回密码~")
            sleep(2)
    else:
        print("\033[31m好的")
        sleep(1)
def baovip(vipp):
    global vip,gc,name
    qing()
    print("\033[33m此功能仅限Segoe OS SVIP-{}用户使用~".format(vipp))
    sleep(0.5)
    print("\033[36m400金币=SegoeOS SVIP-3 + 小孙系统vip + Pan2020vip（近期搞活动，买SegoeOS的会员送小孙系统会员再送pan2020会员，活动截止至6月1日）")
    xianb = input("\033[34m你是否要花400金币立刻包VIP（yes/no）:")
    qing()
    if xianb == "yes":
        if gc >= 400:
            b = gc - 400
            qing()
            print("\033[32m  ○ 购买中")
            printer("\033[34m------------\n")
            sleep(0.5)
            qing()
            vip = 3
            print("\033[34m恭喜你，购买成功！您已是VIP！(关机前有效)")
        else:
            print("\033[31m抱歉，你的金币不足以购买400金币的VIP。")
    else:
        print("\033[33m滴，您已放弃交易！")
    sleep(1.5)
def yanzheng(app):
    qing()
    global passport
    print("\033[93m“"+str(app)+"”想要对你的SogoeOS进行更改\033[0m")
    print("\033[1;32m已验证的开发者:XiaoSun and Pan\033[0m")
    print("\033[93m1 = 允许    2 = 不允许")
    yunxu = input("\033[1;31m>>>")
    print("\033[0m")
    qing()
    if yunxu == "1":
        passport = 1
    elif yunxu == "2":
        passport = 0
    else:
        passport = 0
    return passport
def input_password():
    global smm,password
    if YouKe == 1:
        print("\033[0m\033[36m提示：您的密码是",password)
    mmyan = input("\033[0m\033[?25h\033[33m请输入密码:")
    if mmyan == password:
        print("\033[?25l")
        qing()
        smm = "正确"
    else:
        smm = "错误"
        print("\033[?25l\033[31m密码错误，无法进入。")
        sleep(1)
        qing()
def PDvip():
    global name,password,gc,vip,interview,tel,register,gender,YouKe
    YouKe = 0
    if name == "孙嘉昊":
        if password == "happy516888" or password == "111222":
            vip = 12
            register = 1
            interview = 1
            JI_HUO = 1
            fuHuoBi = 100000000000
            gender = "男"
            tel = "15906510834"
            gc = 1000000000000000
            print("\033[32m小孙，识别出你是VIP。\033[0m")
            speak("尊敬的开发者孙嘉昊，欢迎进入系统。")
            sleep(0.5)
        else:
            print("\033[31m密码错误!登录失败!")
            name = "未登录"
            vip = 0
            password = ""
    elif name == "潘夕习":
        if password == "pi20308303":
            vip = 12
            register = 1
            interview = 1
            JI_HUO = 1
            fuHuoBi = 100000000000
            gender = "男"
            tel = "18900263119"
            gc = 1000000000000000
            print("\033[32m识别出你是VIP用户。\033[0m")
            speak("尊敬的开发者潘夕习，欢迎进入系统。")
            sleep(0.5)
        else:
            print("\033[31m密码错误!登录失败!")
            name = "未登录"
            vip = 0
            password = ""
    else:
        print("\033[93m注册中，请耐心等待，加微信jackiexiaosun08或pjf420137013领取Segoe终生VIP...")
        sleep(1)

def easy():
    while 1:
        print(strftime("现在是%H点%M分",localtime()))
        print("SogoeOS 2020 XP系统有这些软件:")
        print("\033[94m1=退出简易模式")
        print("\033[91m2=计算器")
        print("\033[93m3=记事本(非会员旗舰版)")
        print("\033[95m4=申请VIP")
        print("\033[96m5=性能监视器")
        easo=int(input("\033[94m请输入要打开的应用编号:"))
        qing()
        if easo==1:
            print("正在退出......")
            sleep(3)
            qing()
            print("你的工作将尽可能的不会保存，确定要退出吗？")
            exiteasy=int(input("1=退出 2=取消"))
            qing()
            if exiteasy==1:
                print("正在删除文件......")
                sleep(4)
                qing()
                print("正在退出......")
                sleep(2)
                break
            else:
                print("好的，您已取消退出。")
        elif easo==2:
            while 1:
                try:
                    qing()
                    print("\033[32m    - 普通计算器 -")
                    kaishi1 = input("\033[33m按Enter键开始(字符退出)：")
                    if kaishi1 == "":
                        qing()
                        number1 = input("\033[33m请输入第一个数字: ")
                        number2 = input("\033[32m请输入第二个数字: ")
                        leixin = input("\033[34m请输入运算符号:(\033[31m1.加法，\033[32m2.减法，\033[33m3.乘法，\033[36m4.除法): ")
                        if leixin == "1":
                            fu = "+"
                        elif leixin == "2":
                            fu = "-"
                        elif leixin == "3":
                            fu = "*"
                        elif leixin == "4":
                            fu = "/"
                        else:
                            fu = "+"
                        qing()
                        print("\033[31m正在运算中...\033[33m")
                        sleep(0.1)
                        qing()
                        #请求列竖式
                        if len(number1) == 2 and len(number2) == 2 and fu == "*":
                            print("         "+str(number1[0])+"   "+str(number1[1]))
                            print(" "+fu+"       " +str(number2[0])+"   "+str(number2[1]) )
                            print("-------------------------")
                            shu1_n2 = number2[1]
                            shu2_n2 = number2[0]+"0"
                            shu1_n2 = int(shu1_n2)
                            shu2_n2 = int(shu2_n2)
                            number1 = int(number1)
                            number2 = int(number2)
                            print("       ",shu1_n2 * number1)
                            print("       ",shu2_n2 * number1)
                            print("-------------------------")
                            print("       ",number1 * number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "+":
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1+number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "-":
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1 - number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "*" and len(number1) <= 2 and len(number2) <= 2:
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1 * number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "*" and len(number1) > 2 and len(number2) > 2:
                            qing()
                            print()
                            print()
                            print("\033[33m○ 正在加载竖式\033[31m")
                            print()
                            print()
                            sleep(2)
                            qing()
                            print("     ?    ")
                            print("竖式加载失败")
                            print()
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "/":
                            print("\033[31m抱歉，此版本仅支持加法、减法和乘法的竖式，暂不支持除法竖式~")
                            #类型判断并运算
                            number1 = int(number1)
                            number2 = int(number2)
                            if leixin == "1":
                                print("\033[34m"+str(number1)+"+"+str(number2)+"的答案是:",number1 + number2)
                            elif leixin == "2":
                                print("\033[34m"+str(number1)+"-"+str(number2)+"的答案是:",number1 - number2)
                            elif leixin == "3":
                                print("\033[34m"+str(number1)+"x"+str(number2)+"的答案是:",number1 * number2)
                            elif leixin == "4":
                                leixinofchu = input("\033[33m请选择除法类型：(1.小数计算，2.带余数法计算):")
                                if leixinofchu == "1":#小数计算
                                    print("\033[34m"+str(number1)+"÷"+str(number2)+"的答案是:",number1 / number2)
                                elif leixinofchu == "2":#余数计算
                                    answer_of_chu = str(number1 // number2)+"······"+str(number1 % number2)
                                    print("\033[34m"+str(number1)+"÷"+str(number2)+"的答案是:",answer_of_chu)
                                else:
                                    print("\033[31m没有此选项~")
                        else:
                            qing()
                            print("\033[31m没有此选项~")
                        input("\033[33m按Enter键完成：")
                        qing()
                    else:
                        qing()
                        print("\033[31m退出中...")
                        sleep(1)
                        break
                except ZeroDivisionError:
                    print("除数不能为0")
                except ValueError:
                    print("运算错误！")
        elif easo==3:
            while True:
                qing()
                print("\033[?25h\033[32m欢迎使用记事本!\033[34m输入已有记事本打开,\033[33m输入新名字即可新建,\033[31m输入exit退出,\033[35m输入recycle查看回收站")
                print("\033[33m已有记事本:\033[0m")
                for i in jsb:
                    print(i)
                j=input("\033[36m输入记事本名:")
                qing()
                if j.lower()=='exit':
                    break
                elif j.lower()=='recovery':
                    print("\033[36m| Segoe Recovered files\033[32m")
                    for i in jsbrc:
                        print("\033[32m记事本名称 : "+str(i))
                        print("\033[33m记事本内容 : 见下行\n"+str(jsbrc[i]))
                        print()
                    input("\033[36m（recovery内容无法恢复，只支持临时查看，文章中\033[34m\\n\033[36m代表换行；回车键返回。）")  
                elif j.lower()=='recycle':
                    print("\033[36m| 记事本回收站\033[32m")
                    for i in jsbr:
                        print(i)
                    cao = input("\033[36m输入要执行的操作(1=恢复 2=彻底删除 3=全部彻底删除 4=全部恢复)：")
                    if cao != '3' and cao != '4':
                        jj = input("\033[33m输入要操作的记事本名：")
                    if cao == '1':
                        if jj in jsbr:
                            jsb[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m恢复成功！")
                        else:
                            print("\033[31m记事本名输入错误")
                    elif cao == '2':
                        if jj in jsbr:
                            jsbrc[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m彻底删除成功！")
                        else:
                            print("\033[31m记事本名输入错误")
                    elif cao == '3':
                        for i in jsbr:
                            jsbrc[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在抹掉......")
                        sleep(0.5)
                        print("\033[32m删除成功！")
                    elif cao == '4':
                        for i in jsbr:
                            jsb[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在恢复......")
                        sleep(0.5)
                        print("\033[32m恢复成功！")
                    else:
                        print("\033[31m无效操作")
                    input("\033[35mEnter键返回")
                elif j in jsb:
                    print(jsb[j])
                    print("\033[33m1.更改 \033[31m2.删除 \033[34m3.重命名 \033[31m其他退出")
                    c=input("\033[0m请选择：")
                    if c=='1':
                        qing()
                        nr = ''
                        print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                        while True:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                qing()
                                print("\033[32m输入更改后的内容，输入esc完成，输入clear清空所有内容。\033[33m")
                                continue
                            elif '<fontcolor='in a:
                                if len(a) < 12:
                                    print("\033[31m语法错误：<fontcolor=  value error:is no color input\033[33m")
                                    continue
                                if a[11] == '红':
                                    nr = nr + '\033[31m'
                                elif a[11] == '绿':
                                    nr = nr + '\033[32m'
                                elif a[11] == '黄':
                                    nr = nr + '\033[33m'
                                elif a[11] == '蓝':
                                    nr = nr + '\033[34m'
                                elif a[11] == '紫':
                                    nr = nr + '\033[35m'
                                elif a[11] == '青':
                                    nr = nr + '\033[36m'
                                text = a + '\n'
                                nr = nr + text
                            else:
                                text = a + "\n"
                                nr = nr + text
                        jsb[j]=nr
                        print("\033[32m更改成功!")
                    elif c=='2':
                        jsbr[j] = jsb[j]
                        del jsb[j]
                        print("\033[32m删除成功，可在回收站查看!")
                    elif c=='3':
                        new=input("\033[36m输入新记事本名:")
                        if new=='exit':
                            print("\033[31m不可使用关键词exit命名记事本!")
                            sleep(2)
                            continue
                        jsb[new] = jsb[j]
                        del jsb[j]
                        print("\033[32m更改成功!")
                    else:
                        continue
                    sleep(2)
                else:
                    nr = ''
                    print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                    while True:
                        a = input()
                        if a == 'esc':
                            break
                        elif a == 'clear':
                            nr = ''
                            qing()
                            print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                            continue
                        elif '<fontcolor='in a:
                            if len(a) < 12:
                                print("\033[31m语法错误：<fontcolor=  value error:is no color input\033[33m")
                                continue
                            if a[11] == '红':
                                nr = nr + '\033[31m'
                            elif a[11] == '绿':
                                nr = nr + '\033[32m'
                            elif a[11] == '黄':
                                nr = nr + '\033[33m'
                            elif a[11] == '蓝':
                                nr = nr + '\033[34m'
                            elif a[11] == '紫':
                                nr = nr + '\033[35m'
                            elif a[11] == '青':
                                nr = nr + '\033[36m'
                            text = a + '\n'
                            nr = nr + text
                        else:
                            text = a + "\n"
                            nr = nr + text
                    jsb[j]=nr
                    print("新建成功!")
                    sleep(2)
                print("\033[?25l")
            else:
                baovip(4)
        elif easo==4:
            print("©2020 Copyright KeSheng & HOTM")
            print("buy permanent VIP")
            print("if you want buy the permanent VIP,Please add me in Wechat:jackiexiaosun08(Jiahao Sun)pjf420137013(Xixi Pan).")
            print("After you add me in Wechat you should pay:")
            print("￥10 1month\n￥25 3month\n￥52 6month\n￥123 1year\n￥365 permanent")
            print("that is the form of the prise of the VIP,purchase VIP according to your own needs.")
            print("购买永久VIP")
            print("如果你想购买永久VIP，请先加微信:jackiexiaosun08(孙嘉昊)pjf420137013(潘夕习)。")
            print("加我之后，你应该付款:")
            print("￥10 1个月\n￥25 3个月\n￥52 半年\n￥123 一年\n￥365 永久")
            print("上面是VIP价格表，请按自己的需求购买。")
            input("请按Enter键以表示你阅读并同意以上条款:")
        elif easo==5:
            print("\033[32m+===============欢迎使用Segoe智能电脑性能监视器===============+")
            input("\033[36m                      Enter键开始测试。             ")
            qing()
            print("\033[33m延时:测试中...")
            print("\033[36m登录:等待中...")
            print("\033[34m版本:等待中...")
            #测延时
            t1_c = time()
            sleep(1)
            t2_c = time()
            t_c = t2_c - t1_c
            if t_c > 1:
                t_c2 = t_c - 1
                if t_c2 > 0.21:
                    yanshi = str(t_c2)+"秒，您的延时非常长，说明网络常年不在线，建议您检查网络设置再重启机器。"
                elif t_c2 > 0.12:
                    yanshi = str(t_c2)+"秒，恭喜你，你的延时速度超过了全国0%的电脑，说明网络极差。"
                elif t_c2 > 0.01:
                    yanshi = str(t_c2)+"秒，您的延时较长，说明网络有点差。"
                elif t_c2 > 0.004:
                    yanshi = str(t_c2)+"秒，您的延时有一点点长，可能是卡顿问题，此为正常~"
                elif t_c2 <= 0.002:
                    yanshi = str(t_c2)+"秒，您的延时正常，继续保持哦~"
                else:
                    yanshi = str(t_c2)+"秒，AI智能分析出错！！"
            elif t_c == 1:
                yanshi = "太棒啦，您的电脑没有延时~"
            elif t_c < 1:
                yanshi = "您的电脑太快啦，比学而思编程社区最快的系统运行速度还快，快了 -- 秒。"
            else:
                yanshi = "AI无法分析你的电脑，请重启机器。"
            #测登录
            qing()
            print("\033[33m延时:测试完成")
            print("\033[36m登录:测试中...")
            print("\033[34m版本:等待中...")
            if register==1:
                tryy = "您已创建账号并登录"
            else:
                tryy = "您没有账号或没有登录"
            #测更新
            qing()
            print("\033[0m\033[33m延时:测试完成")
            print("\033[36m登录:测试完成")
            print("\033[34m版本:测试中...")
            ce3 = "Segoe版本:已是最新 python编译器版本:{} 您的系统:{}".format(sys.version[0:5],platform.architecture()[0])
            sleep(2)
            qing()
            print("\033[33m延时:测试完成")
            print("\033[36m登录:测试完成")
            print("\033[34m版本:测试完成")
            sleep(0.1)
            qing()
            print("\033[32m测试结果:")
            print("\033[36m延时:",yanshi)
            print("\033[36m登录:",tryy)
            print("\033[34m版本:",ce3)
            print("\033[35m此测试数据绝对准确。")
            input("\033[31mEnter键返回桌面")
        sleep(6.5)
        qing()
        continue
    
#========================正文========================
#  +============识别星期============+
t1 = strftime("星期%w",localtime())
if t1 == "星期1":
    text_x = "星期一"
elif t1 == "星期2":
    text_x = "星期二"
elif t1 == "星期3":
    text_x = "星期三"
elif t1 == "星期4":
    text_x = "星期四"
elif t1 == "星期5":
    text_x = "星期五"
elif t1 == "星期6":
    text_x = "星期六"
elif t1 == "星期0":
    text_x = "星期日"
else:
    text_x = "---"
            
#  +============隐藏光标============+
print("\033[?25l\033[0m\033[32m")
qing()
#  +============正式开机============+
print("    \033[41m  \033[42m  \033[0m")
print("    \033[44m  \033[43m  \n\033[0m\033[34mSegoeOS 2020")
spt("\033[32m - 欢迎使用 -")
print("\033[36m©2020 - 版权归科盛、月高工作室所有\033[93m")
sleep(1.5)
qing()
print()
print()
print("        □")
print()
print()
print()
sleep(0.2)
qing()
print()
print("      ______ ")
print("      |     |")
print("      |  +  |")
print("      |_____|")
print()
sleep(0.2)
qing()
print("__________________")
print("|                  |")
print("|                  |")
print("|        +         |")
print("|                  |")
print("|__________________|")
f("\033[92m孙嘉昊×潘夕习联合出品 \n")
print("\033[36m请点击屏幕激活光标！")
sleep(3)
while True:
    qing()
    dlp("\033[096m""===================>Welcome To SegoeOS<===================\n")
    dlp("\033[035m""Sigh in：\n")
    dlp("\033[034m""1.极速体验  \033[036m""2.用户登录  \033[033m""3.用户注册  \033[032m""4.开发者登录  ""\033[31m5=暂不登录\n")
    dlp("\033[96m""请输入登录方式：")
    sighinMode = input("")
    qing()
    if sighinMode == '1' or sighinMode == '极速体验':
        YouKe = 1
        you = randint(100000000,999999999)
        name = "游客"+str(you)
        vip = 0
        vt = randint(1,3)
        password = randint(100000,999999)
        password = str(password)
        print("\033[36m好的，请记住:\n\033[32m用户名是:",name,"\n\033[34m您的密码是:",password,"\n\033[36m您的VIP免费体验次数为:",vt)
        input("\033[31m记住后按Enter。")
        login = 1
        break
    elif sighinMode == '2' or sighinMode == '用户登录':
        print("\033[32m□ Segoe智能键盘")
        name = input("\033[34m请输入姓名:")
        if name == "":
            name = "无名氏"
        lxm1 = len(name)
        lxm = lxm1 - 1
        qing()
        print("\033[32m□ Segoe智能键盘")
        print("\033[34m请输入姓名:"+name[0]+lxm*"*")
        password = input("\033[33m请输入密码:")
        qing()
        lmm1 = len(password)
        lmm = lmm1 - 3
        print("\033[32m□ Segoe智能键盘")
        print("\033[34m请输入姓名:"+name[0]+lxm*"*")
        print("\033[33m请输入密码:"+password[0:3]+lmm*"*")
        PDvip()
        login = 1
        break
    elif sighinMode == '3' or sighinMode == '用户注册':
        qing()
        print("\033[33m准备中...")
        sleep(0.1)
        qing()
        name = input("\033[32m请输入你的姓名：")
        qing()
        password = input("\033[34m请创建密码：")
        qing()
        tel = input("\033[36m请输入手机号：")
        qing()
        ji_hui = 6 
        while True:
            ji_hui = ji_hui - 1
            if ji_hui > 0:
                qing()
                yannum = randint(100000,999999)
                print("\033[32m|通知：                                       |")
                print("|您的验证码是"+str(yannum)+"，请勿泄露给他人。         |")
                print("|_____________________________________________|")
                myn = input("\033[34m请输入收到的验证码：")
                try:
                    myn = int(myn)
                    if int(myn) == yannum:
                        print("\033[36m验证码正确，注册成功！")
                        sleep(1)
                        break
                except:
                    print("\033[31m输入错误，注册失败！")
                    sleep(2)
                else:
                    print("\033[31m验证码不正确，请重新输入！")
                    sleep(2)
            elif ji_hui <= 0:
                qing()
                print("\033[31m你已输入多次不正确验证码\033[32m已自动为您变为游客体验模式，您的密码为123456！\033[0m")
                password = "123456"    
                YouKe = 1
            break
        break
        login = 1
    elif sighinMode == '4' or sighinMode == '开发者登录':
        print("\033[33m稍等...")
        sleep(0.2)
        qing()
        xm_list = ["孙嘉昊","潘夕习"]
        tx_list = ["sun","pan"]
        tong1 = input("\033[32m请输入开发者真姓名:")
        tong2 = input("\033[35m请输入开发者通行证:")
        if tong1 == xm_list[0] and tong2 == tx_list[0]:
            vip = 12
            register = 1
            interview = 1
            JI_HUO = 1
            fuHuoBi = 100000000000
            gender = "男"
            tel = "15906510834"
            gc = 1000000000000000
            password = "111222"
            name = xm_list[0]
            print("\033[32m小孙，识别出你是VIP。\033[0m")
            speak("尊敬的开发者孙嘉昊，欢迎进入系统。")
            sleep(0.5)
            break
        elif tong1 == xm_list[1] and tong2 == tx_list[1]:
            vip = 12
            register = 1
            interview = 1
            JI_HUO = 1
            fuHuoBi = 100000000000
            gender = "男"
            tel = "18900263119"
            gc = 1000000000000000
            password = "pi20308303"
            name = xm_list[1]
            print("\033[32m识别出你是VIP。\033[0m")
            speak("尊敬的开发者潘夕习，欢迎进入系统。")
            sleep(0.5)
            break
        else:
            print("\033[31m通行码不正确，登录失败！")
            sleep(1)
        login = 1
    elif sighinMode == '5' or sighinMode == '暂不登录':
        login = 0
        break
qing()
print("\n\n\033[93m○ 欢迎"+str(name))
sleep(1.5)
qing()
while True:
    qing()
    if vip >= 1:
        print("\033[32m您是SVIP-"+str(vip)+"用户 ?")
    else:
        print("\033[32m您是普通用户 ?")
    myDate = strftime("%m-%d",localtime())
    t = strftime("\033[33m%Y-%m-%d %H:%M:%S",localtime())
    print(t,text_x+"\033[34m")
    hour=int(strftime("%H",localtime()))
    if hour<6 or hour>=22:
        print("夜深了,"+name+",您有"+str(gc)+"个金币")
    elif hour<9:
        print("早上好,"+name+",您有"+str(gc)+"个金币")
    elif hour<11:
        print("上午好,"+name+",您有"+str(gc)+"个金币")
    elif hour<13:
        print("中午好,"+name+",您有"+str(gc)+"个金币")
    elif hour<18:
        print("下午好,"+name+",您有"+str(gc)+"个金币")
    else:
        print("晚上好,"+name+",您有"+str(gc)+"个金币")
    print("\033[35mSegoe OS 2020系统有这些软件(暂时):")
    print("\033[31m1=开始菜单")
    print("\033[32m2=万能计算器")
    print("\033[33m3=启动版本转换")
    print("\033[34m4=电脑检测性能")
    print("\033[35m5=有道翻译官")
    print("\033[32m6=智能笔记本")
    print("\033[33m7=音乐")
    print("\033[34m8=欢乐游戏")
    print("\033[35m9=Sogoe安全卫士")
    print("\033[31m10=Sogoe virtual PC 2019")
    print("\033[32m11=强制关机(如电脑严重卡慢无法正常关机，可通过此功能进行强行关闭)")
    print("\033[33m12=CrazyError(无聊千万别点)")
    print("\033[34m13=积分体验制")
    print("\033[35m14=闹钟")
    print("\033[36m15=信息")
    print("\033[91m16=特效模式")
    print("\033[92m17=Sogoe动画")
    print("\033[93m18=地图")
    software = input("\033[36m请输入要打开的应用编号：")
    qing()
    if software == "1":
        while True:
            qing()
            print("\033[36m| 开始菜单")
            print("\033[31m1=电源管理")
            print("\033[32m2=账号管理")
            print("\033[33m3=个性管理")
            print("\033[34m退出输入esc")
            shezhi = input("\033[36m>>>")
            qing()
            if shezhi == "1":
                print("\033[33m| 电源管理")
                print("\033[34m1=关机 \033[32m2=重启 \033[36m3=返回上一级")
                shezhi = input("\033[33m>>>")
                qing()
                if shezhi == "1":
                    print("\033[32m+====关机确认====+")
                    shezhi = input("\033[33m确定关机(y/n):")
                    if shezhi == "y":
                        shutdown()
                    else:
                        print("\033[32m好的，您已取消关机。")
                        sleep(1)
                        break
                elif shezhi == "2":
                    print("\033[32m+====重启确认====+")
                    shezhi = input("\033[33m确定重启(y/n):")
                    if shezhi == "y":
                        qing()
                        print("\033[93m       ○       ")
                        print("               ")
                        print("  正在重新启动 ")
                        sleep(3)
                        qing()
                        sleep(0.5)
                        print("\033[000m")
                        for i in range(4):
                            print("\033[1A_")
                            sleep(0.3)
                            print("\033[1A ")
                            sleep(0.3)
                        sleep(1.7)
                        print(r"C:\Users\SogoeOS>run reboot.bat")
                        print(r"C:\Users\SogoeOS>shutdown -r -t 0")
                        sleep(0.3)
                        qing()
                        print("\n\n\033[32m正在启动Segoe OS 2020系统......")
                        sleep(2)
                        print("\033[1A\033[93m○ 欢迎"+name+"                          ")
                        sleep(2)
                        qing()
                        break
                    else:
                        print("\033[32m好的，您已取消重启。")
                        sleep(1)
                        break
                elif shezhi == "3":
                    continue
            elif shezhi == "2":#账号管理
                if register == 0:
                    qing()
                    print("\033[36m")
                    qing()
                    print(name+"，您还没有注册过Segoe账号，快去注册一个吧！")
                    sleep(0.5)
                    zcks = input("\033[33m你现在就要注册吗（yes/no）:")
                    if zcks == "yes":
                        print("\033[35m注册开始。")
                        print("\033[32m输入时不要担心，不会盗走你的个人资料。")
                        sleep(1)
                        qing()
                        name = input("\033[34m请输入中文姓名：")
                        qing()
                        print("\033[34m请输入中文姓名："+name[0]+"**")
                        gender = input("\033[32m请输入你的性别（男/女）：")
                        qing()
                        print("\033[34m请输入中文姓名："+name[0]+"**")
                        print("\033[32m请输入你的性别（男/女）："+gender)
                        tel = input("\033[33m请输入有效手机号：")
                        qing()
                        print("\033[34m请输入中文姓名："+name[0]+"**")
                        print("\033[32m请输入你的性别（男/女）："+gender)
                        print("\033[33m请输入有效手机号："+tel[0:3]+"*******")
                        password = input("\033[36m请设置新密码：")
                        qing()
                        print("\033[34m请输入中文姓名："+name[0]+"**")
                        print("\033[32m请输入你的性别（男/女）："+gender)
                        print("\033[33m请输入有效手机号："+tel[0:3]+"*******")
                        lmm = len(password)
                        lmm2 = lmm - 3
                        lmm3 = lmm2 * "*"
                        print("\033[36m请设置新密码："+password[0:2]+lmm2 * "*")
                        mm2 = input("\033[35m请再次输入新密码：")
                        if password == mm2:
                            print("\033[32m输入成功")
                        else:
                            print("\033[31m两次输入不同哦~")
                            input("\033[33mEnter键:")
                        sleep(0.5)
                        qing()
                        print("\033[36m| 请选择验证方式：\033[33m")
                        print("1=验证码")
                        print("2=人脸识别")
                        xuan_ = input("\033[36m我的选择：")
                        if xuan_ == "1":
                            while True:
                                qing()
                                num2 = str(randint(100000,999999))
                                print("\033[35m你的验证码是：",num2)
                                yan = input("\033[32m请填写验证码： ")
                                if yan != num2:
                                    print("\033[31m输入错误")
                                else:
                                    print("\033[34m输入正确！")
                                    sleep(1)
                                    break
                        elif xuan_ == "2":
                            print("\033[033m人脸识别中，请稍候...")
                            print("       ○          ")
                            for x in range(10):
                                print("\033[034m###############")
                                sleep(0.1)
                            print("\033[037m")
                            print("\033[32m识别成功！")
                        print("====================")
                        print("注册成功！")
                        sleep(0.5)
                        print("登录成功！")
                        sleep(2)
                        register = 1
                        interview = 1
                else:
                    print("Segoe用户，欢迎您~")
                    sleep(0.8)
                qing()
                input_password()
                if smm == "正确":
                    qing()
                    print("\033[34m\n\n密码正确!\033[36m")
                    sleep(0.5)
                    qing()
                    print("\033[92m| 用户信息\033[36m")
                    if vip >= 1:
                        print("         ?         ")
                        print("       "+name+"       ")
                        print("\033[33m会员：SVIP-"+str(vip))
                    else:
                        print("         ?         ")
                        print("       "+name+"       ")
                        print("\033[33m类型：普通用户")
                    print("\033[32m金币数："+str(gc))
                    print("\033[34m性别："+str(gender))
                    print("\033[35m手机号："+str(tel))
                    print("\033[32m密码："+str(password))
                    if syh == "y":
                        print("         ?         ")
                        print("       "+name2nd+"       ")
                        print("\033[33m会员：双用户福利SVIP-3")
                        print("\033[34m性别："+str(gender2nd))
                        print("\033[35m手机号："+str(tel2nd))
                        print("\033[32m密码："+str(password2nd))
                    else:
                        print("\033[33m双用户功能没有启用")
                    print("\033[92m| 用户设置")
                    aqx = input("\033[34m1=改密码 \n\033[32m2=设置指纹 \n\033[33m3=双用户模式 \n\033[31m4=退出登录 \n\033[36mesc=返回上一级\n\033[31m>>>")
                    if aqx == "1":
                        jmm = input("\033[33m请输入旧密码:\033[8m\033[?25h")
                        if jmm == password:
                            password = input("\033[0m\033[33m请输入新密码:\033[8m\033[?25h")
                            print("\033[0m\033[32m\033[?25l成功把密码设置成"+password)
                        else:
                            print("\033[0m\033[31m\033[?25l旧密码输入错误。")
                    elif aqx == "2":
                        mm2 = input("\033[33m请先输入密码:\033[8m\033[?25h")
                        if mm2 == password:
                            print("\033[0m\033[?25l\033[32m输入正确。\033[36m")
                            sleep(0.5)
                            qing()
                            print("\033[34m请把手指放在此电脑的指纹识别处以感应指纹。")
                            sleep(0.1)
                            print("\033[33m系统已正在识别...")
                            sleep(2)
                            print("\033[33m正在保存...")
                            sleep(1)
                            qing()
                            print("\033[32m设置成功！")
                        else:
                            print("\033[0m\033[?25l\033[31m密码错误~")
                            sleep(1)
                    elif aqx == "3":
                        qing()
                        xmqr = input("\033[33m请确认：你的姓名是不是"+name+"(y/n):")
                        if xmqr == "y":
                            kq = input("\033[34mOK，是否开启双用户模式（yes/no）：")
                            if kq == "yes":
                                qing()
                                name2nd = input("\033[36m请输入用户2的姓名：")
                                password2nd = input("请创建用户2的密码：")
                                gender2nd = input("请输入用户2的性别：")
                                tel2nd= input("请输入用户2的电话：")
                                qing()
                                print("\n\n\033[33m○ 保存中\n\n")
                                sleep(1.5)
                                qing()
                                vip2nd = 3
                                syh = "y"
                                vip = 3
                                print("\033[32m双用户已开启，自动送出福利vip，保存成功~")
                            else:
                                print("\033[32m那么好吧，"+name+"。")
                        else:
                            anme = input("\033[36m那么请重设姓名：")
                            print("\033[32m设置成功~你叫"+name+"了~")
                    elif aqx == "4":
                        qing()
                        tuic = input("\033[33m确定要退出登录吗(y/n):")
                        if tuic == "y":
                            qing()
                            print("\033[31m正在帮您退出登录...")
                            area = "中文"          #语言
                            name = "未登录"        #用户姓名初始
                            gc   = 10              #金币数，gold coin的缩写
                            eyeshield = "关"       #护眼模式
                            vip = 0                #会员等级，顶级为SVIP-12
                            gender = "未知"        #性别
                            interview = 0          #个人数据采访
                            login = 0              #成功登录
                            register = 0           #是否注册
                            tel = "未知"           #电话
                            password = ""          #密码
                            YouKe = 0              #是否游客
                            JI_HUO = 0             #是否激活
                            SHEN_QIAN = "默认"     #深浅
                            fuHuoBi = 0            #复活币
                            ad = 1                 #广告
                            jsb = {}               #记事本
                            jsbr = {}              #记事本回收站
                            jsbrc = {}             #记事本内容找回
                            smm = None             #输密码
                            passport = None        #应用验证
                            syh = "n"              #双用户
                            sleep(1)
                            qing()
                            print("\033[34m退出成功！")
                            sleep(1)
                            print("\033[33m因系统要求，必须重新登录才能继续使用。")
                            sleep(2)
                            qing()
                            print("\033[36m准备中...")
                            sleep(0.2)
                            qing()
                            denglu = 1
                            print("\033[32m□ Segoe智能键盘")
                            sleep(0.1)
                            name = input("\033[34m请输入姓名:")
                            qing()
                            print("\033[32m□ Segoe智能键盘")
                            print("\033[34m请输入姓名:"+name[0]+"**")
                            password = input("\033[33m请输入密码:")
                            qing()
                            lmm1 = len(password)
                            lmm = lmm1 - 3
                            print("\033[32m□ Segoe智能键盘")
                            print("\033[34m请输入姓名:"+name[0]+"**")
                            print("\033[33m请输入密码:"+password[0:3]+lmm*"*")
                            srt2 = time()
                            qing()
                            print("正在处理中...")
                            sleep(0.5)
                            qing()
                            print("\033[36m正在处理中...")
                            for i in range(scale+1):
                                aaa = '*'*i
                                bbb = '.'*(scale-i)
                                ccc =(i/scale)*100
                                print("\r\033[1;32m{:^3.0f}%[{}->{}]".format(ccc,aaa,bbb),end='')
                                sleep(0.01)
                            sleep(0.5)
                            qing()
                            PDvip()
                    elif aqx == "esc":
                        qing()
                        continue
                    else:
                        print("\033[31m没有此选项~")
                else:
                    print("\033[31m密码错误，无法进入。")
                    wang_password()
                sleep(2)
                break
            elif shezhi == "3":
                MiyueAdd=["XAC6L-2L1IF-OUCBR-G2QB2-2M2JV","DJIE2-IEUDN-XXX56-2XEFH-TYU8J","38YUE-SJH97-74PXX-UE5YU-UI89E","JIDE4-U5JN9-Y8EJN-Y5UN3-56TY8","ER3U7-EU8OP-HG89U-EI903-XXXXX-XT6XP"]
                gexing=int(input("1.激活Sogoe 2.禁用简易模式 3.产品简介 4.属性"))
                qing()
                if gexing==1:
                    if JI_HUO==0:
                        print("\033[90m你还没有激活Sogoe,激活后你会获得:")
                        print("1.怀旧2018年版虚拟操作系统 2.积分体验制 3.获得Sogoe奖励")
                        sleep(3)
                        Sogoe_Mi_Yue=input("\033[0m请输入密钥以激活你的Sogoe:")
                        qing()
                        if Sogoe_Mi_Yue in MiyueAdd:
                            print("恭喜！激活成功，目前正在审核！您将会在1小时内收到Sogoe团队的来信。")
                            JI_HUO=1
                            sleep(3)
                            print("恭喜！你的请求已通过审核:)")
                        else:
                            print("激活失败TmT！您输入了无效的密钥或密钥已经被别人使用")
                    else:
                        print("您已激活Sogoe")
                        
                elif gexing==2:
                    print("你需要提供管理员权限，才能进行下一步。")
                    sleep(3);qing();
                    print("禁用成功！\033[94m点击获得SVIP-3以拥有禁用Pan2020XP权限。\033[0m")
                elif gexing==3:
                    print("©Copyright 2019-2020 Kesheng and HOTM workshop")
                    print("SogoeOS 2020 is a new OS by Kesheng and HOTM workshop dveloped on April 10 2020")
                    print("This is the fastest OS and is the handiest OS in the xueersi BCSQ.")
                    print("And for the Pan2020 before the success of the technical preparation,the function is less then Pan2020 and XiaosunOS,but is practical then Pan2020 ans XiaosunOS")  
                    print("It's a bit of an improvement, having learned the lesson that the Pan3.0 was taken off the shelves (Although complaint had been successful,and taken on the shelves).")
                    print("Due to limited technology, some places maybe have bugs or display in English")
                    print("Thanks support!")
                    print("SogoeOS 2020是一个有科盛和月高工作室于2020年4月10日研发的新版操作系统\n这是在学而思编程社区最快而且最容易上手的系统。")
                    print("SogoeOS为Pan2020及之前的系统做好了技术铺垫，虽然功能比Pan2020和小孙系统少，但是比Pan2020和小孙系统更具备实用性。")
                    print("吸取了Pan3.0下架的教训(经申诉，已重新上架)，我们在这方面比之前有一些进步。")
                    print("停止主流支持时间:2020年12月31日 停止技术支持时间:2021年9月19日,请在停止技术支持时间开始左右升级系统！")
                    input("看完按Enter")
                elif gexing==4:
                    print("系统属性")
                    print("SogoeOS 2020 个人版\n版权所有©2019-2020 Kesheng and HOTM workshop\nService Pack 1")
                    print("    \033[41m  \033[42m  \033[0m")
                    print("    \033[44m  \033[43m  ")
                    input("\033[0m看完按Enter")
                else:
                    print("查无此功能！")
            elif shezhi == "esc":
                break
            else:
                print("\033[33m没有这个设置选项~")
                sleep(1.5)
                break
    elif software == "2":
        qing()
        print("\033[002m\033[32m     ﹢﹣× ÷       ")
        print("\033[002m\033[34m欢迎使用万能计算器。")
        sleep(0.5)
        qing()
        print("\033[0m\033[32m     ﹢﹣× ÷       ")
        print("\033[34m欢迎使用万能计算器。")
        sleep(1)
        qing()
        print("\033[35m+===============SegoeOS万能计算器===============+")
        print("\033[31m| 计算器系列")
        print("\033[36m1=普通计算器      \033[32m2=获取数的公因数")
        print("\033[33m3=综合算式计算    \033[34m4=鸡兔同笼问题(VIP专属)")
        print("\033[35m5=平均数计算      \033[36m6=平年闰年计算")
        print("\033[32m7=日期间隔计算(VIP专属)")
        print("\033[31m| 单位转换系列")
        print("\033[32m8=面积转换        \033[34m9=长度转换")
        print("\033[36m10=货币转换")
        ji_xuan = input("\033[33m请输入输入模式的编号:")
        if ji_xuan == "1":
            while 1:
                try:
                    qing()
                    print("\033[32m    - 普通计算器 -")
                    kaishi1 = input("\033[33m按Enter键开始(字符退出)：")
                    if kaishi1 == "":
                        qing()
                        number1 = input("\033[33m请输入第一个数字: ")
                        number2 = input("\033[32m请输入第二个数字: ")
                        leixin = input("\033[34m请输入运算符号:(\033[31m1.加法，\033[32m2.减法，\033[33m3.乘法，\033[36m4.除法): ")
                        if leixin == "1":
                            fu = "+"
                        elif leixin == "2":
                            fu = "-"
                        elif leixin == "3":
                            fu = "*"
                        elif leixin == "4":
                            fu = "/"
                        else:
                            fu = "+"
                        qing()
                        print("\033[31m正在运算中...\033[33m")
                        sleep(0.1)
                        qing()
                        #请求列竖式
                        if len(number1) == 2 and len(number2) == 2 and fu == "*":
                            print("         "+str(number1[0])+"   "+str(number1[1]))
                            print(" "+fu+"       " +str(number2[0])+"   "+str(number2[1]) )
                            print("-------------------------")
                            shu1_n2 = number2[1]
                            shu2_n2 = number2[0]+"0"
                            shu1_n2 = int(shu1_n2)
                            shu2_n2 = int(shu2_n2)
                            number1 = int(number1)
                            number2 = int(number2)
                            print("       ",shu1_n2 * number1)
                            print("       ",shu2_n2 * number1)
                            print("-------------------------")
                            print("       ",number1 * number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "+":
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1+number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "-":
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1 - number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "*" and len(number1) <= 2 and len(number2) <= 2:
                            print(" "+ number1)
                            print(fu + number2)
                            print("-------------------------")
                            number1 = int(number1)
                            number2 = int(number2)
                            print("",number1 * number2)
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "*" and len(number1) > 2 and len(number2) > 2:
                            qing()
                            print()
                            print()
                            print("\033[33m○ 正在加载竖式\033[31m")
                            print()
                            print()
                            sleep(2)
                            qing()
                            print("     ?    ")
                            print("竖式加载失败")
                            print()
                            print("\033[36m - 竖式仅供参考，有时候AI也会犯傻 - ")
                            print()
                        elif fu == "/":
                            print("\033[31m抱歉，此版本仅支持加法、减法和乘法的竖式，暂不支持除法竖式~")
                            #类型判断并运算
                            number1 = int(number1)
                            number2 = int(number2)
                            if leixin == "1":
                                print("\033[34m"+str(number1)+"+"+str(number2)+"的答案是:",number1 + number2)
                            elif leixin == "2":
                                print("\033[34m"+str(number1)+"-"+str(number2)+"的答案是:",number1 - number2)
                            elif leixin == "3":
                                print("\033[34m"+str(number1)+"x"+str(number2)+"的答案是:",number1 * number2)
                            elif leixin == "4":
                                leixinofchu = input("\033[33m请选择除法类型：(1.小数计算，2.带余数法计算):")
                                if leixinofchu == "1":#小数计算
                                    print("\033[34m"+str(number1)+"÷"+str(number2)+"的答案是:",number1 / number2)
                                elif leixinofchu == "2":#余数计算
                                    answer_of_chu = str(number1 // number2)+"······"+str(number1 % number2)
                                    print("\033[34m"+str(number1)+"÷"+str(number2)+"的答案是:",answer_of_chu)
                                else:
                                    print("\033[31m没有此选项~")
                        else:
                            qing()
                            print("\033[31m没有此选项~")
                        input("\033[33m按Enter键完成：")
                        qing()
                    else:
                        qing()
                        print("\033[31m退出中...")
                        sleep(1)
                        break
                except ZeroDivisionError:
                    print("除数不能为0")
                except ValueError:
                    print("运算错误！")
            
        elif ji_xuan == "2":
            qing()
            gys_1 = input("\033[32m请输入一个数以获得因数：")
            print("\033[31m努力计算中...")
            gys_1 = int(gys_1)
            gys_3 = []
            def ys(gys_2):
                gys_5 = 0
                for p in range(gys_1):
                    gys_5 = gys_5 + 1
                    q = gys_1 % gys_5
                    if q == 0:
                        gys_3.append(gys_5)
            ys(gys_1)
            print("\033[34m",gys_1,"的全部因数有：",end = "")
            for gys_4 in gys_3:
                if gys_4 == 1:
                    print("1",end = "")
                else:
                    print(",",gys_4,end = "")
            print()
        elif ji_xuan == "3":
            qing()
            shss_1 = input("\033[33m请输入算式(如：1*5+6/2-1):")
            try:
                print("\033[32m该算式的计算结果如下：")
                print(shss_1,"=",eval(shss_1))
                print("\033[36m递等式:敬请期待")
            except:
                print("\033[31m错误")
        elif ji_xuan == "4":
            qing()
            if vip >= 1:
                head = int(input("\033[32m请输入头数:"))
                feet = int(input("\033[34m请输入脚数:"))
                qing()
                rabbit = feet/2-head
                chicken = head-rabbit
                print("\033[35m运算过程正在维护...")
                print("\033[36m运算结果:鸡有",chicken,"只，兔有",rabbit,"只")
            else:
                baovip(3)
        elif ji_xuan == "5":
            qing()
            pl = []
            qpjsgs = int(input("\033[33m请输入数的个数：\033[32m"))
            for i in range(qpjsgs):
                str1 = '第' +str(i+1)+'个数是:'
                p = int(input(str1))
                pl.append(p)
                qing()
            qing()
            psum = sum(pl)
            pa = psum/qpjsgs
            print("\033[34m平均数是：",pa)
        elif ji_xuan == "6":
            qing()
            a = int(input('\033[33m请输入今年的年份:'))
            qing()
            if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
                print('\033[32m这年是：闰年')
            else:
                print('\033[34m这年是：平年')
        elif ji_xuan == "7":
            qing()
            if vip >= 1:
                print("\033[36m基本格式:如2020-01-01")
                date1 = input("\033[32m输入第一个日期(格式见上):")
                date2 = input("\033[34m输入第二个日期(格式见上):")
                try:
                    days = date_diff(date1,date2)
                    print("\033[93m答案是:"+str(days)+"天。\033[0m")
                except:
                    print("\033[91m格式错误或系统错误，运算失败\033[0m")
            else:
                baovip(3)
        elif ji_xuan == "8":#面积
            qing()
            pfm = int(input("\033[36m请输入平方米:"))
            yic = pfm * 10.7639104
            print("\033[32m转换结果:"+str(pfm)+"平方米="+str(yic)+"平方英尺")
        elif ji_xuan == "9":#长度
            qing()
            print("\033[33m1=厘米(cm)>英寸(inch)")
            print("\033[32m2=厘米(cm)>米(m)")
            print("\033[34m3=厘米(cm)>分米(dm)")
            print("\033[35m4=厘米(cm)>千米(km)")
            print("\033[36m5=厘米(cm)>光年(ly)")
            mode = input("\033[31m>>>")
            qing()
            if mode == "1":
                cm = int(input("\033[36m请输入厘米:"))
                ans = cm * 0.3937008
                print("\033[32m转换结果:"+str(cm)+"厘米="+str(ans)+"英寸")
            elif mode == "2":
                cm = int(input("\033[36m请输入厘米:"))
                ans = cm / 100
                print("\033[32m转换结果:"+str(cm)+"厘米="+str(ans)+"米")
            elif mode == "3":
                cm = int(input("\033[36m请输入厘米:"))
                ans = cm / 10
                print("\033[32m转换结果:"+str(cm)+"厘米="+str(ans)+"分米")
            elif mode == "4":
                cm = int(input("\033[36m请输入厘米:"))
                ans = cm / 100000
                print("\033[32m转换结果:"+str(cm)+"厘米="+str(ans)+"千米")
            elif mode == "5":
                print("\033[31m距离过长，敬请期待！")
                
        elif ji_xuan == "10":#货币
            qing()
            print("\033[33m1=人民币>欧元")
            print("\033[32m2=人民币>日元")
            print("\033[34m3=人民币>美元")
            print("\033[35m4=人民币>韩元")
            mode = input("\033[31m>>>")
            qing()
            if mode == "1":
                q = int(input("\033[36m请输入人民币:"))
                a = q * 0.1318
                print("\033[32m转换结果:"+str(q)+"人民币="+str(a)+"欧元")
            elif mode == "2":
                q = int(input("\033[36m请输入人民币:"))
                a = q * 15.6430
                print("\033[32m转换结果:"+str(q)+"人民币="+str(a)+"日元")
            elif mode == "3":
                q = int(input("\033[36m请输入人民币:"))
                a = q * 0.1410
                print("\033[32m转换结果:"+str(q)+"人民币="+str(a)+"美元")
            elif mode == "4":
                q = int(input("\033[36m请输入人民币:"))
                a = q * 176.8076
                print("\033[32m转换结果:"+str(q)+"人民币="+str(a)+"韩元")
            else:
                print("\033[31m暂时没有这个单位~")
        input("\033[33mEnter键返回桌面。")
    elif software == "3":
        print("欢迎来到版本转换，目前为Beta公测版本，如有Bug及时反馈~")
        system=int(input("选择系统版本\n1=简易模式 2=退出"))
        if system==1 and easyjy==0:
            print("好的，正在切换......")
            sleep(3)
            qing()
            easy()
    elif software == "4":
        print("\033[32m+===============欢迎使用Segoe智能电脑性能测试机===============+")
        input("\033[36m                      Enter键开始测试。             ")
        qing()
        print("\033[33m延时:测试中...")
        print("\033[36m登录:等待中...")
        print("\033[34m版本:等待中...")
        print("\033[35m更多:敬请期待")
        #测延时
        t1_c = time()
        sleep(1)
        t2_c = time()
        t_c = t2_c - t1_c
        if t_c > 1:
            t_c2 = t_c - 1
            if t_c2 > 0.21:
                yanshi = str(t_c2)+"秒，您的延时无敌长，说明网络无敌差，建议您进行小孙网络诊断(未开发,敬请期待)。"
            elif t_c2 > 0.12:
                yanshi = str(t_c2)+"秒，您的延时极长，说明网络超级差。"
            elif t_c2 > 0.01:
                yanshi = str(t_c2)+"秒，您的延时较长，说明网络有点差。"
            elif t_c2 > 0.004:
                yanshi = str(t_c2)+"秒，您的延时有一点点长，可能是卡顿问题，此为正常~"
            elif t_c2 <= 0.002:
                yanshi = str(t_c2)+"秒，您的延时非常正常，继续保持哦~"
            else:
                yanshi = str(t_c2)+"秒，AI智能分析出错！！"
        elif t_c == 1:
            yanshi = "太棒啦，您的电脑没有延时~"
        elif t_c < 1:
            yanshi = "您的电脑太快啦，比小孙系统运行速度还快，快了 -- 秒。"
        else:
            yanshi = "fail(测试失败)"
        #测登录
        qing()
        print("\033[33m延时:测试完成")
        print("\033[36m登录:测试中...")
        print("\033[34m版本:等待中...")
        print("\033[35m更多:敬请期待\033[8m")
        if register==1:
            tryy = "您已创建账号并登录"
        else:
            tryy = "您没有账号或没有登录"
        #测更新
        qing()
        print("\033[0m\033[33m延时:测试完成")
        print("\033[36m登录:测试完成")
        print("\033[34m版本:测试中...")
        print("\033[35m更多:敬请期待\033[0m")
        ce3 = "Segoe版本:最新！ python编译器版本:{} 您的系统:位数{}".format(sys.version[0:5],platform.architecture()[0])
        sleep(2)
        qing()
        print("\033[33m延时:测试完成")
        print("\033[36m登录:测试完成")
        print("\033[34m版本:测试完成")
        print("\033[35m更多:敬请期待\033[0m")
        sleep(0.1)
        qing()
        print("\033[32m测试结果:")
        print("\033[36m延时:",yanshi)
        print("\033[36m登录:",tryy)
        print("\033[34m版本:",ce3)
        print("\033[35m此测试数据绝对准确。")
        input("\033[31mEnter键返回桌面")
    elif software == "5":
        qing()
        print("\033[33m+=================有道翻译官=================+")
        print("\033[32m此翻译机可以 中 > 英   英 > 中   日 > 中   韩 > 中")
        print("\033[34m             输入中文  输入英文  输入日文  输入韩文")
        input("\033[36m+=================回车键开始=================+")
        qing()
        content = str(input('\033[33m请输入你要翻译的内容：'))
        data = {'doctype':'json','type':'AUTO','i':content}
        url = "http://fanyi.youdao.com/translate"
        r = requests.get(url,params=data)
        result = r.json()
        target = result['translateResult'][0][0]["tgt"]
        print("\033[36m翻译结果："+target)
        input("\033[32mEnter键结束。")
    elif software == "6":
        if vip >= 1:
            while True:
                qing()
                print("\033[?25h\033[32m欢迎使用记事本!\033[34m输入已有记事本打开,\033[33m输入新名字即可新建,\033[31m输入exit退出,\033[35m输入recycle查看回收站")
                print("\033[33m已有记事本:\033[0m")
                for i in jsb:
                    print(i)
                j=input("\033[36m输入记事本名:")
                qing()
                if j.lower()=='exit':
                    break
                elif j.lower()=='recovery':
                    print("\033[36m| Segoe Recovered files\033[32m")
                    for i in jsbrc:
                        print("\033[32m记事本名称 : "+str(i))
                        print("\033[33m记事本内容 : 见下行\n"+str(jsbrc[i]))
                        print()
                    input("\033[36m（recovery内容无法恢复，只支持临时查看，文章中\033[34m\\n\033[36m代表换行；回车键返回。）")  
                elif j.lower()=='recycle':
                    print("\033[36m| 记事本回收站\033[32m")
                    for i in jsbr:
                        print(i)
                    cao = input("\033[36m输入要执行的操作(1=恢复 2=彻底删除 3=全部彻底删除 4=全部恢复)：")
                    if cao != '3' and cao != '4':
                        jj = input("\033[33m输入要操作的记事本名：")
                    if cao == '1':
                        if jj in jsbr:
                            jsb[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m恢复成功！")
                        else:
                            print("\033[31m记事本名输入错误")
                    elif cao == '2':
                        if jj in jsbr:
                            jsbrc[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m彻底删除成功！")
                        else:
                            print("\033[31m记事本名输入错误")
                    elif cao == '3':
                        for i in jsbr:
                            jsbrc[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在抹掉......")
                        sleep(0.5)
                        print("\033[32m删除成功！")
                    elif cao == '4':
                        for i in jsbr:
                            jsb[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在恢复......")
                        sleep(0.5)
                        print("\033[32m恢复成功！")
                    else:
                        print("\033[31m无效操作")
                    input("\033[35mEnter键返回")
                elif j in jsb:
                    print(jsb[j])
                    print("\033[33m1.更改 \033[31m2.删除 \033[34m3.重命名 \033[31m其他退出")
                    c=input("\033[0m请选择：")
                    if c=='1':
                        qing()
                        nr = ''
                        print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                        while True:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                qing()
                                print("\033[32m输入更改后的内容，输入esc完成，输入clear清空所有内容。\033[33m")
                                continue
                            elif '<fontcolor='in a:
                                if len(a) < 12:
                                    print("\033[31m语法错误：<fontcolor=  value error:is no color input\033[33m")
                                    continue
                                if a[11] == '红':
                                    nr = nr + '\033[31m'
                                elif a[11] == '绿':
                                    nr = nr + '\033[32m'
                                elif a[11] == '黄':
                                    nr = nr + '\033[33m'
                                elif a[11] == '蓝':
                                    nr = nr + '\033[34m'
                                elif a[11] == '紫':
                                    nr = nr + '\033[35m'
                                elif a[11] == '青':
                                    nr = nr + '\033[36m'
                                text = a + '\n'
                                nr = nr + text
                            else:
                                text = a + "\n"
                                nr = nr + text
                        jsb[j]=nr
                        print("\033[32m更改成功!")
                    elif c=='2':
                        jsbr[j] = jsb[j]
                        del jsb[j]
                        print("\033[32m删除成功，可在回收站查看!")
                    elif c=='3':
                        new=input("\033[36m输入新记事本名:")
                        if new=='exit':
                            print("\033[31m不可使用关键词exit命名记事本!")
                            sleep(2)
                            continue
                        jsb[new] = jsb[j]
                        del jsb[j]
                        print("\033[32m更改成功!")
                    else:
                        continue
                    sleep(2)
                else:
                    nr = ''
                    print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                    while True:
                        a = input()
                        if a == 'esc':
                            break
                        elif a == 'clear':
                            nr = ''
                            qing()
                            print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                            continue
                        elif '<fontcolor='in a:
                            if len(a) < 12:
                                print("\033[31m语法错误：<fontcolor=  value error:is no color input\033[33m")
                                continue
                            if a[11] == '红':
                                nr = nr + '\033[31m'
                            elif a[11] == '绿':
                                nr = nr + '\033[32m'
                            elif a[11] == '黄':
                                nr = nr + '\033[33m'
                            elif a[11] == '蓝':
                                nr = nr + '\033[34m'
                            elif a[11] == '紫':
                                nr = nr + '\033[35m'
                            elif a[11] == '青':
                                nr = nr + '\033[36m'
                            text = a + '\n'
                            nr = nr + text
                        else:
                            text = a + "\n"
                            nr = nr + text
                    jsb[j]=nr
                    print("新建成功!")
                    sleep(2)
            print("\033[?25l")
        else:
            baovip(4)
    elif software == "7":
        qing()
        print("\033[32m  - Segoe OS Music - ")
        print()
        spt2("\033[33m______________________",0.05)
        qing()
        while True:
            qing()
            print("\033[34m")
            qing()
            dlp("\033[32m+==============欢迎使用Segoe音乐==============+\n")
            gel = ["baba","try again","lala","lulu","oh no","goodbye"]
            dlp("\033[36m请问你想要听什么歌\033[33m(1=退出)\033[36m:\033[35m")
            ge = input()
            qing()
            if ge == "1":
                break
            else:
                print("\033[33m正在搜索\""+ge+"\"...")
                spt("--------------\n")
                qing()
                if ge in gel:
                    print("\033[32m好的，现在就为您播放\""+ge+"\"\033[33m")
                    sleep(0.5)
                    qing()
                    ge2 = ge+".mp3"
                    qing()
                    if ge == "baba":
                        print("\033[31m",end='')
                    elif ge == "try again":
                        print("\033[33m",end='')
                    elif ge == "lala":
                        print("\033[36m",end='')
                    elif ge == "lulu":
                        print("\033[32m",end='')
                    elif ge == "oh no":
                        print("\033[31m",end='')
                    elif ge == "goodbye":
                        print("\033[35m",end='')
                    else:
                        print("\033[33m",end='')
                    if ge != "lala" and ge != "goodbye":
                        print("      □      ")
                        print(ge+"(网络歌手)")
                        print("免费 音效on 视频off")
                        print("  ←    ||    →  ")
                        print("                  ")
                        print("○    ↓    ❤   ···")
                        print("====================\033[8m")
                        play_mp3(ge2)
                        print("\033[0m")
                    else:
                        if vip >= 1:
                            print("      □      ")
                            print(ge+"(网络歌手)")
                            print("VIP专享 音效on")
                            print("  ←    ||    →  ")
                            print("                  ")
                            print("○    ↓    ❤   ···")
                            print("====================\033[8m")
                            play_mp3(ge2)
                            print("\033[0m")
                        else:
                            print("\033[31m抱歉，此歌曲为VIP专享(此应用不更新vip券)。您可以尝试包VIP或者用300金币购买小孙音乐专辑。")
                            sleep(2)
                else:
                    print("\033[31m对不起，搜索不到你说的歌曲。")
                    sleep(2)
    elif software == "8":
        print("1.石头剪刀布")
        print("2.一颗雷大战")
        print("3.猜数字")
        game=int(input())
        if game==1:
            num = 1
            yin_num = 0
            shu_num = 0
            while num <= 3:
                if shu_num == 2 or yin_num == 2:
                    break
                user = int(input('请出拳 0（石头） 1（剪刀） 2（布）'))
                if user > 2:
                    print('不能出大于2的值')
                else:
                    data = ['石头', '剪刀', '布']
                    com = random.randint(0, 2)
                    print("您出的是{}，电脑出的是{}".format(data[user], data[com]))
                    if user == com:
                        print('平局')
                        continue
                    elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
                        print('你赢了')
                        yin_num += 1
                    else:
                        print('你输了')
                        shu_num += 1
                num += 1
        elif game==2:
            bomb = random.randint(1, 99)
            print(bomb)
            start = 0
            end = 99
            while 1:
                people = int(input('请输入{}到{}之间的数(不玩了输-1):'.format(start, end)))
                if people > bomb:
                    print('大了')
                    end = people
                elif people < bomb:
                    print('小了')
                    start = people
                elif people==-1:
                    print("欢迎下次再玩！")
                    break
                else:
                    print('BOOM!!!')
                    break
                print('等待电脑了输入{}到{}之间的数:'.format(start, end))
                time.sleep(1)
                com = random.randint(start + 1, end - 1)
                print('电脑输入：{}'.format(com))
                if com > bomb:
                    print('大了')
                    end = com
                elif com < bomb:
                    print('小了')
                    start = com
                else:
                    print('BOOM!!!')
                    break
        elif game==3:
            _=randint(0,99)
            __=-1
            #下划线变量法，我猜别人都用不到吧
            while __!=_:
                __=int(input("从0~99，输入一个数(不玩了按-1)"))
                if __>_:
                    print("大了")
                elif __<_:
                    print("小了")
                elif __==-1:
                    __=_
                    print("欢迎下次光临")
                else:
                    print("对了")
                    
    elif software == "9":
        print("正在进行体检，这大概需要1~2分钟，你可以先休息，等检测好我们会语音通报给你。")
        sleep(5)
        qing()
        print("检测中......")
        sleep(2)
        qing()
        print("检测账号是否安全...")
        sleep(3)
        print("检测账号是否安全...账号安全")
        print("检测插件是否有效...")
        sleep(30)
        qing()
        print("检测账号是否安全...账号安全")
        print("检测插件是否有效...插件有效，无错误关联")
        print("检测快捷方式是否全部有效...")
        sleep(15)
        print("检测账号是否安全...账号安全")
        print("检测插件是否有效...插件有效，无错误关联")
        print("检测快捷方式是否全部有效...全部有效")
        speak("检测完成，你的电脑存在很健康")  
    elif software == "10":
        if JI_HUO==0:
            print("\033[91m您未激活Sogoe,无法使用该程序")
        else:
            print("    \033[41m  \033[42m  \033[0m")
            print("    \033[44m  \033[43m  ")
            spt("\033[92m    欢迎使用")
            sleep(1)
            print("©Copyright 2019-2020 月高工作室")
            sleep(3)
            qing()
            for i in range(30):
                print("\033[94m欢迎")
                sleep(0.05)
                qing()
                print("\033[0m欢迎")
                sleep(0.05)
                qing()
            play_mp3("baba.mp3")
            while 1:
                print(ctime)
                print("0.退出系统")
                print("1.命令提示符")
                print("2.系统属性")
                print("3.时间")
                print("4.屏保")
                print("5.护眼模式")
                print("6.点我！1分钟赚500金币")
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
                    print("Virtual PC 1.0")
                    print("版权所有©2019-2020 HOTM workshop,保留所有权利。")
                    print("Service Pack 0.9.1")
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
                elif prog==6:
                    for i in range(61):
                        gc=gc+9
                        sleep(1)
                    print("500金币已到账！")
                else:
                    print("程序不存在")
                sleep(6.5)
                qing()
                continue
    elif software == "11":
        print("正在关机......")
        sleep(3)
        shutdown()
    elif software == "12":
        for j in range(5):
            for i in range(13):
                print("❎ 滚回到以前的版本")
                print("抱歉你的bugOS 2020要滚回Pan 81 Pro了")
                sleep(2)
            print("⚠️访问人员过多，服务器超载，暂时停用Sogoe。")
            sleep(5)
        qing()
        for i in range(6):
            print("⚠️电池电量低\n还剩20%电量")
            sleep(3)
        print("❎ 您的系统不支持运行SogoeOS")
        print("您的系统(WindowsXP)配置过低，请升级至Win7再尝试运行")
        sleep(6)
        qing()
        for i in range(5):
            print(r"❎ Error:注册表第4856项in Sogoe_User\Login\Safe 无效的注册表项")
            sleep(5)
            print("?已修复注册项，重启将生效(可能会把默认语言改成English)")
            sleep(6)
        qing()
        computerfailure("CrazyError超负荷运载导致系统崩溃")
    elif software == "13":
        jifen = 0
        while True:
            qing()
            print("\033[33m你现在有"+str(jifen)+"分。")
            print("\033[33m1=任务清单    \033[32m2=换礼品    \033[36m3=导入   \033[31m4=退出此模式")
            Vmos = input("\033[34m请选择：")
            if Vmos == "1":
                qing()
                print("\033[33m1=练琴(15分钟以上：2积分；练足40分钟：10积分)\n\033[32m2=跳绳(每跳足200个：2积分；累计1000个：20积分)\n\033[31m3=炒菜(5积分/道)\n\033[34m4=拖地(5积分)\n\033[32m5=阅读(超过30分钟：5积分)\n\033[36m6=英语阅读(15分钟：10积分)\n\033[31m7=考试分数90分以上(10积分/次)\n\033[33m妈妈注：宝贝，加油 ヾ(◍°∇°◍)ﾉﾞ")
                print("\033[32m(☆每120积分换一个神秘大礼)")
                Vxuan = input("\033[0m请选择：")
                qing()
                zhix = input("\033[33m请问这个任务你执行好了吗(yes/no):")
                if zhix == "yes":
                    print("\033[36m请认真核对表格，待会儿告诉我加几积分。")
                    sleep(1)
                    print("\033[33m1=练琴(15分钟以上：2积分；练足40分钟：10积分)\n\033[32m2=跳绳(每跳足200个：2积分；累计1000个：20积分)\n\033[31m3=炒菜(5积分/道)\n\033[34m4=拖地(5积分)\n\033[32m5=阅读(超过30分钟：5积分)\n\033[36m6=英语阅读(15分钟：10积分)\n\033[31m7=考试分数90分以上(10积分/次)\n\033[33m妈妈注：宝贝，加油 ヾ(◍°∇°◍)ﾉﾞ")
                    sleep(2)
                    jia = int(input("\033[33m加几分(说实话)？"))
                    jifen = jifen + jia
                    print("成功了~")
                    sleep(1)
                else:
                    print("那就赶快去执行！")
                    sleep(1.5)
            elif Vmos == "2":
                qing()
                print("""
\033[32m______________\033[34m      ______________ \033[36m      _____________
\033[32m|            |\033[34m      |             |\033[36m     |             |
\033[32m|            |\033[34m      |             |\033[36m     |             |
\033[32m|      ？    |\033[34m      |   HUAWEI    |\033[36m     |    deli     |
\033[32m|            |\033[34m      |             |\033[36m     |             |
\033[32m|____________|\033[34m      |_____________|\033[36m     |_____________|
\033[32m 1=神秘礼物   \033[34m     2=华为Mate30(5G)\033[36m        3=文具套装
\033[32m   120￥      \033[34m         1999￥      \033[36m        999￥""")
                liwu = input("\033[33m你要换第几个礼物？")
                if liwu == "1":
                    if jifen >= 120:
                        mama = ["A","C","G","H","E","Z","B","X","N"]
                        ma1 = random.choice(mama)
                        ma2 = random.randint(100000,999999)
                        ma  = ma1+str(ma2)
                        print()
                        print("\033[34m兑换成功，请到妈妈那里审核。")
                        print("\033[36m礼物名：普通型神秘礼物")
                        print("\033[32m价格：120￥")
                        print("\033[33m成功码："+ma)
                        jifen = jifen - 120
                        sleep(2)
                        input("\033[32mEnter键完成：")
                    else:
                        print("\033[31m您的钱不足，无法购买！")
                        sleep(1.5)
                elif liwu == "2":
                    if jifen >= 1999:
                        mama = ["A","C","G","H","E","Z","B","X","N"]
                        ma1 = random.choice(mama)
                        ma2 = random.randint(100000,999999)
                        ma  = ma1+str(ma2) 
                        print()
                        print("\033[34m兑换成功，请到妈妈那里审核。")
                        print("\033[36m礼物名：华为Mate30(5G)手机一个")
                        print("\033[32m价格：1999￥")
                        print("\033[33m成功码："+ma)
                        jifen = jifen - 1999
                        sleep(2)
                        input("\033[32mEnter键完成：")
                    else:
                        print("\033[31m您的钱不足，无法购买！")
                        sleep(1.5)
                elif liwu == "3":
                    if jifen >= 999:
                        mama = ["A","C","G","H","E","Z","B","X","N"]
                        ma1 = random.choice(mama)
                        ma2 = random.randint(100000,999999)
                        ma  = ma1+str(ma2) 
                        print()
                        print("\033[34m兑换成功，请到妈妈那里审核。")
                        print("\033[36m礼物名：文具套装")
                        print("\033[32m价格：999￥")
                        print("\033[33m成功码："+ma)
                        jifen = jifen - 999
                        sleep(2)
                        input("\033[32mEnter键完成：")
                    else:
                        print("\033[31m您的钱不足，无法购买！")
                        sleep(1.5)
                else:
                    print("\033[31m没有此礼品~")
                    sleep(1)
            elif Vmos == "3":
                qing()
                yiqian = int(input("\033[33m请问你以前一共赚了几积分(说实话)："))
                jifen = jifen + yiqian
                print("成功了！")
                sleep(1)
            else:
                break
    elif software == "14":
        print("1.查看时间 2.计时器 3.倒计时 4.设置闹钟")
        clockset=int(input("\n选择选项:"))
        if clockset==1:
            for i in range(11):
                print(ctime())
                sleep(1)
                qing()
        elif clockset==2:
            timeset=0
            input("Enter键开始:")
            qing()
            timeset=time()
            input("已开始计时，Enter键结束:")
            qing()
            timeset2=time()
            print("刚刚过去了"+str(timeset2-timeset)+"秒")
        elif clockset==3:
            sec=int(input("请问你要倒计时多长时间(单位:秒)"))
            input("Enter键开始倒计时")
            qing()
            while sec>0:
                sleep(1)
                sec=sec-1
            print("时间到！")
            speak("时间已到！")
        elif clockset==4:
            INtime=input("输入闹钟响应时间,比如07:00")
            qing()
            print("将在对应时间响应闹钟，请不要关闭机器或退出程序，在闹钟响应前会一直处于休眠模式")
            qing()
            while strftime("%H:%M")!=INtime:
                sleep(1)
            print("闹钟响应！")
            speak("闹钟已响应！")
        else:
            print("选项不存在")
    elif software == "15":
        phone = input("\033[32m请输入手机号码[真的可以发到手机里，建议不要输入陌生号码]:")
        if len(phone) < 5:
            system("clear")
            print("请输入正确的手机号码!")
            sleep(1)
            system("clear")
        conten = input("请输入发送内容[Enter发送]:")
        send_msg(int(phone),conten)
        print("发送成功\033[42m ✔ \033[0m")
    elif software == "16":
        texiao=int(input("1.下划线特效 2.斜体特效 3.斜体下划线特效 4.关闭特效\n输入你想要的特效"))
        if texiao==1:
            print("\033[4m下划线特效已开启:)")
        elif texiao==2:
            print("\033[3m斜体特效已开启[滑稽]")
        elif texiao==3:
            print("\033[3m\033[4m斜体下划线特效已开启?")
        elif texiao==4:
            print("\033[0m特效已关闭;-)")
        else:
            print("特效不存在")
    elif software == "17":
        dh("     \033[0mS")
        dh("     \033[0m\033[2mS")
        dh("     \033[41m  \033[42m  \033[0m\n     \033[44m  \033[43m  \033[0m")
        sleep(1)
        dh("   \033[41m  \033[42m  \033[0m\n \033[44m  \033[43m  \033[0m")
        dh("  \033[41m  \033[42m  \033[0m\n \033[44m  \033[43m  \033[0m")
        dh(" \033[41m  \033[42m  \033[0m\n \033[44m  \033[43m  \033[0m")
        dh("\033[41m  \033[42m  \033[0m\n \033[44m  \033[43m  \033[0m")
        dh("\033[41m  \033[42m  \033[0m\n\033[44m  \033[43m  \033[0m\033[2mSogoeOS 2020")
        dh("\033[41m  \033[42m  \033[0m\n\033[44m  \033[43m  \033[0mSogoeOS 2020")
        sleep(10)
    elif software == "18":
        try:
            spt("1.导航 2.AQI空气质量检测 3.天气预报 ")
            sleep(1)
            spt("请问您需要什么？")
            ans=int(input(""))
            if ans==1:        
                start=input("起点：")
                end=input("终点：")
                city=input("所在城市：")
                route_list=get_routes(start,end,city)
                len1=len(route_list)
                if len1>0:
                    for i in range(len1):
                        print(i+1,":",route_list[i])
                        sleep(1)
                    spt("请选择要搭乘的路线：")
                    print()
                    num=input("")
                    qing()
                    scale=15
                    for i in range(scale+1):
                        aaa = '*'*i
                        bbb = '.'*(scale-i)
                        ccc =(i/scale)*100
                        print("\r\033[1;32m{:^3.0f}%[{}->{}]".format(ccc,aaa,bbb),end='')
                        sleep(0.6)
                    qing()
                    num=int(num)
                    num=num-1
                    bus_list=get_sites(route_list,num)
                    len2=len(bus_list)
                    spt("\033[36m途径以下站点：")
                    for i in range(len2):
                        print(i+1,":",bus_list[i])
                        sleep(1)
                    sleep(15)
                    qing()
                else:
                    spt("您已在目的地附近!")
                    qing()
            if ans==2:
                city = input("请输入城市名:")
                if len(city) > 1:
                    pollution = AQI(city)
                    print(pollution)
                else:
                    print("输入错误")
                if pollution < 50:
                    print("你可以出去了")
                elif pollution < 100:
                    print("如果你对空气质量敏感，请呆在家里")
                elif pollution < 150:
                    print("劝告家里老人和小孩不要出去")
                elif pollution < 200:
                    print("是人就别出去")
                elif pollutoin < 300:
                    print("呆在家里吧，外面空气质量炒鸡辣鸡")
                else:
                    print("注意城市的空气质量,减少污染")
                    sleep(5)
                qing()
            if ans==3:
                area = input("请问你要查询的地区是：")
                temp1 = air_temp(area,1)
                speed1 = air_speed(area,1)
                print("温度：",temp1,"℃\n    风速",speed1,"米/秒")
        except:
            print("世界上最遥远的距离就是没网。\033[94m检查设置")
    else:
        print("\033[34m○ 正在查找应用:{}".format(software))
        sleep(0.5)
        qing()
        print()
        print()
        print("\033[33m系统未查找到软件 - {} -".format(software))
        print("\033[36m原因智能分析中...")
        sleep(0.7)
        #智能辨别
        software_len = len(software)
        NUMBER = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
        try:
            software2 = int(software)
            YUAN = "您输入了不合法的编号，请您输入正确编号~"
        except:
            if software == "" or software == " " or software == " "*software_len:
                YUAN = "您什么也没输入哟~"
            elif software in NUMBER:
                YUAN = "请输入阿拉伯数字,不可输入汉字~"
            elif software[0:3] == "www" or software[0:4] == "http":
                YUAN = "不支持输入网址~"
            else:
                YUAN = "您输入了程序名,请输入编号~"
        qing()
        print()
        print()
        print("\033[33m系统未查找到软件 - {} -".format(software))
        print("\033[36m原因:{}".format(YUAN))
        sleep(0.5)
        input("\033[32mEnter键返回桌面。")
        qing()
        continue
    sleep(10)
    qing()
    continue