from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*#string库？感觉好奇怪
import platform
import requests
#-----------------------------------导库-------------------------------
def error():
    print("\033[44m")
    qing()
    print("                ⚠  ")
    print("               警告")
    print("现在您暂时无法使用系统因为你输入了一些代码")
    print("或系统发生了一些错误，请按运行键继续\033[8m:")

def qing():
    system("clear")
#---------------------------------定义---------------------------------
try:
    print("\033[?25l",end="")
    su1=time()
    for i in range(3):
        print("_")
        sleep(0.5)
        qing()
        sleep(0.5)
    sleep(1)
    for i in range(5):
        for j in range(10):
            print("  "*j+"|||")
            print("©HOTM Workshop")
            sleep(0.1)
            qing()
        qing()
    sleep(2)
    su2=time()-su1
    su2=round(su2)
    if su2<=11:
        print("\033[93m360提醒您:本次开机用了"+str(su2)+"秒，超越了全国99%的电脑，获得五星级神机称号")
    elif su2<=12:
        print("\033[93m360提醒您:本次开机用了"+str(su2)+"秒，超越了全国97%的电脑，可能是卡顿情况，此为正常现象")
    elif su2<=20:
        print("\033[93m360提醒您:本次开机用了"+str(su2)+"秒，超越了全国75%的电脑，速度比较慢啊")
    else:
        print("\033[93m360提醒您:本次开机用了"+str(su2)+"秒，超越了全国1%的电脑，你的电脑延迟非常严重，建议检查网络")
    sleep(3)
    qing()
    while 1:
        print("\033[0m开始")
        print('''\033[31m0.关机     \033[32m1.睡眠     \033[33m2.计算器
\033[34m3.各代Pan版本死亡倒计时
\033[35m4.记事本            \033[36m5.新版本检测
\033[31m6.重启 \033[32m7.Pan5.1小动画
\033[33m8.系统属性    \033[34m9.360安全卫士    \033[35m10.Pan Virtual PC 2019
\033[36m11.斗地主
\033[31m12.MS-DOS
\033[32m13.有道翻译官   \033[33m14.系统推广程序   \033[34m15.地图  \033[35m16.我的电脑
''')
        prog=input("\033[0m输入应用程序序号:")
        system("clear")
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
            input()
        elif prog=="2":
            qing()
            print("\033[002m\033[32m     ﹢﹣× ÷       ")
            print("\033[002m\033[34m欢迎使用万能计算器。")
            sleep(0.5)
            qing()
            print("\033[0m\033[32m     ﹢﹣× ÷       ")
            print("\033[34m欢迎使用万能计算器。")
            sleep(1)
            qing()
            print("\033[35m+===============Pan万能计算器===============+")
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
            input("\033[33mEnter键返回桌面。")
        elif prog=="3":
            z("1.Pan1.0 Pro\n\033[91m诞生时间:2019年12月14日 停止主流支持时间:2020年1月14日 停止技术支持时间:2020年5月12日\n已停止支持!历时150天")
            z("2.Pan2.0 Pro\n\033[91m诞生时间:2019年12月19日 停止主流支持时间:2020年5月12日 停止技术支持时间:2020年7月2日\n已停止支持!历时196天")
            z("3.PanTO\n\033[91m诞生时间:2020年1月10日 停止主流支持时间:2020年5月12日 停止技术支持时间:2020年5月12日\n已停止支持!历时123天")
            z("4.Pan98 XP\n\033[91m诞生时间:2019年12月29日 停止主流支持时间:2020年5月16日 停止技术支持时间:2020年6月18日\n已停止支持!历时172天")
        elif prog=="4":
            while 1:
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
                    print("\033[36m| Pan Recovered files\033[32m")
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
                    elif cao == '1':
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
                        while 1:
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
            
        elif prog=="5":
            print("正在检测新版本......")
            sleep(3)
            qing()
            print("最新版本:5.1.1 你的版本:5.1.1")
            print("检测成功，您的版本已是最新")
        elif prog=="6":
            for i in range(5):
                print("\033[0mo 正在重启")
                sleep(0.2)
                system("clear")
                print("\033[94mo 正在重启")
                sleep(0.2)
                system("clear")
            print("\033[0m",end="")
            sleep(1)
            for i in range(3):
                print("_")
                sleep(0.5)
                system("clear")
                sleep(0.5)
            sleep(1)
        elif prog=="7":
            print("\033[41m  \033[0m               \033[42m  \033[0m")
            print("\n\n\n")
            print("\033[44m  \033[0m               \033[43m  \033[0m")
            sleep(0.4)
            system("clear")
            print("\033[41m  \033[0m          \033[42m  \033[0m")
            print("\n\n")
            print("\033[44m  \033[0m          \033[43m  \033[0m")
            sleep(0.4)
            system("clear")
            print("\033[41m  \033[0m   \033[42m  \033[0m")
            print("\n")
            print("\033[44m  \033[0m   \033[43m  \033[0m")
            sleep(0.4)
            system("clear")
            print("\033[41m  \033[0m\033[42m  \033[0m")
            print("\033[44m  \033[0m\033[43m  \033[0m")
            print("\033[0m\033[2mPan 5.1")
            sleep(0.5)
            system("clear")
            print("\033[0m",end="")
            print("\033[101m  \033[0m\033[102m  \033[0m")
            print("\033[104m  \033[0m\033[103m  \033[0m")
            print("\033[0mPan 5.1 Built for Pad")
        elif prog=="8":
            print("\033[101m  \033[0m\033[102m  \033[0m")
            print("\033[104m  \033[0m\033[103m  \033[0mPan 5.1\033[91mPad Special version")
            print("\033[0mHOTM Pan")
            print("版本3.6(内部版本 3900:Service Pack 1)")
            print("版权所有 ©2020 HOTM Workshop。保留所有权利。")
            print("Pan5.1 平板特殊版 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
            input("看完按Enter")
        elif prog=="9":
            print("\033[32m+===============欢迎使用360智能电脑性能测试机===============+")
            input("\033[36m                      Enter键开始测试。             ")
            qing()
            print("\033[33m延时:测试中...")
            print("\033[34m版本:等待中...")
            print("\033[35m更多:敬请期待")
            t1_c = time()
            sleep(1)
            t2_c = time()
            t_c = t2_c - t1_c
            if t_c > 1:
                t_c2 = t_c - 1
                if t_c2 > 0.21:
                    yanshi = str(t_c2)+"秒，您的延时无敌长，说明网络无敌差，建议您使用另一台设备登录您的Pan。"
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
                yanshi = "您的电脑太快啦，比Pan系统运行速度还快，快到系统都无法判断。"
            else:
                yanshi = "fail(测试失败)"
            #测登录
            qing()
            print("\033[33m延时:测试完成")
            print("\033[34m版本:测试中...")
            print("\033[35m更多:敬请期待\033[8m")
            #测更新
            qing()
            print("\033[0m\033[33m延时:测试完成")
            print("\033[34m版本:测试中...")
            print("\033[35m更多:敬请期待\033[0m")
            ce3 = "Pan版本:最新！ python编译器版本:{} 您的系统:{}".format(version[0:5],platform.architecture()[0])
            sleep(2)
            qing()
            print("\033[33m延时:测试完成")
            print("\033[34m版本:测试完成")
            print("\033[35m更多:敬请期待\033[0m")
            sleep(0.1)
            qing()
            print("\033[32m测试结果:")
            print("\033[36m延时:",yanshi)
            print("\033[34m版本:",ce3)
            print("\033[35m此测试数据绝对准确。")
            input("\033[31mEnter键返回桌面")
        elif prog=="10":
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
                print("\033[93mO 欢迎")
                sleep(2)
                qing()
                while 1:
                    print("\033[0m------------PAN PRO 3---------------")   
                    print(ctime)
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
18."错误"的代码''')
                    prog3=int(input())
                    system("clear")
                    if prog3==1:
                        print("您已通过Pan 4.0 NT授权激活。")
                        print("\033[31m?激活Pan YES")
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
                        print("您的版本:Virtual 2019 3.0.1 最新版本:Virtual 2019 3.0.1\n您已是最新版本。")
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
                    else:
                        print("该程序不存在。")
                    sleep(6.5)
                    system("clear")
                    continue
        elif prog=="11":        
            Poke.init()
            Poke.wash()
            Poke.send()    
            Poke.show()
        elif prog=="12":
            print("\033[0mHOTM Pan[版本3.6.3900]")
            print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
            while 1:
                print("C:\\local>",end="")
                dos=input()
                if dos=="help":
                    print("有关某个命令的详细信息，请键入help命令名")
                    print("break    退出dos程序，这与exit是一样的")
                    print("clear    清屏")
                    print("dos      打开一个新的Pan命令解释窗口")
                    print("exit     退出dos程序")
                    print("help     提供Pan的所有命令代码信息")
                    print("panver   查看Pan的版本")
                    print("bsod     自动蓝屏")
                    print("shutdown 关机")
                elif dos=="clear":
                    qing()
                elif dos=="dos":
                    print("HOTM Pan[版本3.6.3900]")
                    print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.6.3900]")
                elif dos=="bsod" or dos=="shutdown":
                    break
                else:
                    print("\""+dos+"\"不是一个命令代码，请检查拼写。")
            if dos=="bsod":
                qing()
                error()
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
        elif prog=="13":
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
        elif prog=="14":
            print("较好的操作系统")
            z("1.JIN霸王系统hw1.0.2\n虽然功能少，且有一些比较大的bug，但是每个应用都可以调戏，但是注意不要运行时间过长，否则直接关机")
            z("2.北弦手机1.0(以我的QQ名命名?)\n在iPad触摸设备上发挥不错，但是在PC上就比较鸡肋了...(win8也不过如此)适合一些性能低的用户使用")
            z("3.阿石电脑30.0\n功能多且实用，先给一个好评，但是这个系统似乎被停止支持更新了?")
            z("4.SUNUI 105\n大V编写的系统，稳定无bug，特别推荐(PS:SogoeOS是我们合作编写的系统)")
            z("5.Pan 2020\n月高工作室新推系统，如果你用的是旧版系统(比如Pan3.0)，建议升级到此系统")
        elif prog=="15":
            try:
                a("1.导航 2.AQI空气质量检测 3.天气预报 ")
                sleep(1)
                a("请问您需要什么？")
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
                        a("请选择要搭乘的路线：")
                        print()
                        num=input("")
                        system("clear")
                        scale=15
                        for i in range(scale+1):
                            aaa = '*'*i
                            bbb = '.'*(scale-i)
                            ccc =(i/scale)*100
                            print("\r\033[1;32m{:^3.0f}%[{}->{}]".format(ccc,aaa,bbb),end='')
                            sleep(0.6)
                        system("clear")
                        num=int(num)
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
                        a("您已在目的地附近!")
                        system("clear")
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
                    system("clear")
                if ans==3:
                    area = input("请问你要查询的地区是：")
                    temp1 = air_temp(area,1)
                    speed1 = air_speed(area,1)
                    print("温度：",temp1,"℃\n    风速",speed1,"米/秒")
            except:
                print("世界上最遥远的距离就是没网。\033[34m检查设置")
        elif prog=="16":
            print("\033[0mSystem(C:)\n6.18GB可用/8.00GB")
            System32=input("输入文件名，(如C:):")
            qing()
            if System32=="C:":
                print("名称    类型           修改日期               大小")
                print("Start   快捷方式(.lnk) 2020年6月14日 13:23    0.12GB")
                print("local   文件夹         2020年6月14日 13:25    1.7GB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="local":
                    print("名称    类型            修改日期               大小")
                    print("Start   软件(.exe)      2020年6月14日 13:23    1.3GB")
                    print("Touch   扩展驱动(.dll)  2020年6月14日 13:26    153MB")
                    print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                    print("System  扩展驱动(.dll)  2020年6月14日 13:30    1MB")
                    print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                else:
                    print("该文件不存在")
            else:
                print("该文件不存在")
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
        print("10秒后返回桌面")
        sleep(10)
        qing()
        continue
except:
    qing()
    error()