from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*
import platform
import requests
#-----------------------------------导库-------------------------------
ds_1=0
def error():
    print("\033[44m")
    qing()
    print("                ⚠  ")
    print("               警告")
    print("现在您暂时无法使用系统因为你输入了一些代码")
    print("或系统发生了一些错误，请按运行键继续\033[8m:")

def qing():
    system("clear")

def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    
def kfz():
    while 1:
        print("\033[91m提示:您已进入开发者模式!")
        print("\033[0m开始                        developer")
        print("\033[95m1.命令提示符    \033[93m2.计算器      \033[92m3.记事本     \033[90m4.关机     \033[91m5.手动Ghost")
        print("\033[0m"+strftime("%H:%M",localtime()))
        kfz=input("\033[0m请输入应用序号:")
        qing()
        if kfz=="1":
            print("\033[0mHOTM Pan[开发者版本3900]")
            print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
            while 1:
                print("C:\\local>",end="")
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
                elif dos=="clear":
                    qing()
                elif dos=="cmd":
                    print("HOTM Pan[版本3.65.3901]")
                    print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3901]")
                elif dos=="bsod" or dos=="shutdown":
                    print("请稍等\n正在退出CMD")
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
        elif kfz=="2":
            print("\033[0mSystem(C:)\n6.18GB可用/8.00GB")
            print("\033[0m备份Ghost(E:)\n1.90GB可用/2.00GB")
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
            elif System32=="E:":
                print("名称    类型             修改日期               大小")
                print("Ghost   扩展驱动(.dll)   2020年7月18日 19:38    53MB")
                #102.4M
                print("PanTSE2 系统安装包(.wim) 2020年10月1日 18:59    49MB")
                print("readme  文本(.txt)       2020年10月1日 19:02    409.6KB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="readme":
                    b("本磁盘是重置系统备份的磁盘")
                    b("【请勿重新格式化】\n【请勿删除文件】\n【请勿添加文件】")
                    b("否则，系统将永久崩溃，切记~~~~~~")
                else:
                    print("该文件不可预览")
            else:
                print("该文件不存在")
        elif kfz=="3":
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
        elif kfz=="4":
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
        elif kfz=="5":
            setup()
        else:
            software_len = len(kfz)
            NUMBER = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
            try:
                software2 = int(kfz)
                YUAN = "您输入了不合法的编号，请您输入正确编号~"
            except:
                if kfz == "" or kfz == " " or kfz == " "*software_len:
                    YUAN = "您什么也没输入哟~"
                elif kfz in NUMBER:
                    YUAN = "请输入阿拉伯数字,不可输入汉字~"
                elif kfz[0:3] == "www" or kfz[0:4] == "http":
                    YUAN = "不支持输入网址~"
                else:
                    YUAN = "您输入了程序名,请输入编号~"
            qing()
            print()
            print()
            print("\033[33m系统未查找到软件 - {} -".format(kfz))
            print("\033[36m原因:{}".format(YUAN))
            sleep(0.5)
            input("\033[32mEnter键返回开始菜单。")
            qing()
            continue
        print("\n10秒后返回开始菜单\033[000m")
        sleep(10)
        qing()
        continue

def setup():
    print("\033[44m")
    qing()
    print("Pan Setup")
    print("准备工作...\n备份文件到D盘")
    print("C:\\"+name+"\\user.dll")
    sleep(0.09)
    print("C:\\"+name+"\\data.gho")
    sleep(0.2)
    sleep(15)
    qing()
    print("Pan Setup")
    print("现在开始重装系统\n您选择的系统是:Pan TSE2")
    sleep(3)
    qing()
    print("Pan Setup")
    print("正在获取电脑配置")
    sleep(5)
    qing()
    print("Pan Setup")
    print("正在配置Pan")
    sleep(20)
    qing()
    sb=randint(0,10)#没有骂人，在这里sb是“失败”的缩写
    if sb==5:
        print("Pan Setup")
        print("配置Pan失败，正在还原配置")
        sleep(5)
        qing()
    print("Pan Setup")
    print("正在复制文件")
    sleep(1)
    print(r"C:\local\Start.exe")
    sleep(4.5)
    print(r"C:\local\Touch.dll")
    sleep(1)
    print(r"C:\local\program.exe")
    sleep(1.5)
    print(r"C:\local\System.dll")
    sleep(0.1)
    print(r"C:\local\Startup.exe")
    sleep(0.09)
    print(r"D:\user.dll")
    sleep(0.09)
    print(r"D:\data.gho")
    sleep(0.2)
    print("所有文件都已复制成功")
    sleep(3)
    qing()
    print("Pan Setup")
    print("准备就绪...")
    sleep(randint(2,15))
    qing()
    print("Pan Setup")
    print("准备完成！\n您的数据和用户信息成功的保存了下来，系统也重装完成，接下来您可以尽情使用Pan TSE了\n5秒后进入系统")
    sleep(5)
    qing()

llqjh=0
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
    for i in range(randint(2,6)):
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
    name=input("请输入您的姓名:")
    password=input("请输入您的密码:")
    qing()
    password_yz=None
    password_yz=input("请再次输入您的密码:")
    while password_yz!=password:
        password_yz=input("\033[91m密码错误，请输入您的密码:")
    print("\033[94mo 欢迎"+name)
    sleep(2)
    qing()
    while 1:
        print("\033[0m开始                        "+name)
        print("\033[90m0.关机  \033[30m1.待机    \033[91m2.计算器")
        print("\033[31m3.记事本        \033[92m4.重启（不会丢失数据)")
        print("\033[32m5.系统属性    \033[93m6.命令提示符    \033[33m7.有道     \033[94m8.地图 ")
        print("\033[95m9.浏览器        \033[34m10.计算机      \033[35m11.Pan系统入门 \033[96m12.应用商店")
        if ds_1==1:
            print("\033[91m13.地图")
        print("\033[0m"+strftime("%H:%M",localtime()))
        prog=input("\033[0m请输入应用序号:")
        qing()
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
            print("\033[0m电脑正在休眠，按Enter键结束")
            sleep(0.5)
            qing()
            input()
            password_yz=input("请输入您的密码以登录:")
            while password_yz!=password:
                password_yz=input("\033[91m密码错误，请输入您的密码:")
            print("\033[94mo 欢迎"+name)
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
            print("\033[35m+===============SegoeOS万能计算器===============+")
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
        elif prog=="4":
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
            password_yz=input("请输入您的密码以验证身份:")
            while password_yz!=password:
                password_yz=input("\033[91m密码错误，请输入您的密码:")
            print("\033[94mo 欢迎"+name)
        elif prog=="5":
            print("\033[101m  \033[0m\033[102m  \033[0m")
            print("\033[104m  \033[0m\033[103m  \033[0mPan\033[91mTouch Speed Edition")
            print("\033[0mHOTM Pan")
            print("版本3.65(内部版本 2.0.1测试版本)")
            print("版权所有 ©2020 HOTM Workshop。保留所有权利。")
            print("PanTSE 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
            input("看完按Enter")
        elif prog=="6":
            print("\033[0mHOTM Pan[版本3.65.3912]")
            print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
            while 1:
                print("C:\\local>",end="")
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
                elif dos=="clear":
                    qing()
                elif dos=="cmd":
                    print("HOTM Pan[版本3.65.3912]")
                    print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3912]")
                elif dos=="bsod" or dos=="shutdown":
                    print("请稍等\n正在退出CMD")
                    break
                elif dos=="modify":
                    user=input("新用户名:")
                    password=input("新密码:")
                    print("修改成功!")
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
        elif prog=="7":
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
        elif prog=="8":
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
        elif prog=="9":
            #运行正式版会崩，这里用极速版
            print("\033[91m检测到您的电脑性能不佳，已自动切换成极速版\033[0m")
            sleep(0.5)
            qing()
            if llqjh==0:
                password_yz=input("请输入您的密码以激活:")
                while password_yz!=password:
                    password_yz=input("\033[91m密码错误，请输入您的密码:")
                print("\033[93mo 激活成功")
            ck=["c++","C++","星光工作室","霍格沃兹工作室","诺耀工作室","星斩工作室","Scratch","scratch","Python","python","css","CSS","HTML","html","Html","PHP","php","Php","javascript","js","JavaScript","JS","秦浩铭","PEN果公司","PEN果工作室","酷喵工作室","CPB防栗局","cpb防栗局","Cpb防栗局","漫威工作室","马子锦","缪子航","月高工作室","潘夕习","C语言","星河工作室","酷喵浏览器","易语言","使用须知","金恺文","帮助","陈妍悦","王铭煊","茜文"];
            f=0;

            if 1:
                system("export xterm=TERM&&clear")#不想看见编译成功
                while(1):
                    print("                             \033[34m酷\033[94mku\033[91mmiao\033[31m喵\n");
                    print("                    \033[94m┌──────────────────────────┐\n");#水印
                    print("                    \033[94m│                          \033[94m│\033[000m\n");#防伪
                    print("                    \033[94m└──────────────────────────┘\n");
                    print("\033[3A                    |  \033[000m")
                    print("\033[?25h")
                    a=input()
                    print("\033[0m")
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
        elif prog=="10":
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
        elif prog=="11":
            print("\033[0m1.开机和登录 2.软件 3.浏览器问题 4.升级Pan 5.进入开发者模式 6.重装系统")
            rm=input()
            qing()
            if rm=="1":
                b("1)360报告卡顿现象\n清理电脑垃圾或重启机器即可，如问题严重，请换个浏览器(推荐Chrome)或重装系统(推荐win7，iPadOS)。\n2)基本信息可以不填么?\n可以，但是最好填(也可以在开始菜单打开命令提示符输入modify更改)，姓名栏可以写您的真实名字，也可以写您的昵称。")
                b("\n3)用电脑能正常运行PanTSE吗?\n能，系统最好xp以上，如果只想体验触摸系统(平板系统)，建议使用iPad\n4)为什么我一启动机器就会报告蓝屏?\n可能是您在开机时输入了一些东西或者系统发生了一些小错误导致的，如果问题严重，可以降级到Pan5.1")
                b("\n5)为什么我输入自己的密码提示错误?\n可能您拼写不正确或别人更改了您的密码，重启机器即可解决。")
            elif rm=="2":
                b("0功能，关闭机器\n1功能，休眠，您可以在这时候放松一下，放松完按Enter键重新进入开始菜单\n2功能，计算器，解决生活中的数学问题，如果您在做作业，不建议这样做。")
                b("3功能，记事本，将一天要做的事记录下来，Pan会帮你存储到c盘中。\n4功能，重启，如果您的机器遇到问题可以打开此功能，如果是大问题，请按停止键再按运行键。\n5功能，系统属性，可以查看系统的基本信息。(也可以在命令提示符输入panver查看版本)\n")
                b("6功能，MS-DOS，现在改名为CMD,用在一些专业的行业当中\n7功能，有道，可以轻松翻译英，韩，日，中四国语言\n8功能，地图，如果迷路了，可以通过它来找到回家的路(前提是你得有钱坐公交)\n")
                b("9功能，浏览器，运行正式版会崩，所以这里统一用极速版了(酷喵的，已经授权了)\n10功能，计算器(我可不是2功能哦)，类似于PanNT4的\"我的电脑\"\n11功能就是我啦，可以给刚刚入坑的Pan小白一些帮助\n")
            elif rm=="3":
                b("1)在浏览器运行过程中蓝屏了怎么办?\n进入TSE的源码http://code.xueersi.com/ide/code/6421076找到【浏览器】的脚本，更改一下出错源码位置，或者重新按运行键\n")
                b("2)总是提醒该词条不存在是怎么肥事?\n检查拼写是否正确或者输入\"帮助\"看看浏览器里面都有什么词条。")
                b("3)超长了怎么办?\n重按运行键即可。\n4)为什么浏览器退不出来?\n等浏览器返回到主页，输入\"退出\"即可。")
            elif rm=="4":
                b("如果您的电脑运行的是已经停止支持的Pan2.0或者是即将停止支持的Pan3.0，我们建议您升级到Pan2020及以上版本，谢谢配合！")
            elif rm=="5":
                yq=None
                while yq!="PANTSE20200706":
                    yq=input("请输入邀请码:")
                qing()
                kfz()
            elif rm=="6":
                setup()
                print("\033[0m")
            else:
                print("该章节不存在")
        elif prog=="12":
            print("1.?阿丘快跑\033[91m小组件\033[0m")
            print("2.?地图")
            down=int(input("请选择要安装的软件的序号:"))
            if down==1:
                qing()
                print("   ?阿丘快跑\033[91m小组件\033[0m")
                print("           姚小超")
                print("\033[92mHOTM检测通过√")
                print("\033[92m360检测通过√")
                print("准备文件...")
                sleep(2)
                qing()
                print("   ?阿丘快跑\033[91m小组件\033[0m")
                print("           姚小超")
                print("\033[92mHOTM检测通过√")
                print("\033[92m360检测通过√")
                print("正在安装...")
                sleep(5)
                qing()
                jl=""
                for i in range(50):
                    jl = jl + " "
                    print(jl + "阿乒")
                    sleep(0.2)
                    system("clear")
                    jl = jl + " "
                    print(jl + "阿乓")
                    sleep(0.2)
                    system("clear")
            elif down==2 and ds_1==0:
                print("            ?地图")
                print("         HOTM官方")
                print("\033[92mHOTM检测通过√")
                print("\033[92m360检测通过√")
                print("准备文件...")
                sleep(5)
                qing()
                print("            ?地图")
                print("         HOTM官方")
                print("\033[92mHOTM检测通过√")
                print("\033[92m360检测通过√")
                print("正在安装...")
                sleep(18)
                qing()
                print("安装完成，请到开始菜单输入13查看。")
                ds_1=1
            else:
                print("非常抱歉，暂无此软件或您已安装此软件")
        elif prog=="13" and ds_1==1:
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
        print("\n10秒后返回开始菜单\033[000m")
        sleep(10)
        qing()
        continue
except:
    qing()
    error()
    