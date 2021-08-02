from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from string import*
import platform
import requests

jsb = {}               #记事本
jsbr = {}              #记事本回收站
jsbrc = {}             #记事本内容找回
def a(text):
    stdout.write(text)
    stdout.flush()
def z(text):
    a("\r"+" "*0+"\r")
    for i in text:
        stdout.write(i)
        stdout.flush()
        sleep(0.01)
    print("\n")
def qing():
    system("clear")
def mane():
    user="default"
    while 1:
        print("\033[0m现在是"+strftime("%Y年%m月%d日 %H:%M",localtime()))
        print("""0.关机
1.计算器
2.记事本
3.系统属性
4.MS-DOS
5.我的电脑
6.新版本检测""")
        preprog=input("请选择要打开的应用的编号:")
        qing()
        if preprog=="0":
            print("\033[93m现在你可以安全的关闭你的电脑了")
            break
        elif preprog=="1":
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
            print("\033[36m1=普通计算器      \033[32m2=获取数的公因数")
            print("\033[33m3=综合算式计算    \033[34m4=鸡兔同笼问题")
            print("\033[35m5=平均数计算      \033[36m6=平年闰年计算")
            print("\033[32m7=日期间隔计算")
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
        elif preprog=="2":
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
        elif preprog=="3":
            print("\033[101m  \033[0m\033[102m  \033[0m")
            print("\033[104m  \033[0m\033[103m  \033[0mPan 4.0\033[91mPE ")
            print("\033[0mHOTM Pan")
            print("版本1.0(内部版本 2000:Service Pack 0)")
            print("版权所有 ©2020 HOTM Workshop。保留所有权利。")
            print("Pan4.0 PE 维护版 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
            print("\n根据\033[94m月高工作室软件许可条款\033[0m，本产品使用权属于:\n"+user)
            input("看完按Enter")
        elif preprog=="4":
            print("\033[0mHOTM Pan[版本1.0.2000]")
            print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
            while 1:
                print("C:\\"+user+">",end="")
                dos=input()
                if dos=="help":
                    print("有关某个命令的详细信息，请键入help命令名")
                    print("break    退出dos程序，这与exit是一样的")
                    print("clear    清屏")
                    print("dos      打开一个新的Pan命令解释窗口")
                    print("exit     退出dos程序")
                    print("help     提供Pan的所有命令代码信息")
                    print("modify   修改用户信息")
                    print("bsod     自动蓝屏")
                    print("shutdown 关机")
                elif dos=="clear":
                    qing()
                elif dos=="dos":
                    print("HOTM Pan[版本1.0.2000]")
                    print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="modify":
                    user=input("新用户名:")
                    mm=input("新密码:")
                    print("修改成功!")
                elif dos=="bsod" or dos=="shutdown":
                    break
                else:
                    print("\""+dos+"\"不是一个命令代码，请检查拼写。")
            if dos=="bsod":
                qing()
                error("developer system key file had been deleted")
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
        elif preprog=="5":
            print("\033[0mSystem(C:)\n6.18GB可用/8.00GB")
            print("\033[0mBsod(H:)\n857MB可用/860MB")
            print("\033[0mData(A:)\n1.42MB可用/1.44MB")#不是我自己定的，是A盘存活在这个世界的时候，本来就这么点空间
            System32=input("请输入文件名(比如C:):")
            qing()
            if System32=="C:":
                print("名称    修改日期        类型        大小")
                print(user+"   2020/5/29 17:17 文件夹      1.82GB")
                System32=input("请输入文件名(比如C:):")
                qing()
                if System32==user:
                    print("名称    修改日期        类型        大小")
                    print("System  2020/5/24 15:01 文件夹      1.82GB") 
                    System32=input("请输入文件名(比如C:):")
                    qing()
                    if System32=="System":
                        print("名称            修改日期        类型         大小")
                        print("login.exe       2020/5/16 0:08  应用程序     312MB")
                        print("startup.exe     2020/5/15 23:50 应用程序     17MB")
                        print("run.dll         2020/5/15 20:03 应用程序扩展 1.39GB")
                        print("code.html       2020/5/29 17:17 网页         98MB")
                    else:
                        print("该文件不存在")
                else:
                    print("该文件不存在")
            elif System32=="H:":
                print("名称        修改日期        类型         大小")
                print("bsod.exe    2020/5/16 22:37 应用程序     2MB")
                print("code.py     2020/5/16 21:50 Python代码   52KB")
            elif System32=="A:":
                print("名称        修改日期        类型         大小")
                print("SP1.dll     2020/5/28 12:45 应用程序扩展 28KB")
            else:
                print("该文件不存在")
        elif preprog=="6":
            print("正在检测新版本......")
            sleep(3)
            qing()
            print("最新版本:1.0.1 你的版本:1.0.1")
            print("检测成功，您的版本已是最新")
        else:
            software_len = len(preprog)
            NUMBER = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
            try:
                software2 = int(preprog)
                YUAN = "您输入了不合法的编号，请您输入正确编号~"
            except:
                if preprog == "" or preprog == " " or preprog == " "*software_len:
                    YUAN = "您什么也没输入哟~"
                elif preprog in NUMBER:
                    YUAN = "请输入阿拉伯数字,不可输入汉字~"
                elif preprog[0:3] == "www" or preprog[0:4] == "http":
                    YUAN = "不支持输入网址~"
                else:
                    YUAN = "您输入了程序名,请输入编号~"
            qing()
            print()
            print()
            print("\033[33m系统未查找到软件 - {} -".format(preprog))
            print("\033[36m原因:{}".format(YUAN))
            sleep(0.5)
            input("\033[32mEnter键返回桌面。")
            qing()
            continue
        sleep(10)
        qing()
        continue
def error(pppoe):
    print("\033[0m\033[44m",end="")
    qing()
    print("A problem had been detected and pan has been shut down to repair to you computer")
    print("We will note errors which your computer has")
    print("If you want to know other message,please search:"+pppoe)
    print("press run to continue...\033[0m\033[8m")

try:
    if 1:
       print("\033[000m")
       system("clear")
       print("\033[27C\033[8B\033[91m正在加载文件...\n")
       print("\033[25C\033[107m",end="")
       for i in range(14):
            sleep(0.35)
            print("\033[107m ",end="")
       print("\033[?25l")
    sleep(3);
    print("\033[000m")
    mane()
except Exception as e:
    qing()
    error(e)