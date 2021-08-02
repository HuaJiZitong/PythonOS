from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*
import platform
import requests
import urllib.request
import json,requests,re,sys
from random import*
from time import*
from os import*
from xes.ext import*
from xes.AIspeak import*
import json,requests,re,sys
import urllib.request
import re 
from socket import*
from email.mime.text import MIMEText
from random import*
import smtplib
import requests
import urllib.request ,re,os
import webbrowser

qhqd=0
goto=0
def dt():#此作品为彩虹花·石悠悦创作，禁止借鉴
    start=input("\033[33m起点\033[31m(只限城内导航！例：中亭街-五一广场) ")
    end=input("\033[36m终点 ")
    city=input("\033[32m所在城市(例：上海市)")
    route_list=get_routes(start,end,city)
    len1=len(route_list)
    if len1>0:
        for i in range(len1):
            print(i+1,":",route_list[i])
            sleep(1)
            b("请选择要搭乘的路线：")
            print()
            num=input("")
            system("clear")
            scale=15
            for i in range(scale+1):
                aaa = '*'*i
                bbb = '.'*(scale-i)#特别鸣谢：蔡昊轩
                ccc =(i/scale)*100
                print("\r\033[1;32m{:^3.0f}%[{}->{}]".format(ccc,aaa,bbb),end='')
                sleep(0.6)
                system("clear")
                num=int(num)#算法提供方:PanTSE2 原作者:蔡昊轩
                num=num-1
                bus_list=get_sites(route_list,num)
                len2=len(bus_list)
                a("\033[36m途径以下站点：")
                for i in range(len2):
                    print(i+1,":",bus_list[i])
                    sleep(1)
                sleep(15)
                system("clear")
    else:
        b("您已在目的地附近!")
        system("clear")
#声明：你打开了这个作品，请不要抄袭！
#声明：这里有我们的水印。律师函已经准备好了
#声明：如果你抄袭并发布了，我们会全网通缉你抄袭！
def tq():
    city = input("\033[36m请输入你想搜索天气的城市(例：北京市)")
    now=air_temp(city,i)
    if now >= 35:
        v="你的城市快变成一个大烤炉啦"
    if now >= 25 and now <35:
        v="温度宜人，可以出行"
    if now >= 15 and now < 25:
        v="温度有点低呀，是不是冬天快到了"
    if now >= 5 and now < 15:
        v="啊啊啊好冷啊，赶快披上棉袄"
    if now < 5:
        v="恭喜！你可以堆雪人了"
    print("您查询到的温度为:"+str(now)+"℃ "+v)#如果直接打印now会蓝屏
def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)#新的逐字输出

def q():
    system("clear")#一个一个打system("clear")真tm烦

def qing():
    system("clear")#运行某些特定的程序蓝屏了，才发现是qing函数不存在
    
def bsod():
    print("\033[0m\033[44m")
    q()
    print("A problem has been detected and Pan had been shutdown to prevent damage to your computer.")
    print("If this is the first time you've seen this stop error screen,restart your computer.If this screen appears again,follow these steps:")
    print("To check your broswer have or not supports Pan,you can test baidu.com to test your broswer have or not supports.")
    print("If problem continue,to check out your computer system version whether is XP or lower system.")
    print("If version is XP or lower,please create a virtual Win7 PC to run Pan.")
    print("If problem continue,try to check out the hardware in your computer or change a new computer.")
    print("Press run to continue...\033[8m")#蓝屏死机错误

try:
    print("\033[?25l石悠悦X潘夕习")
    b("\033[93m欢迎来到磐石系统！\033[92m")#Pan系统代号石头，以前Beta版叫Pan Stone
    sleep(2)
    q()
    for i in range(randint(2,6)):
        for j in range(10):
            print("  "*j+"|||")
            print("©HOTM and Oranges Workshop")
            sleep(0.1)
            q()
        q()
    sleep(3)
    q()
    print("\033[94m请先登录账号")
    user=input("\033[0m昵称:\033[?25h")
    word=None
    word=input("密码:")
    q()
    password_yz=None
    password_yz=input("请再次输入您的密码:")
    while password_yz!=word:
        password_yz=input("\033[91m密码错误，请输入您的密码:")
    print("\033[92mo 欢迎\033[?25l")
    #变量
    jsb={}
    sleep(2)
    q()
    while 1:
        if goto==0:
            print("\033[0m开始                "+user)
            print("系统功能")
            print("\033[30m0.关机 \033[90m1.待机 \033[31m2.命令提示符 \033[91m3.忘记密码 \033[32m4.检测更新\n\033[92m5.我的电脑")
            print("\033[0m效率")
            print("\033[33m6.万能数学计算器 \033[93m7.闹钟 \033[34m8.信息 \033[94m9.天气 \033[35m10.记事本 \033[95m11.地图")
            print("\033[0m生活")
            print("\033[36m12.社区浏览器 \033[96m13.虚拟机2021")#基本功能
            print("\033[93m\n\n"+strftime("%H:%M,",localtime())+strftime("%Y/%m/%d", localtime())+"\n输入程序序号")
            print("\033[1;36m┌──────────┐")
            print("\033[1;33m│          │")
            print("\033[1;36m└──────────┘")
            print("\033[1;33m    ")
            prog=input("\033[3A\033[1C")#适配搜索框(祖传prog变量)
            q()
        else:
            print(user+"您好，程序正在为您切换您输入的程序...")
            if chqh=="1":
                prog="2"
            else:
                prog="6"
            sleep(3)
            goto=0
            q()
        if prog=="0":
            for i in range(5):
                print("\033[0mo 正在关机")
                sleep(0.2)
                system("clear")
                print("\033[94mo 正在关机")
                sleep(0.2)
                system("clear")
            sleep(1)
            qing()
            print("\033[92m现在你可以安全地关闭你的电脑了\033[8m")
            break
        elif prog=="1":
            print("\033[0m电脑正在休眠，按Enter键结束")
            sleep(2)
            system("clear")
            print("\033[90m电脑正在休眠，按Enter键结束")
            sleep(0.5)
            qing()
            input()
            password_yz=input("请输入您的密码以登录:")
            while password_yz!=word:
                password_yz=input("\033[91m密码错误，请输入您的密码:")
            print("\033[94mo 欢迎"+name)
        elif prog=="2":
            print("\033[0mHOTM Pan[版本3.65.3895]")
            print("版权所有 (c) 2021 HOTM and Oranges Workshop。保留所有权利。")
            while 1:
                print("C:\\"+user+">",end="")
                dos=input()
                if dos=="help":
                    print("有关某个命令的详细信息，请键入help命令名")
                    print("break    退出cmd程序，这与exit是一样的")
                    print("clear    清屏")
                    print("cmd      打开一个新的Pan命令解释窗口")
                    print("exit     退出cmd程序")
                    print("help     提供Pan的所有命令代码信息")
                    print("panver   查看Pan的版本")
                    print("bsod     自动蓝屏")
                    print("shutdown 关机")
                    print("modify   修改账号")
                elif dos=="clear":
                    q()
                elif dos=="cmd":
                    print("HOTM Pan[版本3.65.3895]")
                    print("版权所有 (c) 2021 HOTM and Oranges Workshop。保留所有权利。。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3895]")
                elif dos=="bsod" or dos=="shutdown":
                    break
                elif dos=="modify":
                    user=input("新用户名:")
                    password=input("新密码:")
                    print("修改成功!")
                else:
                    print("\""+dos+"\"不是一个命令代码，请检查拼写。")
            if dos=="bsod":
                q()
                bsod()
                break
            elif dos=="shutdown":
                for i in range(5):
                    print("\033[0mo 正在关机")
                    sleep(0.2)
                    system("clear")
                    print("\033[94mo 正在关机")
                    sleep(0.2)
                    system("clear")
                sleep(1)
                qing()
                print("\033[92m现在你可以安全地关闭你的电脑了\033[8m")
                break
        elif prog=="3":
            phone = input("\033[32m请输入手机号码[真的可以发到手机里，建议不要输入陌生号码]:")
            if len(phone) < 5:
                system("clear")
                print("请输入正确的手机号码!")
                sleep(1)
                system("clear")
            rd=randint(1000,9999)
            conten="【Pan系统】验证码"+rd+"，请勿泄露给他人"
            send_msg(int(phone),conten)
            yan=None
            while yan!=rd:
                yan=int(input("输入验证码:"))
            word=input("输入新密码:")
            q()
            password_yz=None
            password_yz=input("请再次输入您的密码:")
            while password_yz!=word:
                password_yz=input("\033[91m密码错误，请输入您的密码:")
            print("\033[92mo 欢迎\033[?25l")
        elif prog=="4":
            print("检测更新中...")
            sleep(2)
            q()
            print("检测更新中...")
            print("检测Pan内核...PanTSE1\033[91m最新版本\033[0m")
            sleep(2)
            q()
            print("检测更新中...")
            print("检测Pan内核...PanTSE2平板系统和Pan4.0个人电脑内核\033[91m最新版本\033[0m")
            print("检测Ashi内核...Ashi Windows 31终端版\033[91m最新版本\033[0m")
        elif prog=="5":
            print("\033[0mSystem(C:)\n4.00GB可用/16.00GB")
            print("\033[0mData(D:)\n3.00GB可用/8.00GB")
            print("\033[0mBored(B:)\n357KB可用/360KB")#B盘本身容量大小
            bc=randint(1,10)
            System32=input("请输入文件名(比如C:):")
            q()
            if System32=="C:":
                print("名称    修改日期        类型        大小")
                print(user+"   2020/5/24 15:01 文件夹      5.02GB")
                System32=input("请输入文件名(比如C:):")
                qing()
                if System32==user:
                    print("名称    修改日期        类型        大小")
                    print("桌面    2020/8/28 14:54 文件夹      50KB")
                    print("System  1987/3/19 2:11  文件夹      7.98GB") 
                    System32=input("请输入文件名(比如C:):")
                    q()
                    if System32=="桌面":
                        print("名称            修改日期        类型        大小")
                        print("programs.exe    2020/7/28 9:27  应用程序    50KB")
                    elif System32=="System":
                        print("名称            修改日期        类型         大小")
                        print("Pan.exe         2020/5/16 0:08  应用程序     3.98GB")
                        print("Ashi.exe        2020/7/30 21:50 应用程序     4.00GB")
                    else:
                        print("该文件不存在")
                else:
                    print("该文件不存在")
            elif System32=="D:":
                print("名称            修改日期        类型         大小")
                print("Pack.zip        2020/7/31 10:56 压缩文件夹   3.00GB")
                print("jsbda.cmd       2020/5/27 23:59 CMD命令      3KB")
                print("virtual.iso    2019/12/29 13:16 光盘镜像     1.98GB")
            elif System32=="B:" and bc!=5:
                for j in range(5):
                    for i in range(10):
                        print("❎ 滚回到以前的版本")
                        print("抱歉你的Bug Stone要滚回Pan 81 Pro了")
                        sleep(0.1)
                    print("⚠️ 访问人员过多，服务器超载，暂时停用Pan。")
                    sleep(5)
                qing()
                for i in range(6):
                    print("️? 电池电量低\n还剩20%电量")
                    sleep(3)
                print("❎ 您的系统不支持运行Pan")
                print("您的系统(WindowsXP)配置过低，请升级至Win7再尝试运行")
                sleep(6)
                qing()
                for i in range(5):
                    print(r"? Error:注册表第4856项in Pan_User\Login\Safe 无效的注册表项")
                    sleep(5)
                    print("✅  已修复注册项，重启将生效(可能会把默认语言改成美式英语)")
                    sleep(2)
                qing()
                bsod()
                break
            else:
                print("该磁盘不存在或已经拔出")
        elif prog=="6":
            qing()
            print("\033[002m\033[32m     ﹢﹣× ÷       ")
            print("\033[002m\033[34m欢迎使用万能计算器。")
            sleep(0.5)
            qing()
            print("\033[0m\033[32m     ﹢﹣× ÷       ")
            print("\033[34m欢迎使用万能计算器。")
            sleep(1)
            qing()
            print("\033[35m+===============磐石万能计算器===============+")
            print("\033[31m| 计算器系列")
            print("\033[36m1=普通计算器      ")
            print("\033[33m2=综合算式计算    ")
            print("\033[35m3=平均数计算      \033[36m5=平年闰年计算")#4这个数字不吉利，所以我没用了
            print("\033[32m6=日期间隔计算")
            print("\033[31m| 单位转换系列")
            print("\033[36m7=货币转换")
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
                shss_1 = input("\033[33m请输入算式(如：1*5+6/2-1):")
                try:
                    print("\033[32m该算式的计算结果如下：")
                    print(shss_1,"=",eval(shss_1))
                    print("\033[36m递等式:敬请期待")
                except:
                    print("\033[31m错误")
            elif ji_xuan == "3":
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
            elif ji_xuan == "5":
                qing()
                a = int(input('\033[33m请输入今年的年份:'))
                qing()
                if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
                    print('\033[32m这年是：闰年')
                else:
                    print('\033[34m这年是：平年')
            elif ji_xuan == "6":
                qing()
                print("\033[36m基本格式:如2020-01-01")
                date1 = input("\033[32m输入第一个日期(格式见上):")
                date2 = input("\033[34m输入第二个日期(格式见上):")
                try:
                    days = date_diff(date1,date2)
                    print("\033[93m答案是:"+str(days)+"天。\033[0m")
                except:
                    print("\033[91m格式错误或系统错误，运算失败\033[0m")
            elif ji_xuan == "7":#货币
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
            input("\033[33mEnter键返回开始菜单。")
        elif prog=="7":
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
        elif prog=="8":
            phone = input("\033[32m请输入手机号码[真的可以发到手机里，建议不要输入陌生号码]:")
            if len(phone)<5:
                system("clear")
                print("请输入正确的手机号码!")
                sleep(1)
                system("clear")
            conten = input("请输入发送内容[Enter发送]:")
            send_msg(int(phone),conten)
            print("发送成功\033[42m ✔ \033[0m")
        elif prog=='9':
            tq()
        elif prog=='10':
            print("\033[?25h\033[96m欢迎来到记事本!\033[91m输入exit退出，输入delete删除某个记事本,输入已有记事本名打开，输入新名字新建")
            print("已有记事本:",end="")
            for i in jsb:
                print(i,end="")
            j=input("\033[36m输入记事本名:")
            q()
            if j=="exit":
                print("\033[?25l")
                break
            elif j=="delete":
                print("已有记事本:",end="")
                for i in jsb:
                    print(i,end="")
                jj=input("\033[36m输入记事本名:")
                if jj in jsb:
                    del jsb[jj]
                    print("\033[32m删除成功！")
                else:
                    print("\033[31m记事本名输入错误")
            elif j in jsb:
                nr = ''
                if 1:#懒得解决缩进问题
                    if 1:
                        print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                        while 1:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                q()
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
            else:
                nr = ''
                if 1:
                    if 1:
                        print("\033[32m输入记事本内容，输入esc完成，输入clear清空所有内容。\033[33m")
                        while 1:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                q()
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
                            print("\033[32m新建成功!")
        elif prog=='11':
            dt()
        elif prog=='12':
            tm=time.strftime("%H:%M:%S", time.localtime())
            print("hi,",user,tm) 
            print("                   \033[36m社区 \033[31m浏览器")
            print("       \033[36m┌──────────────────────────────────┐")
            print("       \033[33m│                                 │")
            print("       \033[36m└──────────────────────────────────┘")
            print("")
            a=input("\033[5A\033[5C")
            print("\033[0m")
            if 1:
                if 1:
                    system("clear")
                    print(a+"_酷喵百科       dic.hotm.cn/\033[90mkumiao.url?wd="+a+"\033[0m\n");
                    print("————————————————————————————————————————————————————\n");
                    if(a==ck[0] or a==ck[1]):
                       b('''C++是C语言的继承，它既可以进行C语言的过程化程序设计，又可以进行以抽象数据类型为特点的基于对象的程序设计，还可以进行以继承和多态为特点的面向对象的程序设计。C++擅长面向对象程序设计的同时，还可以进行基于过程的程序设计，因而C++就适应的问题规模而论，大小由之
                         C++不仅拥有计算机高效运行的实用性特征，同时还致力于提高大规模程序的编程质量与程序设计语言的问题描述能力。
                         中文名:C++语言 外文名:The C++ Programming Language/c plus plus 类    别:计算机程序设计语言 创始人:Bjarne Stroustrup 创始公司:贝尔实验室 基本内容:类、封装、重载、继承、模版''')
                    elif(a==ck[2]): 
                        b("星光工作室(Star Light,简称SR)，2020年2月28日入驻学而思编程社区，主要部门有教育部和科技研发部；以优秀作品著称，公认学而思最脚踏实地的工作室作品。涉及爬虫、pygame、tkinter和python终端输出。口号有:不断创新创新永远是我们的口号，探索探索再探索，学习学习再学习！技术党拥有涉及许多方面的技术人才，打造良好的学习环境。Idea创意使我们不甘平庸，创意使我们继续向前")
                    elif(a==ck[3]): 
                        b("霍沃格兹工作室于2020年3月9日由陈张远致成立，内部有大量的优秀成员，欢迎大家进入(绝非打广告！)")
                    elif(a==ck[4]): 
                        b("诺耀工作室于2020年3月13日由创始人李佳诺所建。有自己的官网：http:#nuoyaogzsguanfang.cn。创建了“诺耀工作室”的微信公众号。目前在学而思，网易卡塔，小码王等社区内总共作品有60+")
                    elif(a==ck[5]): 
                        b("星斩工作室于2020年1月30日成立，拥有20+成员，均承包不同语言，官方网站：www.starcutc.com。官方邮箱：starcutcn@163.com、starcut@starcutc.com。在学而思、编程猫、卡搭社区都有人员。")
                    elif(a==ck[6] or a==ck[7]): 
                        b("Scratch是麻省理工学院的“终身幼儿园团队”开发的图形化编程工具，主要面对青少年开放。\n目前已有1.4版、2.0版本（增加克隆积木，视频侦测，Lego拓展积木）、3.0版本（增加文字朗读、翻译和Makey makey等选择性下载扩展积木，并增加micro:bit和Lego mindstorms EV3拓展积木）。所有人都可以在任意版本中创作自己的程序。")
                    elif(a==ck[8] or a==ck[9]): 
                        b("Python是一种跨平台的计算机程序设计语言。 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越多被用于独立的、大型项目的开发")#我是水印，我就藏在这里
                    elif(a==ck[10] or a==ck[11]): 
                        b("层叠样式表(英文全称：Cascading Style Sheets)是一种用来表现HTML（标准通用标记语言的一个应用）或XML（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种脚本语言动态地对网页各元素进行格式化。\nCSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力")
                    elif(a==ck[12] or a==ck[13] or a==ck[14]): 
                        b("HTML称为超文本标记语言，是一种标识性的语言。它包括一系列标签．通过这些标签可以将网络上的文档格式统一，使分散的Internet资源连接为一个逻辑整体。HTML文本是由HTML命令组成的描述性文本，HTML命令可以说明文字，图形、动画、声音、表格、链接等。")
                    elif(a==ck[15] or a==ck[17] or a==ck[16]): 
                        b("PHP即“超文本预处理器”，是一种通用开源脚本语言。PHP是在服务器端执行的脚本语言，与C语言类似，是常用的网站编程语言。PHP独特的语法混合了C、Java、Perl以及 PHP 自创的语法。利于学习，使用广泛，主要适用于Web开发领域。")#我还能藏这
                    elif(a==ck[20] or a==ck[18] or a==ck[19] or a==ck[21]): 
                        b("JavaScript（简称“JS”） 是一种具有函数优先的轻量级，解释型或即时编译型的编程语言。虽然它是作为开发Web页面的脚本语言而出名的，但是它也被用到了很多非浏览器环境中，JavaScript 基于原型编程、多范式的动态脚本语言，并且支持面向对象、命令式和声明式（如函数式编程）风格。")
                    elif(a==ck[22]): 
                        b("秦浩铭，漫威工作室室长，本词典提供方之一(另一个是缪子航)，他打破了一个个不可能的纪录(如大屏logo等)\n让人很遗憾的是，秦浩铭于2020年4月18日离开社区，漫威工作室因没有室长逐渐瓦解")
                    elif(a==ck[23] or a==ck[24]): 
                        b("PEN果工作室(MOGO,中文名笔果)，成立于2019年6月6日，旗下有酷喵工作室，Microsoft工作室，编程行业技术研究进军领导者")
                    elif(a==ck[25]): 
                        b("酷喵(kumiao),PEN果旗下工作室，成立于2019年1月1日，于2019年6月6日被缪子航收购并担任其室长。")#水印潘夕习
                    elif(a == ck[26] or a == ck[27] or a == ck[28]): 
                        b("CPB防栗局(SEVA)，是著名人物与作品的发源地。")
                    elif(a==ck[29]): 
                        b("漫威工作室(MARVEL)创建于2019年10月23日，室长是秦浩铭，成员最多达到50+。\n2020年4月18日，秦浩铭离开社区，漫威逐渐瓦解")
                    elif(a==ck[30]): 
                        b("星河室长马子锦(马秃头)。2019年8月28日建立星河工作室；创造了slow函数，即逐字输出，现在人们在编程社区编程，一定会用到slow函数，这就得感谢他的功劳了。")
                    elif(a==ck[31]): 
                        b("缪子航，PEN果工作室室长，本词条提供方之一(详见\"秦浩铭\"词条)")
                    elif(a==ck[32]): 
                        b("月高工作室于2019年11月23日由创始人潘夕习成立，具有代表作《跳舞的线》。")#I am水印
                    elif(a==ck[33]): 
                        b("潘夕习，月高工作室室长，本词典提供方")
                    elif(a==ck[34]): 
                        b("C语言是一门面向过程的、抽象化的通用程序设计语言，广泛应用于底层开发。C语言能以简易的方式编译、处理低级存储器。C语言是仅产生少量的机器语言以及不需要任何运行环境支持便能运行的高效率程序设计语言。尽管C语言提供了许多低级处理的功能，但仍然保持着跨平台的特性，以一个标准规格写出的C语言程序可在包括类似嵌入式处理器以及超级计算机等作业平台的许多计算机平台上进行编译")#有评论区?
                    elif(a==ck[35]): 
                        b("星河工作室是一个成立半年的工作室\n半年的沉淀使得星河工作室一跃上前,成为社区前三工作室\n星河工作室一直要求:\"高质量,高科技,高素养\"\n我们工作室曾经遇到许多挫折,甚至倒闭过一段时间\n但是... 我们撑下来了,我们一起努力,一起呐喊) 有难同当,有福同享) 最后,我们成功的走到了现在!\n一个工作室的核心不是人数,也不是技术,是团结")
                    elif(a==ck[36]): 
                        b("酷喵浏览器{PEN果研发，李承竣、秦浩铭、潘夕习代理}\n原【酷喵搜索】\n酷喵浏览器适配于各种电脑以及手机(Alpha)，【极速版】支持XP/2000/9x/Vista等老系统。酷喵浏览器采用【PEN果自研PKEN核心引擎以及GMS搜索引擎（PEN果自研引擎）】，实现了{极速，流畅，无恶意程序等多方面优点}。目前正在开发插件技术")#是不是水印放太少了
                    elif(a==ck[37]): 
                        b("易语言（EPL）是一门以中文作为程序代码编程语言，其以“易”著称，创始人为吴涛。易语言早期版本的名字为E语言。其最早的版本的发布可追溯至2000年9月11日。创造易语言的初衷是进行用中文来编写程序的实践，方便中国人以中国人的思维编写程序，并不用再去学习西方思维。易语言的诞生极大的降低了编程的门槛和学习的难度。从2000年以来，易语言已经发展到一定的规模，功能上、用户数量上都十分可观。")
                    elif(a==ck[38]):
                        print( "酷喵浏览器【使用须知】 | {PEN果公司}授权使用 |"  )
                        print( "欢迎使用【酷喵浏览器】，谢谢你的观看！\n谢谢点赞的人/谢谢观看的人/谢谢使用的人！"  )
                        print( "酷喵浏览器Python版网址链接：↓\ncode.xueersi.com/home/project/detail?lang=code&pid=5781119&version=python&form=python&langType=python"  )
                        print( "酷喵浏览器C++版网址链接：↓\ncode.xueersi.com/home/project/detail?lang=code&pid=5291453&version=cpp&form=cpp&langType=cpp"  )
                        print( "没有使用的同学可以先去体验一下哦！（还有Beta版哦！）"  )
                        print( "1、酷喵浏览器持续更新1年（或更久），持续更新日期截至2021.04.20（或许会继续更新）"  )
                        print( "2、酷喵浏览器开源协议：\n(1)开源是使同学们更好地了解程序，不是用于抄袭\n(2)转载请标明版权（改编请标明原程序制作商的名称【PEN果公司】）\n(3)开源不仅仅是公开源码，源码里还有很多【作者寄语Beta】\n(4)欢迎提供【开源词库】\n(5)不欢迎大家抄袭/可以学习/可以转载/可以观摩/可以收藏"  )
                        print( "3、酷喵浏览器的词库仍在开发中，暂时使用【无敌百科的词库】，特此鸣谢{秦浩铭?2020}"  )#97行水印20号画的
                        print( "4、欢迎任何人投稿加入酷喵浏览器，谢谢"  )
                        print( "5、酷喵浏览器点赞的人可获得更多权益（详见酷喵浏览器搜索【点赞的人】）"  )
                        print( "6、酷喵浏览器使用{PEN果自研PKEN核心引擎以及GMS搜索引擎（PEN果自研引擎）}，"  )
                        print( "   注：此搜索引擎/核心引擎均为【开源引擎】，欢迎大家的使用（但必须标明版权）"  )
                        print( "7、酷喵浏览器3大特权：\n（1）浏览器持续更新 \n（2）欢迎任何人提供词库/人物 \n（3）SVIP般的体验，快速打开，快速搜索词库，无限速服务，Windows 95及以上版本均支持使用/Mac OS 5(System 5)以上版本：均支持使用"  )
                        print( "请按任意键继续...")
                        system("read anykey")#按任意键继续 
                    elif(a==ck[39]): 
                        b("金恺文，男，11岁，生于2009年8月5日，IQ120，EQ105，霍格沃茨工作室程序管理员，代表作——HOGWARS电脑：https://code.xueersi.com/home/project/detail?lang=code&pid=4177436&version=python&form=python&langType=python，目前Python等级3级(喂，这样窃取个人隐私不好吧)")
                    elif(a=="退出"):
						#"退出"是特殊词条，所以没有加到ck库里面去
                        system("export xterm=TERM&&clear")
                        print("\033[0m\033[44m请稍后......\n酷喵浏览器正在关闭\033[0m\033[?25l");break;
                    elif(a==ck[40]):
                        print("不知道该搜索什么?现在支持搜索的词条有(有的是拼写不同的同义词，不算词条内，不想玩了输\"退出\"):\n")
                        sleep(1)
                        for i in range(41):
                            print(ck[i])
                            sleep(0.05)
                        print("共27个词条\n")
                        sleep(2)
                        print("请按任意键继续...")
                        system("read anykey")
                    elif(a==ck[41]):
                        b("陈妍悦，梦时工作室成员，著名作品有《闪耀星途》，且有许多粉丝，和茜文是姐妹关系，缪子航的妹妹。");
                    elif(a==ck[42]):
                        b("王铭煊,女，曾多次抄袭他人作品，还喜欢抄袭logo（比如远光灯的logo）；，此人不仅不承认自己的错误，还继续诋毁他人。（大家应该都知道他的为人了吧，大家有没有发现这个人的介绍没有小卡片的标识【以为我觉得他不应该有小卡片的标识】）");
                    elif(a==ck[43]):
                        b("茜文，女，天蝎座，繁星桥阳和魔幻工作室室长，PEN果工作室副室长，霍格沃茨审核员，远光灯记者，刘炳毅粉丝，茜烨的姐姐。");
                    else:#109行那个，水印不是打字打出来的吗，你怎么说画？？？
                        print("对不起，本词典暂无此词条，请检查拼写或向开发者联系微信:pjf420137013 QQ:420137013\n")
                        #你以为水印是干嘛的，防伪呗！
                        #我们是一家的
                        #楼上说的对
                    sleep(3)
                    system("export xterm=TERM&&clear")
                    continue
        elif prog=="13":
            if True:
                hy=0
                print("\033[94mPan 3.0 in Virtual")
                print("      基于虚拟机技术构建")
                sleep(0.3)
                system("clear")
                for i in range(11):
                    print("Pan 3.0 in Virtual")
                    print("      基于虚拟机技术构建")
                    print("正在开机..."+("▇"*i))
                    sleep(0.2)
                    qing()
                sleep(0.5)
                qing()
                print("__________________")
                print("|                  |")
                print("|                  |")
                print("|        +         |")
                print("|                  |")
                print("|__________________|")
                print("\033[94m请点击屏幕验证身份并激活光标")
                sleep(2)
                qing()
                password_yz=None
                password_yz=input("\033[?25h请输入您的密码:")
                while password_yz!=word:
                    password_yz=input("\033[91m密码错误，请输入您的密码:")
                print("\033[93m\033[?25lO 欢迎")
                sleep(2)
                qing()
                while 1:
                    print("\033[0m------------PAN PRO 3---------------")   
                    print(ctime())
                    print('''\033[?25m0.关机
1.设置
2.计算器
3.平均数计算器
4.鸡兔同笼计算器
5.年龄计算器
6.记事本
7.小游戏
8.更新
9.信息
10.成绩预测
11.加入工作室
12.护眼模式
13.你的身材标准吗？
14.幻觉
15.新闻
16.如何一夜上热搜
17.待机
18."错误"的代码
19.切换程序''')
                    prog3=int(input())
                    system("clear")
                    if prog3==1:
                        print("您已通过Pan Stone授权激活。")
                        print("\033[31m? 激活Pan YES")
                    elif prog3==2:
                        print("输入的数全为整数")
                        print("输入运算符号 1:+ 2:- 3:* 4:/")
                        fuhao=int(input())
                        s1=int(input("输入第一个数"))
                        s2=int(input("输入第二个数"))
                        if fuhao==1:
                            print(s1+s2)
                        elif fuhao==2:
                            print(s1-s2)
                        elif fuhao==3:
                            print(s1*s2)
                        elif fuhao==4:
                            print(s1/s2)
                        else:
                            print("错误")
                    elif prog3==3:
                        gs=int(input("有几个数"))
                        pjs=0
                        for j in range(0,gs):
                            s=int(input("输入数字："))
                            pjs=pjs+s
                        print("平均数是:",pjs/gs)
                    elif prog3==4:
                        head=int(input("有几个头"))
                        feet=int(input("有几只脚"))
                        chicken=feet-(head*2)
                        rabbit=chicken/4
                        chicken=head-rabbit
                        print("鸡有",int(chicken),"只，兔有",int(rabbit),"只")
                    elif prog3==5:
                        new=int(input("输入已知年龄"))
                        old=int(input("已知年龄到了这个年纪之后，老的多少岁？(已知年龄<未知年龄)"))
                        print("老的年龄是",(old-new)/2,"岁")
                    elif prog3==6:
                        while True:
                            qing()
                            print("\033[?25h\033[32m欢迎使用记事本!\033[34m输入已有记事本打开,\033[33m输入新名字即可新建,\033[31m输入exit退出,\033[35m输入recycle查看回收站")
                            print("\033[33m已有记事本:\033[0m")
                            for i in jsb:
                                print(i)
                            j=input("\033[36m输入记事本名:")
                            qing()
                            if j.lower()=='exit':
                                print("\033[?25l")
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
                    elif prog3==7:
                        for i in range(1,16):
                            num=random.randint(0,10)
                            score=0
                            print("?"+" "*num+"\(·□·)\ ")
                            sum1=int(input("输入目测距离(误差不超过1个空格):"))
                            if sum1==num or sum1==num-1 or sum1==num+1:
                                print("吃到emoji小人，加两分！")
                                score=score+2
                            else:
                                print("粉身碎骨，扣一分！")
                                score=score-1
                            print("你的得分为：",score)
                    elif prog3==8:
                        print("检测中······")
                        sleep(1)
                        print("您的版本:Virtual 2019 SP2 最新版本:Virtual 2021 Build 2018(2019 Sp2的测试版本)\n您已是最新版本。")
                    elif prog3==9:
                        z("提前声明:请勿发送给陌生人，否则您的精神或财产可能受到损失")
                        phone = input("\033[32m请输入手机号码:")
                        if len(phone) < 5:
                            system("clear")
                            print("请输入正确的手机号码!")
                            sleep(1)
                            system("clear")
                        conten = input("请输入发送内容[Enter发送]:")
                        send_msg(int(phone),conten)
                        print("发送成功\033[42m ✔ \033[0m")
                    elif prog3==10:
                        print("预计你某科的成绩为",randint(85,100),"分")
                    elif prog3==11:
                        print("""【程序部】（选一完成）要求：会Scratch,Python,C++（重要）要求不高，但作品需要精致，不抄袭，不骗赞
        【文艺部】要求：精通Scratch，工作：进行录音/拍摄等一些工作
        【宣传部】选一作品或者工作室招人进行宣传，发送到学而思编程官网即可
        【后勤部】要求和程序部一样，修改程序部的bug即可。
        PS:有意者请加QQ:420137013 如果有英语不行的，关注微信公众号:Eng-Knows""")
                    elif prog3==12:
                        if hy==0:
                            print("\033[32m护眼模式已打开！")
                            hy=1
                        else:
                            print("\033[37m护眼模式已关闭！")
                            hy=0
                    elif prog3==13:
                        cm=int(input("输入你的身高（单位：厘米）"))
                        kg=int(input("输入你的体重（单位：千克）"))
                        std=(cm-100)*0.9
                        if kg>std*1.1:
                            print("你偏胖")
                        elif kg<std*0.9:
                            print("你偏瘦")
                        else:
                            print("你的身材很标准?！")
                    elif prog3==14:
                        print("\033[93m代码运行结束")
                        sleep(3*2)
                        print("\033[37m什么？你还没走？")
                        print("那试试这样子吧")
                        break
                    elif prog3==15:
                        print("暂无资讯")
                        input("看完按Enter")
                    elif prog3==16:
                        print("1.发一些社区人都关注的东西，如“操作系统”，“反迷你”等标题")
                        print("2.如果你不那样的话，你就反复点你的作品，再刷新，就可以了(只能做一次，绝非刷赞)")
                    elif prog3==17:
                        sl=int(input("输入待机秒数，不超过2.5分钟"))
                        if sl<=150:
                            for i in range(0,sl):
                                print(sl)
                                sl=sl-1
                                sleep(1)
                        
                        else:
                            print("时间超限！")
                        print("O欢迎！")
                    elif prog3==18:
                        print('''Traceback (most recent call last):
File "main.py", line 1020, in <module>
    sleep(2)
    ^
NameError: name 'sleep' is not defined
\033[93m代码运行结束''')
                    elif prog3==0:
                        print("正在关机······")
                        sleep(2)
                        break
                    elif prog3==19:
                        if qhqd==0:
                            print("\033[44m")
                            qing()
                            print("欢迎使用程序切换功能")
                            sleep(2)
                            print("此程序目前处于Beta版本，如有Bug请在评论区里反馈。")
                            sleep(3)
                            ch=input("如果你现在使用，部分功能可能会被限制，是否(Y|N)继续启动?")
                            if ch=="Y":
                                qing()
                                print("\033[000m启动成功")
                                qhqd=1
                                sleep(3);qing();
                                print("输入支持的程序序号:")
                                chqh=input("1.命令提示符 2.计算器")
                                if chqh=="1" or chqh=="2":
                                    goto=1
                                    break
                                else:
                                    print("不支持此程序，请重新打开此程序并输入;-)")
                            else:
                                qing()
                                print("\033[000m您放弃了启动。")
                        else:
                            sleep(3);qing();
                            print("输入支持的程序序号:")
                            chqh=input("1.命令提示符 2.计算器")
                            if chqh=="1" or chqh=="2":
                                goto=1
                                break
                            else:
                                print("不支持此程序，请重新打此程序开并输入;-)")
                        
                    else:
                        print("该程序不存在。")
                    sleep(6.5)
                    system("clear")
                    continue
        else:
            software_len = len(prog)
            NUMBER = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
            try:
                software2 = int(prog)
                YUAN = "您输入了不合法的编号，请您输入正确编号~"
            except:
                if prog == "" or prog == " " or prog == " "*software_len:
                    YUAN = "您什么也没输入哟~"
                elif prog in NUMBER:
                    YUAN = "请输入阿拉伯数字,不可输入汉字~"
                elif prog[0:3] == "www" or prog[0:4] == "http":
                    YUAN = "不支持输入网址~"
                elif prog=="13" and ds_1==0:
                    YUAN = "您还没有安装此软件"
                else:
                    YUAN = "您输入了程序名,请输入编号~"
            qing()
            print()
            print()
            print("\033[33m系统未查找到软件 - {} -".format(prog))
            print("\033[36m原因:{}".format(YUAN))
            sleep(0.5)
            input("\033[32mEnter键返回开始菜单。")
            qing()
            continue
        print("10秒后返回桌面。")
        sleep(10)
        qing()
        continue
except:
    bsod()
