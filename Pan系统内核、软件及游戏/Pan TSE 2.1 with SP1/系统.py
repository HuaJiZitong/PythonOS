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
key=None
jsb={}               #记事本
jsbr={}              #记事本回收站
jsbrc={}             #记事本内容找回
ds_1=0
ds_2=0
ds_4=0
ds_5=0
wfp=1.5
e=2.0
obj=0
classic=0
jsb=["使用Pan TSE的记事本记录代办选项"]
ID=randint(10000,99999999)
def error(err):
    print("\033[44m")
    qing()
    for i in range(0,100,5):
        sleep(0.46)
        qing()
        print(":(")
        print("你的电脑遇到问题，需要重新启动。")
        print("我们只收集某些错误信息，然后为你重新启动。(完成"+str(i)+"%)")
        print("如果你想了解更多信息，则可以稍后在线搜索此错误:"+err)
    print("请按运行键继续...")

def qing():
    system("clear")

def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    print()

def kfz():
    global llqjh
    jsb={}               #记事本
    jsbr={}              #记事本回收站
    jsbrc={}             #记事本内容找回
    while 1:
        print("\033[0m开始                        SYSTEM")
        print("\033[95m1.命令提示符    \033[93m2.计算机      \033[92m3.记事本     \033[90m4.关机     \033[91m5.手动Ghost")
        print("\033[93mD.管理磁盘  \033[91mK.Pan激活工具(谨慎使用)")
        print("\033[0m"+strftime("%H:%M",localtime()))
        kfz=input("\033[0m请输入应用序号:")
        qing()
        if kfz=="1":
            print("\033[0mHOTM Pan[开发者版本3902]")
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
                    print("HOTM Pan[开发者版本3902]")
                    print("版权所有 (c) 2020 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3902]")
                elif dos=="bsod" or dos=="shutdown":
                    print("请稍等\n正在退出CMD")
                    break
                else:
                    print("\""+dos+"\"不是一个命令代码，请检查拼写。")
            if dos=="bsod":
                qing()
                error("Cannot perform normal shutdown")
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
        elif kfz=="K":
            b("您当前使用的系统:Pan PE")
            b("您要激活的系统:Pan TSE 2.1")
            if llqjh==0:
                msq="未激活"
            else:
                msq="已激活"
            b("激活状态:"+msq)
            b("请确认无误后按小写y键继续激活(途中可能会卸载一些软件，这是系统Bug，请想好后再继续)")
            msq=input()
            if msq=="y":
                print("正在激活Pan...")
                sleep(3)
                msq="已激活"
                key=str(randint(100,999))+"-"+str(randint(1000000,9999999))
                ds_3=0
                llqjh=1
                ds_2=0
                ds_4=0
                ds_5=0
                sleep(5)
                print("Pan TSE 2.1\n计算机已永久激活")
            else:
                print("好的，您取消了激活，如果手残按错了可以回到开始菜单重新激活。")
        elif kfz=="2":
            print("\033[0mSystem(C:)\n6.18GB可用/8.00GB")
            print("\033[0m备份Ghost(E:)\n"+str(e-0.1)+"GB可用/"+str(e)+"GB")
            print("\033[90mCD-ROM驱动器(D:)\n不可用\033[0m")
            System32=input("输入文件名，(如C:):")
            qing()
            if System32=="C:":
                print("名称    类型           修改日期               大小")
                print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1KB")
                print("WSJ     文件夹         2021年4月17日 17:56    25KB")
                print("Program 文件夹         2021年1月27日 17:10    119.9MB")
                print("local   文件夹         2020年6月14日 13:25    1.7GB")
                print(name+"   文件夹         2020年12月7日 17:54    100MB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="local":
                    print("名称    类型            修改日期               大小")
                    print("Start   软件(.exe)      2020年6月14日 13:23    1.3GB")
                    print("Touch   扩展驱动(.dll)  2020年6月14日 13:26    153MB")
                    print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                    print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                    print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                elif System32=="WSJ":
                    print("名称    类型            修改日期               大小")
                    print("Boot    安装包(.wim)    2021年4月17日 17:56    24KB")
                    print("Readme  文本(.txt)      2021年4月15日 11:26    1KB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="Readme":
                        b("本目录为莴笋尖Pan PE(月高工作室唯一指定Pan PE制作)生成的系统文件，请勿删除文件，否则会导致Pan PE无法正常运行！")
                    elif System32=="Boot":
                        print("名称    类型            修改日期               大小")
                        print("Code    直译式代码(.py) 2020年6月1日 15:07     24KB")
                        print("load    软件(.exe)      2020年7月18日 13:26    1KB")
                        print("ltemp   虚拟光驱(.iso)  2020年6月1日 15:07     0KB")
                        print("~$emp   缓存(.tmp)      2020年6月1日 15:07     0KB")
                    else:
                        print("该文件不存在或不可更改")
                elif System32=="Program":
                    print("名称    类型           修改日期               大小")
                    print("program 软件(.exe)     2020年7月19日 13:23    117MB")
                    print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                    print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
                    print("Taiwan  语言包(.bin)   2021年1月27日 17:15    1KB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32==".drives":
                        b("该服务包括:第三方程序启动服务(已启用)")
                    elif System32=="Taiwan":
                        sleep(0.2)
                        print("This program cannot run in x86 mode.")
                    else:
                        print("该文件不存在或不可更改")
                elif System32==name:
                    print("名称    类型            修改日期               大小")
                    print("user    扩展驱动(.dll)  2020年12月7日 17:56    1KB")
                    print("data    备份文件(.gho)  2020年12月7日 17:57    1KB")
                else:
                    print("该文件不存在")
            elif System32=="E:":
                print("名称    类型             修改日期               大小")
                print("Ghost   扩展驱动(.dll)   2020年7月18日  19:38    53MB")
                print("PanTSE2 系统安装包(.wim) 2020年10月1日  18:59    46.5MB")
                print("readme  文本(.txt)       2020年10月1日  19:02    407.6KB")
                print("TSE21   镜像(.iso)       2020年11月26日 15:37    904KB")
                print("develop 命令文件(.bat)   2020年11月17日 11:55    1KB")
                print("data    配置文件(.ini)   2020年11月18日 0:02     1KB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="readme":
                    b("本磁盘是重置系统备份的磁盘\n")
                    b("【请勿重新格式化】\n【请勿删除文件】\n【请勿添加文件】\n")
                    b("否则，系统将永久崩溃，切记~~~~~~")
                elif System32=="develop":
                    print("您要如何查看该文件?")
                    System32=input("A.16位的CMD B.32位的CMD C.记事本")
                    qing()
                    if System32=="A":
                        print("C:\\local>taskkill /f /im program.exe")
                        print("Succeed!")
                        sleep(0.1)
                        print("C:\\local>taskkill /f /im Startup.exe")
                        print("Succeed!")
                        sleep(0.1)
                        print("E:\\>cd E:\\&cd .>data.ini")
                        print("Succeed to add a new ini file called \"data\"!")
                        sleep(2)
                        print("-------------------------")
                        print("Succeed in 2.2 seconds with return value 12")
                        print("Press anykey to continue...")
                        input()
                    elif System32=="B":
                        print("C:\\local>taskkill /f /im program.exe")
                        print("Failed!")
                        sleep(2)
                        print("-------------------------")
                        print("Error:this program(or command) cannot support with 32-bit")
                        print("Succeed in 2 seconds with return value 395768")
                        print("Press anykey to continue...")
                    elif System32=="C":
                        b("taskkill /f /im program.exe\n")
                        b("taskkill /f /im Startup.exe\n")
                        b("cd E:\\&cd .>develop.txt")
                    else:
                        print("该文件不能以程序"+System32+"来打开")
                else:
                    print("该文件不可预览")
            elif System32=="D:":
                print("该磁盘里没有可用的安装文件(setup.exe或者oemsetup.inf)，也没有可查看的文件。")
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
        elif kfz=="D":
            print("\033[0mVirtualDisk(11.6GB)")
            print("\033[90mSystem(C: 8.00GB) \033[94m备份GHOST(E: "+str(e)+"GB) 未分配("+str(wfp)+"GB)  \033[90mEFI恢复分区(0.1GB)")
            print("\033[0m光盘(0Byte)")
            print("\033[90mCD-ROM驱动器(D: 0Byte)")
            disk=input("\033[0m选择要更改的分区(填写盘符，没有盘符填名称，如E:)")
            qing()
            if disk=="C:" or disk=="D:":
                print("该分区已被组织HOTM锁定，不可更改")
                sleep(3)
                disk=input("是否继续更改?(Y|N)")
                if disk=="Y":
                    qing()
                    error("operating system not found")
                    break
                else:
                    print("好的，即将返回桌面")
            elif disk=="EFI恢复分区":
                print("A.查看文件 B.属性")
                disk=input()
                qing()
                if disk=="A":
                    print("名称    类型             修改日期               大小")
                    print("BIOS    固件(.bin)       2020年6月14日 13:23    128KB")
                    print("config  数据(.dat)       2020年7月6日 15:42     105KB")
                elif disk=="B":
                    print("EFI恢复分区")
                    print("可用空间:99.77MB")
                    print("总空间:100MB")
                else:
                    print("该操作无效。")
            elif disk=="E:":
                disk=input("A.压缩卷 B.属性 C.扩展卷\n")
                print("\033[41m")
                qing()
                if disk=="A":
                    print("欢迎使用压缩卷功能\n本功能会帮助你压缩E盘，节约出一个空闲空间")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用压缩卷\n本功能会帮助你压缩E盘，节约出一个空闲空间")
                    print("可压缩:"+str(e-0.25)+"GB\n\033[90mTIP:必须要预留一些空间供磁盘完成任务")
                    disk=input("\033[94m输入要压缩的空间:")
                    qing()
                    if float(disk)>e-0.25:
                        print("压缩后的空间太小！请重新选择！")
                    else:
                        print("正在压缩...")
                        wfp=wfp+float(disk)
                        e=e-float(disk)
                        sleep(2)
                        print("压缩成功！E盘剩余空间为"+str(e)+"GB!")
                elif disk=="B":
                    print("备份GHOST(E:)")
                    print("\033[94m可用空间:"+str(e-0.1)+"GB")
                    print("已用空间:0.1GB")
                    print("总容量:"+str(e)+"GB")
                elif disk=="C":
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大E盘")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大E盘")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！E盘剩余空间为"+str(e)+"GB!")
                else:
                    print("该操作无效。")
            elif disk=="未分配":
                disk=input("A.属性 B.与E盘合并")
                if disk=="A":
                    print("未分配")
                    print("\033[92m已准备就绪！等待分配分区中")
                    print("\033[0m总容量:"+str(wfp)+"GB")
                elif disk=="B":
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与E盘合并")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与E盘合并")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！E盘剩余空间为"+str(e)+"GB!")
            else:
                print("该磁盘不存在")
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
    global ds_3
    global ds_4
    global ds_5
    global name
    global password
    print("\033[44m")
    qing()
    print("\033[7mP\033[0;44man Setup\n==========")
    print("准备工作...\n备份文件到E盘")
    print("C:\\"+name+"\\user.dll")
    sleep(0.09)
    print("C:\\"+name+"\\data.gho")
    sleep(0.2)
    qing()
    print("\033[7mP\033[0;44man Setup\n==========")
    print("\033[107m \033[104m            Finding ISO File            [x]\033[107m \033[44m")
    print("\033[107;30m查找可安装的镜像...                          \033[40m \033[44m")
    print(" \033[40m                                             \033[44m")
    sleep(15)
    qing()
    print("\033[7mP\033[0;44man Setup\n==========")
    print("\033[107m \033[104m            Choose Operating System            [x]\033[107m \033[44m")
    print("\033[107;30m正在重装系统                                        \033[40m \033[44m\n\033[107m选择你的系统:(共找到6个镜像，3个镜像有效)"+11*" "+"\033[40m \033[44m\n\033[107mPan TSE 2.1                                         \033[40m \033[44m\n\033[107mPan TSE2原版                                        \033[40m \033[44m\n\033[107mPan Developer PE                                    \033[40m \033[44m\033[107m\n"+52*" "+"\033[40m \n\033[44m \033[40m"+51*" "+"\033[40m \033[44m")
    efi=input("\n\n\033[101m请输入(区分大小写和空格):"+27*" "+"\n\033[1A请输入(区分大小写和空格):")
    print("\033[0m")
    qing()
    if efi=="Pan TSE 2.1":
        for i in range(0,904,int(69.5)):
            print("正在解压ISO("+str(i)+"KB/904KB)")
            sleep(0.2)
            system("clear")
    elif efi=="Pan TSE2原版":
        for i in range(0,int(46.5),int(11.6)):
            print("正在解压ISO("+str(i)+"MB/46.5MB)")
            sleep(0.2)
            system("clear")
    elif efi=="Pan Developer PE":
        print("正在重置PE")
        print("重新格式化PE系统盘...")
        sleep(3)
        qing()
        print("正在重置PE")
        print("写入文件...")
        print("E:\\Ghost.dll")
        sleep(3)
        print("E:\\PanTSE2.wim")
        sleep(2.5)
        print("E:\\TSE21.iso")
        sleep(0.37)
        print("E:\\develop.bat")
        sleep(3)
        qing()
        print("正在重置PE")
        print("更改Start.exe...")
        print("Line 1409:Add \"Pan PE\"")
        sleep(0.3)
        print("Line 1273:Copy files and hide disk E:")
        sleep(2.1)
        print("Line 1492:Save the program")
        sleep(0.5)
        qing()
        print("正在重置PE")
        print("执行develop.bat...")
        sleep(2)
        system("clear")
        print("重置成功!")
    else:
        print("正在解压文件(0B/0B)")
        sleep(0.01)
        system("clear")
        print("解压WIM或ISO失败，系统中断重装!")
        sleep(0.2)
        print("正在回滚操作...")
  
    if efi=="Pan TSE 2.1" or efi=="Pan TSE2原版":
        sleep(3)
        qing()
        print("正在获取电脑配置")
        sleep(5)
        print("正在配置Pan")
        ds_2=0
        ds_3=0
        ds_4=0
        ds_5=0
        name="Setup"
        password=None
        sleep(20)
        sb=randint(0,10)#没有骂人，在这里sb是“失败”的缩写
        if sb==5:
            print("配置Pan失败，正在回滚操作")
            sleep(5)
        print("正在复制文件")
        sleep(1)
        print(r"C:\local\Start.exe")
        print(r"C:\local\Touch.dll")
        sleep(1)
        print(r"C:\local\program.exe")
        sleep(1.5)
        print(r"C:\Start.lnk")
        print(r"C:\local\Startup.exe")
        sleep(0.09)
        print(r"E:\user.dll")
        sleep(0.09)
        print(r"E:\data.gho")
        sleep(0.2)
        print("所有文件都已复制成功")
        sleep(3)
        qing()
        print("准备就绪...")
        sleep(randint(2,15)-2)
        print("\033[44m")
        qing()
        print("\033[7mP\033[37;44man Setup\n==========")
        print("\033[107m \033[104m            Preparing Pan            [x]\033[107m \033[40m \033[44m")
        print("\033[107;90m准备就绪..."+31*" "+"\033[40m \033[44m")
        print(" \033[40m"+42*" "+"\033[44m")
        sleep(2)
        qing()
        print("\033[7mP\033[37;44man Setup\n==========")
        print("\033[107m \033[104m  Registered OK  [x]\033[107m \033[44;90m")
        print("\033[107m准备完成！"+12*" "+"\033[44m\n\033[107m您的数据和用户信息成功\033[44m\n\033[107m的保存了下来，系统也重\033[44m\n\033[107m装完成，接下来您可以尽\033[44m\n\033[107m情使用Pan TSE了"+7*" "+"\033[44m\n\033[107m5秒后进入系统         ")
        sleep(5)
        qing()
def vm(mm,user):
    print("\033[0m1.Pan1.0    2.PanTO    3.Pan3.0")
    if 1:
        if 1:
            sys=input("输入虚拟机序号:")
            qing()
            if sys=="3":
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
                mm3=None
                no_wrong=0
                while mm3!=mm:
                    if no_wrong==0:
                        mm3=input("为了确保安全，请输入密码:")
                        no_wrong=1
                    else:
                        mm3=input("密码错误，请重新输入:")
                    qing()
                print("密码输入正确")
                print("\033[93mO 欢迎")
                sleep(2)
                qing()
                while 1:
                    print("\033[0m------------PAN PRO 3---------------")   
                    print(ctime())
                    print('''0.关机
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
                        print("您已通过VMware授权激活。")
                        print("\033[32m🙂  激活Pan YES")
                        print("\033[31m虚拟机上的Pan数据可能会被篡改，请注意隐私安全")
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
                        print("您的版本:Virtual 2020 3.0.2 最新版本:Virtual 2020 3.1 Beta\n您还未升级Pan,请联系您的管理员进行升级。")
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
            elif sys=="1":
                print("\033[44m")
                system("clear")
                print("                       HOTM®")
                print("                     HOTM Pan")
                print("                   Version 1.0.3")
                print(" \n \n \n \n \n \n \nCopyright <c> HOTM Workshop,2019.All rights Reserved.")
                print("HOTM is a registered trademark of HOTM Studio.")
                print("\033[0m")
                sleep(3)
                qing()
                while 1:
                    print("PAN1.0 in Virtual PC from HOTM original version")
                    print("0.Shutdown")
                    print("1.Clock")
                    print("2.Clac")
                    print("3.Control")
                    print("4.Notepad")
                    print("5.Alarm")
                    prog1=int(input(""))
                    qing()
                    if prog1==0:
                        print("_")
                        sleep(1)
                        qing()
                        print("please wait_")
                        sleep(0.01)
                        qing()
                        print("please wait\nPan is shutting down..._")
                        sleep(2)
                        break
                    elif prog1==1:
                        for i in range(10):
                            print(ctime())
                            sleep(1)
                            qing()
                    elif prog1==2:
                        num=int(input("Please Enter the First number:"))
                        ope=input("Please Enter operate mode(+,-,*,/):")
                        num2=int(input("Please Enter the Second number:"))
                        if ope=="+":
                            print(num+num2)
                        elif ope=="-":
                            print(num-num2)
                        elif ope=="*":
                            print(num*num2)
                        elif ope=="/":
                            print(str(num*num2)+" or "+str(num*num2)+"......"+str(num%num2))
                        else:
                            print("Error")
                    elif prog1==3:
                        print("🙁  Your PC is out of support")
                        print("Please update to PanNT4 or higher version,or your PC can't work.")
                    elif prog1==4:
                        print("Notepad(Enter someting,Enter\"esc\"save and exit)")
                        notepad=None
                        print("last record:\n"+notepad)
                        while notepad!="esc":
                            notepad=input()
                    elif prog1==5:
                        z("Alarm")
                        z("input time(such as 7:00)",end="")
                        time=input()
                        while strftime("%H:%M")!=alarm:
                            sleep(1)
                        print("⏳  Alarm")
                        play_mp3("lulu.mp3")
                    else:
                        print("I am sorry,the porgram is not defined")
                    sleep(5)
                    qing()
                    continue
            elif sys=="2":
                print("           🌁")
                print("       HOTM\033[91mPan\033[94mTO\033[0m")
                sleep(0.2)
                qing()
                for i in range(10):
                    print("           🌁")
                    print("       HOTM\033[91mPan\033[94mTO\033[0m")
                    print("Startup...["+"▮"*i+"]")
                    sleep(0.1)
                    qing()
                print("\033[9m?\033[91mPan\033[94mTO\033[0m\n")
                mm_to=None
                while mm_to!=mm:
                    mm_to=input("要进入系统，请先输入Pan TSE账户"+user+"的密码:")
                qing()
                print("\033[92mo 欢迎\033[0m")
                sleep(2)
                while 1:
                    print(ctime())
                    print("""0.关机
1.画图
2.闹钟
3.邮件
4.计算器
5.设置
6.系统属性""")
                    progto=input("")
                    qing()
                    if progto=="1":
                        print("您的电脑配置不支持此程序，程序已被禁用。")
                    elif progto=="0":
                        print("\033[94mo 正在关机...\033[0m")
                        break
                    elif progto=="2":
                        z("Alarm(Version1.0.1 in Pan 1.0)")
                        z("input time(such as 7:00)",end="")
                        time=input()
                        while strftime("%H:%M")!=alarm:
                            sleep(1)
                        print("⏳  Alarm")
                        play_mp3("lulu.mp3")
                    elif progto=="3":
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
                    elif progto=="4":
                        num=int(input("输入第一个数:"))
                        ope=input("输入运算符号(+,-,*,/):")
                        num2=int(input("输入第二个数:"))
                        if ope=="+":
                            print(num+num2)
                        elif ope=="-":
                            print(num-num2)
                        elif ope=="*":
                            print(num*num2)
                        elif ope=="/":
                            print(str(num*num2)+" or "+str(num*num2)+"......"+str(num%num2))
                        else:
                            print("Error")
                    elif progto=="5":
                        print("此电脑制造商:\033[3mVMware\033[0m")
                        print("电脑启用时间:2020年6月18日 技术支持有效期:2020年5月12日\n延伸技术支持:2021年12月31日",end="")
                        print("计算机名称:PanTO Virtual")
                        sleep(2)
                        print("请按任意键继续...")
                        system("read anykey")
                    elif progto=="6":
                        print("           🌁")
                        print("       HOTM\033[91mPan\033[94mTO\033[0m")
                        print("       (c)2019 HOTM workshop")
                        input("Enter键继续")
                    else:
                        print("找不到应用程序。")
                    sleep(5)
                    qing()
                    continue
llqjh=0
ds_3=0
#---------------------------------定义---------------------------------
try:
    print("\033[?25l",end="")
    su1=time()
    for i in range(3):
        print("_")
        sleep(0.2)
        qing()
        sleep(0.2)
    sleep(1)
    for i in range(randint(2,6)):
        print("           \033[101m  \033[0m\033[102m  \033[0m")
        print("           \033[104m  \033[0m\033[103m  \033[0m")
        print("\n\n"+"            \033[104m \033[100m \033[0m")
        print("            \033[100m \033[100m \033[0m")
        sleep(0.2)
        qing()
        print("           \033[101m  \033[0m\033[102m  \033[0m")
        print("           \033[104m  \033[0m\033[103m  \033[0m")
        print("\n\n"+"            \033[100m \033[104m \033[0m")
        print("            \033[100m \033[100m \033[0m")
        sleep(0.2)
        qing()
        print("           \033[101m  \033[0m\033[102m  \033[0m")
        print("           \033[104m  \033[0m\033[103m  \033[0m")
        print("\n\n"+"            \033[100m \033[100m \033[0m")
        print("            \033[100m \033[104m \033[0m")
        sleep(0.2)
        qing()
        print("           \033[101m  \033[0m\033[102m  \033[0m")
        print("           \033[104m  \033[0m\033[103m  \033[0m")
        print("\n\n"+"            \033[100m \033[100m \033[0m")
        print("            \033[104m \033[100m \033[0m")
        sleep(0.2)
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
    while name=="Administrator" or name=="guest" or name=="SYSTEM" or name==" "*len(name):
        qing()
        name=input("输入的姓名不可用，请重新输入:")
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
        if llqjh==0:
            print("\033[90m激活Pan\n输入35768以激活Pan\033[0m")
        if classic==0 or classic==2:
            if classic==2:
                print("\033[101m")
                qing()
            print("\033[0m开始                        "+name)
            print("\033[90m0.关机  \033[30m1.待机    \033[91m2.计算器")
            print("\033[31m3.记事本        \033[92m4.重启（不会丢失数据)")
            print("\033[32m5.系统属性    \033[93m6.命令提示符    \033[33m7.有道     \033[94m8.地图 ")
            print("\033[95m9.浏览器        \0330[34m10.计算机      \033[35m11.Pan系统入门 \033[96m12.应用商店")
            if ds_1==1:
                print("\033[91m13.扫雷")
            if ds_2==1:
                print("\033[33m14.Diskgenius")
            if ds_3==1:
                print("\033[94m15.VMware")
            if ds_4==1:
                print("\033[33m16.360安全卫士")
            if ds_5==1:
                print("\033[96m17.拍拍战争")
            print("\033[0m"+strftime("%H:%M",localtime()))
            prog=input("\033[0m请输入应用序号:")
        else:
            print("\033[103m")
            qing()
            print("现在是",strftime("%Y年%m月%d日 %H点%M分%S秒",localtime()))
            print("\033[90m0.关机\n\033[30m1.待机\n\033[91m2.计算器")
            print("\033[31m3.记事本\n\033[92m4.重启（不会丢失数据)")
            print("\033[32m5.系统属性\n\033[33m6.命令提示符\n\033[33m7.有道\n\033[94m8.地图 ")
            print("\033[95m9.浏览器\n\033[34m10.计算机\n\033[35m11.Pan系统入门\n\033[96m12.应用商店")
            if ds_1==1:
                print("\033[91m13.扫雷")
            if ds_2==1:
                print("\033[33m14.Diskgenius")
            if ds_3==1:
                print("\033[94m15.VMware")
            if ds_4==1:
                print("\033[33m16.360安全卫士")
            if ds_5==1:
                print("\033[96m17.拍拍战争")
            prog=input("\033[0;103m请输入应用序号:")
        
        print("\033[0m")
        qing()
        if llqjh==0:
            print("\033[90m激活Pan\n输入35768以激活Pan\033[0m")
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
            print("版权所有 ©2021 HOTM Workshop。保留所有权利。")
            print("PanTSE 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
            input("看完按Enter")
        elif prog=="6":
            print("\033[0mHOTM Pan[版本3.65.3935]")
            print("版权所有 (c) 2021 HOTM Workshop。保留所有权利。")
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
                    print("HOTM Pan[版本3.65.3935]")
                    print("版权所有 (c) 2021 HOTM Workshop。保留所有权利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3935]")
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
                error("Cannot perform normal shutdown")
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
                key=input("您当前运行的程序可能会损害您的计算机，确定继续运行吗(Y|N)")
                if key=="Y" or key=="y":
                    password_yz=input("请输入您的密码以激活:")
                    while password_yz!=password:
                        password_yz=input("\033[91m密码错误，请输入您的密码:")
                    print("\033[93mo 激活成功")
                    key=str(randint(100,999))+"-"+str(randint(1000000,9999999))
                else:
                    print("好的，您取消了激活。")
                    key=None
            ck=["c++","C++","星光工作室","霍格沃兹工作室","诺耀工作室","星斩工作室","Scratch","scratch","Python","python","css","CSS","HTML","html","Html","PHP","php","Php","javascript","js","JavaScript","JS","秦浩铭","PEN果公司","PEN果工作室","酷喵工作室","CPB防栗局","cpb防栗局","Cpb防栗局","漫威工作室","马子锦","缪子航","月高工作室","潘夕习","C语言","星河工作室","酷喵浏览器","易语言","使用须知","金恺文","帮助","陈妍悦","王铭煊","茜文"];
            f=0;

            if 1:
                system("export xterm=TERM&&clear")#不想看见编译成功
                while(1):
                    print("社区词典_酷喵搜索       dic.hotm.cn/\033[90mkumiao.url?\033[0m\n");
                    print("————————————————————————————————————————————————————\n");
                    print("                         \033[34m酷\033[94mku\033[91mmiao\033[31m喵");
                    print("                    \033[94m┌───────────────────┐");#水印
                    print("                    \033[94m│                   \033[94m│\033[000m");#防伪
                    print("                    \033[94m└───────────────────┘");
                    print("\033[4A                  \033[000m")
                    print("\033[?25h")
                    a=input("\033[94m                    |\033[0m")
                    print("\033[0m")
                    system("clear")
                    if llqjh==0:
                        print("无法连接到网页，请确认网络正常工作，再确认有没有激活Pan。")
                        a="退出"
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
                    elif a=="退出":
                        print("\033[44m")
                        system("clear")
                        print("请稍后......\n酷喵浏览器正在关闭\033[?25l");break;
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
            print("\033[0m💽 CD-ROM驱动器(D:)")
            if ds_3==1:
                print("0Byte可用/6.55GB NTFS磁盘格式")
            else:
                print("驱动器不可用 RAW磁盘格式")
            System32=input("输入文件名，(如C:):")
            qing()
            if System32=="C:":
                print("名称    类型           修改日期               大小")
                print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1KB")
                print("WSJ     文件夹         2021年4月17日 17:56    25KB")
                print("Program 文件夹         2021年1月27日 17:10    119.9MB")
                print("local   文件夹         2020年6月14日 13:25    1.7GB")
                print(name+"   文件夹         2020年12月7日 17:54    100MB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="local":
                    print("名称    类型            修改日期               大小")
                    print("Start   软件(.exe)      2020年6月14日 13:23    1.3GB")
                    print("Touch   扩展驱动(.dll)  2020年6月14日 13:26    153MB")
                    print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                    print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                    print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                elif System32=="WSJ":
                    print("名称    类型            修改日期               大小")
                    print("Boot    安装包(.wim)    2021年4月17日 17:56    24KB")
                    print("Readme  文本(.txt)      2021年4月15日 11:26    1KB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="Readme":
                        b("本目录为莴笋尖Pan PE(月高工作室唯一指定Pan PE制作)生成的系统文件，请勿删除文件，否则会导致Pan PE无法正常运行！")
                    elif System32=="Boot":
                        print("名称    类型            修改日期               大小")
                        print("Code    直译式代码(.py) 2020年6月1日 15:07     24KB")
                        print("load    软件(.exe)      2020年7月18日 13:26    1KB")
                        print("ltemp   虚拟光驱(.iso)  2020年6月1日 15:07     0KB")
                        print("~$emp   缓存(.tmp)      2020年6月1日 15:07     0KB")
                    else:
                        print("该文件不存在或不可更改")
                elif System32=="Program":
                    print("名称    类型           修改日期               大小")
                    print("program 软件(.exe)     2020年7月19日 13:23    117MB")
                    print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                    print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
                    print("Taiwan  语言包(.bin)   2021年1月27日 17:15    1KB")
                    print("Notes   数据(.dat)     2020年6月30日 23:31    1KB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32==".drives":
                        b("该服务包括:第三方程序启动服务(已启用)")
                    elif System32=="Taiwan":
                        sleep(0.2)
                        print("This program cannot run in x64 mode.")
                    else:
                        print("该文件不存在或不可更改")
                elif System32==name:
                    print("名称    类型            修改日期               大小")
                    print("user    扩展驱动(.dll)  2020年12月7日 17:56    1KB")
                    print("data    备份文件(.gho)  2020年12月7日 17:57    1KB")
                else:
                    print("该文件不存在")
            elif System32=="D:" and ds_3==1:
                print("名称    类型            修改日期               大小")
                print("autorun 安装信息(.inf)  2021年1月25日 16:58    1KB")
                print("icon    图标(.ico)      2015年7月18日 13:26    5KB")
                print("Pan 3.0 软盘文件(.img)  2020年9月25日 13:27    3.71GB")
                print("Pan TO  软盘文件(.img)  2020年9月25日 13:30    1.86GB")
                print("Pan103  软盘文件(.flp)  2020年9月25日 13:31    956MB")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="autorun":
                    b("[autorun]\nICON=icon.ico,0")
                elif System32=="Pan 3.0":
                    print("名称    类型            修改日期               大小")
                    print("Pan 3.0 虚拟机配置(.vmx)2021年1月25日 16:58    4KB")
                    print("Pan 3.0 磁盘驱动(.vmdk) 2020年7月18日 13:26    3.70GB")
                elif System32=="Pan TO":
                    print("名称    类型            修改日期               大小")
                    print("Pan TO  虚拟机配置(.vmx)2021年1月25日 16:58    4KB")
                    print("Pan TO  磁盘驱动(.vmdk) 2020年7月18日 13:26    1.85GB")
                elif System32=="Pan103":
                    print("名称    类型            修改日期               大小")
                    print("Pan103  虚拟机配置(.vmx)2021年1月25日 16:58    4KB")
                    print("Pan103  磁盘驱动(.vmdk) 2020年7月18日 13:26    955MB")
                else:
                    print("该文件不存在或不可更改")
            else:
                if System32=="D:":
                    print("无法读取这个磁盘，请检查磁盘是否被拔出或移动，再检查是否安装磁盘管理软件。")
                else:
                    print("该磁盘不存在")
        elif prog=="11":
            print("\033[0m1.开机和登录 2.软件 3.浏览器问题 4.升级Pan 5.重装系统")
            rm=input()
            qing()
            if rm=="1":
                b("1)360报告卡顿现象\n清理电脑垃圾或重启机器即可，如问题严重，请换个浏览器(推荐Chrome)或重装系统(推荐win7，iPadOS)。\n2)基本信息可以不填么?\n可以，但是最好填(也可以在开始菜单打开命令提示符输入modify更改)，姓名栏可以写您的真实名字，也可以写您的昵称。")
                b("\n3)用电脑能正常运行PanTSE吗?\n能，系统最好xp以上，如果只想体验触摸系统(平板系统)，建议使用iPad\n4)为什么我一启动机器就会报告蓝屏?\n可能是您在开机时输入了一些东西或者系统发生了一些小错误导致的，如果问题严重，可以降级到PanNT4")
                b("\n5)为什么我输入自己的密码提示错误?\n可能您拼写不正确或别人更改了您的密码，重启机器即可解决。")
            elif rm=="2":
                b("0功能，关闭机器\n1功能，休眠，您可以在这时候放松一下，放松完按Enter键重新进入开始菜单\n2功能，计算器，解决生活中的数学问题，如果您在做作业，不建议这样做。")
                b("3功能，记事本，将一天要做的事记录下来，Pan会帮你存储到c盘中。\n4功能，重启，如果您的机器遇到问题可以打开此功能，如果是大问题，请按停止键再按运行键。\n5功能，系统属性，可以查看系统的基本信息。(也可以在命令提示符输入panver查看版本)\n")
                b("6功能，MS-DOS，现在改名为CMD,用在一些专业的行业当中\n7功能，有道，可以轻松翻译英，韩，日，中四国语言\n8功能，地图，如果迷路了，可以通过它来找到回家的路(前提是你得有钱坐公交)\n")
                b("9功能，浏览器，运行正式版会崩，所以这里统一用极速版了(酷喵的，已经授权了)\n10功能，计算机(我可不是2功能哦)，类似于PanNT4的\"我的电脑\"\n11功能就是我啦，可以给刚刚入坑的Pan小白一些帮助\n12功能，应用商店，可以购买应用或找回已卸载的原生应用")
            elif rm=="3":
                b("1)在浏览器运行过程中蓝屏了怎么办?\n进入TSE的源码http://code.xueersi.com/ide/code/6421076找到【浏览器】的脚本，更改一下出错源码位置，或者重新按运行键\n")
                b("2)总是提醒该词条不存在是怎么肥事?\n检查拼写是否正确或者输入\"帮助\"看看浏览器里面都有什么词条。\n")
                b("3)超长了怎么办?\n重按运行键即可。\n4)为什么浏览器退不出来?\n等浏览器返回到主页，输入\"退出\"即可。")
            elif rm=="4":
                b("如果您的电脑运行的是已经停止支持的Pan2.0或者是即将停止支持的Pan3.0，我们建议您升级到Pan2020及以上版本，谢谢配合！")
            elif rm=="5":
                setup()
                print("\033[0m")
            else:
                print("该章节不存在")
        elif prog=="12":
            print("\033[42m")
            qing()
            print("A.💣  扫雷  \033[41m原生\033[42m")
            print("B.💾  Diskgenius")
            print("C.💻  VMware Workstation 16")
            print("D.💼  360安全卫士")
            print("E.👋  拍拍战争")
            prog=input("输入想安装的应用的字母:")
            qing()
            if prog=="A" and ds_1==0:
                print("             💣  扫雷")
                print("              HOGWARS")
                print("识别为被删除的原生应用！是否恢复(Y|N)")
                if input()=="Y":
                    qing()
                    print("正在恢复(更改program.exe)...")
                    sleep(3)
                    print("正在恢复(创建快捷方式)...")
                    sleep(0.5)
                    print("恢复成功！可在开始菜单查看！")
                    ds_1=1
                else:
                    qing()
                    print("好的，您取消了操作。")
            elif prog=="B" and ds_2==0:
                print("       💾  Diskgenius")
                print("         易之数软件")
                print("√HOTM检测通过 √HOGWARS检测通过")
                print("是否安装(Y|N)")
                if input()=="Y":
                    qing()
                    print("正在安装(更改program.exe)...")
                    sleep(3)
                    print("正在安装(创建快捷方式)...")
                    sleep(0.5)
                    print("安装成功！可在开始菜单查看！")
                    ds_2=1
                else:
                    qing()
                    print("好的，您取消了操作。")
            elif prog=="C" and ds_3==0:
                print("         💻  VMware")
                print("          威睿科技")
                print("√HOTM检测通过 √HOGWARS检测通过")
                print("是否安装(Y|N)")
                if input()=="Y":
                    qing()
                    print("正在安装(更改program.exe)...")
                    sleep(3)
                    print("正在安装(创建快捷方式)...")
                    sleep(0.5)
                    print("安装成功！可在开始菜单查看！")
                    ds_3=1
                else:
                    qing()
                    print("好的，您取消了操作。")
            elif prog=="D" and ds_4==0:
                print("         💼  360安全卫士")
                print("            奇虎科技")
                print("√HOTM检测通过 √HOGWARS检测通过")
                print("是否安装(Y|N)")
                if input()=="Y":
                    qing()
                    print("正在安装(更改program.exe)...")
                    sleep(3)
                    print("正在安装(创建快捷方式)...")
                    sleep(0.5)
                    print("安装成功！可在开始菜单查看！")
                    ds_4=1
                else:
                    qing()
                    print("好的，您取消了操作。")
            elif prog=="E" and ds_5==0:
                print("         👋 拍拍战争")
                print("       RongChen's group")
                print("√HOTM检测通过 √HOGWARS检测通过")
                print("是否安装(Y|N)")
                if input()=="Y":
                    qing()
                    print("正在安装(更改program.exe)...")
                    sleep(3)
                    print("正在安装(创建快捷方式)...")
                    sleep(0.5)
                    print("安装成功！可在开始菜单查看！")
                    ds_5=1
                else:
                    qing()
                    print("好的，您取消了操作。")
        elif prog=="13" and ds_1==1:
            if 1:
                print("9*9扫雷")
                checkerboard = [0,"01","02","03","04","05","06","07","08","09"]
                for i in range(10,82) :
                    checkerboard += [str(i)]
                mode = input("1.入门(6个雷) 2.简单(8个雷) 3.普通(10个雷) 4.困难(12个雷) 5.超难(15个雷) 6.自定义(1~80个雷)")
                set_comp = False
                isyou = True
                set_zone = 0
                set_mine = 0
                game_res = 0
                dig = [True] + ([False] * 81)
                game_checkwin = 0
                def showcheckerboard() :
                    system("clear")
                    for i in range(9) :
                        for i2 in range(1,9) :
                            if "\033[3" in checkerboard[i*9+i2] :
                                print(checkerboard[i*9+i2],end="\033[0m ")
                            else :
                                print(checkerboard[i*9+i2],end=" ")
                        if "\033[3" in checkerboard[i*9+i2] :
                            print(checkerboard[i*9+9] + "\033[0m")
                        else :
                            print(checkerboard[i*9+9])
                def do_dig(zone) :
                    global game_res
                    global mine
                    if mine[zone] == 1 :
                        print("你挖到雷了!")
                        print("游戏结束")
                        game_res = 2
                    else :
                        global dig
                        global checkerboard
                        global isyou
                        dig[zone] = True
                        if zone == 1 :
                            if checkerboard[1] == "01" :
                                if mine[2] + mine[10] + mine[11] == 0 :
                                    checkerboard[1] = "  "
                                    isyou = False
                                    do_dig(2)
                                    do_dig(10)
                                    do_dig(11)
                                else :
                                    checkerboard[1] = "\033[34mM" + str(mine[2] + mine[10] + mine[11])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 9 :
                            if checkerboard[9] == "09" :
                                if mine[8] + mine[17] + mine[18] == 0 :
                                    checkerboard[9] = "  "
                                    isyou = False
                                    do_dig(8)
                                    do_dig(17)
                                    do_dig(18)
                                else :
                                    checkerboard[9] = "\033[34mM" + str(mine[8] + mine[17] + mine[18])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 73 :
                            if checkerboard[73] == "73" :
                                if mine[64] + mine[65] + mine[74] == 0 :
                                    checkerboard[73] = "  "
                                    isyou = False
                                    do_dig(64)
                                    do_dig(65)
                                    do_dig(74)
                                else :
                                    checkerboard[73] = "\033[34mM" + str(mine[64] + mine[65] + mine[74])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 81 :
                            if checkerboard[81] == "81" :
                                if mine[71] + mine[72] + mine[80] == 0 :
                                    checkerboard[81] = "  "
                                    isyou = False
                                    do_dig(71)
                                    do_dig(72)
                                    do_dig(80)
                                else :
                                    checkerboard[81] = "\033[34mM" + str(mine[71] + mine[72] + mine[80])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [2,3,4,5,6,7,8] :
                            if checkerboard[zone] == ("0" + str(zone)) :
                                if mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [10,19,28,37,46,55,64] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 9] + mine[zone - 8] + mine[zone + 1] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone + 1)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 9] + mine[zone - 8] + mine[zone + 1] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [74,75,76,77,78,79,80] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [18,27,36,45,54,63,72] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 1] + mine[zone + 8] + mine[zone + 9] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 1] + mine[zone + 8] + mine[zone + 9])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        else :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                    if game_res == 0 :
                        game_checkwin = 0
                        for i in range(1,82) :
                            if dig[i] != mine[i] :
                                game_checkwin = game_checkwin + 1
                        if game_checkwin == 81 :
                            showcheckerboard()
                            print("胜利!")
                            print("游戏结束")
                            game_res = 1
                if mode == "1" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 6 :
                            if randint(1,81) <= 6 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 6 :
                            set_comp = True
                elif mode == "2" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 8 :
                            if randint(1,81) <= 8 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 8 :
                            set_comp = True
                elif mode == "3" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 10 :
                            if randint(1,81) <= 10 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 10 :
                            set_comp = True
                elif mode == "4" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 12 :
                            if randint(1,81) <= 12 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 12 :
                            set_comp = True
                elif mode == "5" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 15 :
                            if randint(1,81) <= 15:
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 15 :
                            set_comp = True
                else :
                    mine2 = input("输入雷数(1~80)")
                    try :
                        int(float(mine2))
                    except :
                        print("错误:非整数")
                    else :
                        mine2 = int(float(mine2))
                        if mine2 > 80 :
                            print("错误:雷数太高(最高为80)")
                        elif mine2 < 1 :
                            print("错误:雷数太低(最低为1)")
                        else :
                            while set_comp == False :
                                set_zone = 0
                                set_mine = 0
                                mine = [0] * 82
                                while set_zone < 81 and set_mine < mine2 :
                                    if randint(1,81) <= mine2 :
                                        mine[set_zone + 1] = 1
                                        set_mine = set_mine + 1
                                    set_zone = set_zone + 1
                                if set_mine == mine2 :
                                    set_comp = True
                while game_res == 0 :
                    showcheckerboard()
                    isyou = True
                    game_setzone = input("\033[0m请输入操作格(01~81)")
                    try :
                        int(float(game_setzone))
                    except :
                        print("请输入正确的数字!")
                        sleep(0.5)
                    else :
                        if int(game_setzone) in list(range(1,82)) :
                            game_zonectrl = input("请选择操作 1.挖土 2.标旗/取消标旗 3.重选操作格")
                            if game_zonectrl == "1" :
                                game_setzone = int(float(game_setzone))
                                do_dig(game_setzone)
                            elif game_zonectrl == "2" :
                                if checkerboard[int(game_setzone)] == game_setzone :
                                    checkerboard[int(game_setzone)] = "\033[31m" + game_setzone
                                elif checkerboard[int(game_setzone)] == "\033[31m" + game_setzone :
                                    checkerboard[int(game_setzone)] = game_setzone
                                else :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        else :
                            print("请输入正确的数字!")
                            sleep(0.5)
        elif prog=="14" and ds_2==1:
            print("\033[0mVirtualDisk(11.6GB)")
            print("\033[94mSystem(C: 8.00GB) \033[94m备份GHOST(X: "+str(e)+"GB) 未分配("+str(wfp)+"GB)  \033[90mEFI恢复分区(ESP: 0.1GB)")
            print("\033[90mCD-ROM驱动器(0Byte)")
            print("CD-ROM驱动器(D: 0Byte)")
            disk=input("\033[0m选择要更改的分区(填写盘符，没有盘符填名称，如E:)")
            qing()
            if disk=="C:" :
                print("A.属性 B.重新格式化")
                disk=input()
                qing()
                if disk=="A":
                    b("System(C:)")
                    b("类型:本地磁盘 文件系统:NTFS")
                    b("可用空间:6.18GB 总空间:8.00GB")
                elif disk=="B":
                    disk=input("你确定要格式化吗(Y|N)?")
                    qing()
                    if disk=="Y":
                        print("正在格式化...")
                        sleep(3)
                        print("格式化成功，重启生效")
                        sleep(2)
                        print("检测到C盘内无系统，自动切换到安装系统模式")
                        sleep(0.01)
                        setup()
                    else:
                        print("好的，您取消了格式化")
                else:
                    print("该操作无效。")
            elif disk=="ESP:":
                print("A.查看文件 B.属性")
                disk=input()
                qing()
                if disk=="A":
                    print("名称    类型             修改日期               大小")
                    print("BIOS    固件(.bin)       2020年6月14日 13:23    128KB")
                    print("config  数据(.dat)       2020年7月6日 15:42     105KB")
                elif disk=="B":
                    b("EFI恢复分区(ESP:)")
                    b("类型:本地磁盘 文件系统:FAT32")
                    b("可用空间:99.77MB")
                    b("总空间:100MB")
                else:
                    print("该操作无效。")
            elif disk=="X:":
                disk=input("A.压缩卷 B.属性 C.扩展卷\n")
                print("\033[41m")
                qing()
                if disk=="A":
                    print("欢迎使用压缩卷功能\n本功能会帮助你压缩X盘，节约出一个空闲空间")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用压缩卷\n本功能会帮助你压缩X盘，节约出一个空闲空间")
                    print("可压缩:"+str(e-0.25)+"GB\n\033[90mTIP:必须要预留0.25GB空间供磁盘有能力完成基本任务")
                    disk=input("\033[94m输入要压缩的空间:")
                    qing()
                    if float(disk)>e-0.25:
                        print("压缩后的空间太小！请重新选择！")
                    else:
                        print("正在压缩...")
                        wfp=wfp+float(disk)
                        e=e-float(disk)
                        sleep(2)
                        print("压缩成功！X盘剩余空间为"+str(e)+"GB!")
                elif disk=="B":
                    print("备份GHOST(X:)")
                    print("\033[94m可用空间:"+str(e-0.1)+"GB")
                    print("已用空间:0.1GB")
                    print("总容量:"+str(e)+"GB")
                elif disk=="C":
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大X盘")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大X盘")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！X盘剩余空间为"+str(e)+"GB!")
                else:
                    print("该操作无效。")
            elif disk=="未分配":
                disk=input("A.属性 B.与X盘合并")
                if disk=="A":
                    print("未分配")
                    print("\033[92m已准备就绪！等待分配分区中")
                    print("\033[0m总容量:"+str(wfp)+"GB")
                elif disk=="B":
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与X盘合并")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与X盘合并")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！X盘剩余空间为"+str(e)+"GB!")
            else:
                print("该磁盘不存在")
        elif prog=="15" and ds_3==1:
            vm(password,name)
        elif prog=="16" and ds_4==1:
            while 1:
                a360=input("1.我的电脑 2.软件管家 X.退出")
                qing()
                if a360=="1":
                    print("\033[32m+===============欢迎使用360电脑性能测试机===============+")
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
                            yanshi = str(t_c2)+"秒，您的延时非常长，说明网络非常差，建议您进行360网络诊断。"
                        elif t_c2 > 0.12:
                            yanshi = str(t_c2)+"秒，您的延时极长，说明网络极差。"
                        elif t_c2 > 0.01:
                            yanshi = str(t_c2)+"秒，您的延时较长，说明网络有点差。"
                        elif t_c2 > 0.004:
                            yanshi = str(t_c2)+"秒，您的延时有一点点长，可能是卡顿问题，此为正常~"
                        elif t_c2 <= 0.002:
                            yanshi = str(t_c2)+"秒，您的延时非常正常，继续保持哦~"
                        else:
                            yanshi = str(t_c2)+"秒，无法识别类型~"
                    elif t_c == 1:
                        yanshi = "太棒啦，您的电脑没有延时~"
                    elif t_c < 1:
                        yanshi = "您的电脑太快啦，比Pan系统运行速度还快，快到无法shi。"
                    else:
                        yanshi = "fail(测试失败)"
                    #测登录
                    qing()
                    print("\033[33m延时:测试完成")
                    print("\033[36m登录:测试中...")
                    print("\033[34m版本:等待中...")
                    print("\033[35m更多:敬请期待\033[8m")
                    if name:
                        tryy = "您已创建账号并登录"
                    else:
                        tryy = "您没有账号或没有登录"
                    #测更新
                    qing()
                    print("\033[0m\033[33m延时:测试完成")
                    print("\033[36m登录:测试完成")
                    print("\033[34m版本:测试中...")
                    print("\033[35m更多:敬请期待\033[0m")
                    ce3 = "Pan版本:最新版本 python编译器版本:{} 您的系统:{}{}".format(sys.version[0:5],platform.platform(),platform.architecture()[0])
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
                    input("\033[31mEnter返回主页")
                elif a360=="2":
                    if ds_2==1:
                        print("1.💾 Diskgenius \033[93m5星/5星\033[0m19.17MB")
                    if ds_3==1:
                        print("2.💻 VMware Workstation 16\033[93m4.5星/5星\033[0m6.61GB")
                    if ds_4==1:
                        print("3.💼 360安全卫士\033[93m1.4星/5星\033[0m18.19MB")
                    if ds_5==1:
                        print("4.👋 拍拍战争\033[93m3.9星/5星\033[0m2.8MB")
                    a360=input("输入要卸载的程序的序号:")
                    qing()
                    print("正在卸载...")
                    if a360=="1":
                        ds_2=0
                    elif a360=="2":
                        ds_3=0
                    elif a360=="3":
                        ds_4=0
                    elif a360=="4":
                        ds_5=0
                    else:
                        print("程序不存在或已经卸载")
                elif a360=="X":
                    break
                else:
                    print("该选项不存在")
                sleep(3)
                qing()
                continue
        elif prog=="17" and ds_5==1:
            print("\033[93m通知:这不是玩游戏的最佳分辨率，最佳分辨率是1366×768")
            while 1:
                pp=input("(X键退出)\033[91mA.单人赛 \033[92mB.生存大乱斗 \033[93mC.v0.13公测体验 \033[93mE.玩法说明\033[0m")
                qing()
                if pp=="A":
                    m=1
                    m_d=1
                    d=0
                    d_d=0
                    df=0
                    xl=0
                    xl_d=0
                    print("你("+str(ID)+") VS 正在匹配...")
                    sleep(3)
                    qing()
                    print("你("+str(ID)+") VS 用户"+str(randint(10000,99999999)))
                    sleep(1)
                    qing()
                    while m!=0 and m_d!=0:
                        print("A.防御 B.蓄力",end="")
                        if d>0:
                            print(" C.打一枪",end="")
                        pp=input()
                        qing()
                        if pp=="A":
                            pp="防御"
                        elif pp=="B":
                            pp="蓄力"
                            xl=xl+1
                            d=d+1
                        elif pp=="C" and d>0:
                            pp="打枪"
                            d=d-1
                            xl=0
                        else:
                           pp="防御" 
                        print("你:"+pp)
                        df=randint(1,3)
                        if df==3 and xl_d==0:
                            while df==3:
                                df=randint(1,3)
                        if df==1:
                            df="防御"
                        elif df==2:
                            df="蓄力"
                            xl_d=xl_d+1
                            d_d=d_d+1
                        elif df==3 and d_d>0:
                            df="打枪"
                            d_d=d_d-1
                            xl_d=0
                        else:
                           df="防御" 
                        sleep(uniform(2.0,5.0))
                        print("对方:"+str(df))
                        if pp=="蓄力" and df=="打枪":
                            m=0
                            print("你死了！")
                        if pp=="打枪" and df=="蓄力":
                            m_d=0
                            print("祝贺你，打倒了对方！")
                        if pp=="打枪" and df==pp:
                            m=0
                            m_d=0
                            print("平局！")
                        sleep(3)
                        qing()
                elif pp=="C":
                    m=1
                    m_d=1
                    df=0
                    print("你("+str(ID)+") VS 正在匹配...")
                    sleep(3)
                    qing()
                    print("你("+str(ID)+") VS 用户"+str(randint(10000,99999999)))
                    sleep(1)
                    qing()
                    while m!=0 and m_d!=0:
                        print("A.金神 B.木神 C.水神 D.火神 E.土神 F.风神 G.电神")
                        pp=input()
                        qing()
                        if pp=="A":
                            pp="金神"
                        elif pp=="B":
                            pp="木神"
                        elif pp=="C":
                            pp="水神"
                        elif pp=="D":
                            pp="火神"
                        elif pp=="E":
                            pp="土神"
                        elif pp=="F":
                            pp="风神"
                        elif pp=="G":
                            pp="电神"
                        else:
                           pp="木神" 
                        print("你:"+pp)
                        df=randint(1,7)
                        if df==1:
                            df="金神"
                        elif df==2:
                            df="木神"
                        elif df==3:
                            df="水神"
                        elif df==4:
                            df="火神"
                        elif df==5:
                            df="土神"
                        elif df==6:
                            df="风神"
                        elif df==7:
                            df="电神"
                        else:
                           df="木神"
                        sleep(uniform(2.0,5.0))
                        print("对方:"+str(df))
                        if (pp=="金神" and df=="木神") or (pp=="木神" and df=="土神") or (pp=="土神" and df=="水神") or (pp=="水神" and df=="火神") or (pp=="火神" and df=="金神") or (pp=="水神" and df=="电神") or (pp=="风神" and df=="火神") or (pp=="电神" and df=="风神"):
                            m_d=0
                            print("祝贺你，打倒了对方！")
                        elif (df=="金神" and pp=="木神") or (df=="木神" and pp=="土神") or (df=="土神" and pp=="水神") or (df=="水神" and pp=="火神") or (df=="火神" and pp=="金神") or (df=="水神" and pp=="电神") or (df=="风神" and pp=="火神") or (df=="电神" and pp=="风神"):
                            m=0
                            print("你死了！")
                        else:
                            pass
                        sleep(3)
                        qing()
                elif pp=="B":
                    fi=0
                    m=[1,1,1,1,1,1]
                    d=[0,0,0,0,0,0]
                    df=[0,0,0,0,0,0]
                    xl=[0,0,0,0,0,0]
                    cp=[None,None,None,None,None,None]
                    cp2=[None,None,None,None,None,None]
                    cp3=[None,None,None,None,None,None]
                    idf=randint(1,5)
                    print("你是"+str(idf)+"号玩家")
                    print("你("+str(ID)+")  正在匹配(0) 正在匹配(0) 正在匹配(0) 正在匹配(0)")
                    sleep(5)
                    qing()
                    print("你是"+str(idf)+"号玩家")
                    print("你("+str(ID)+")  用户"+str(randint(10000,99999999))+" 用户"+str(randint(10000,99999999))+" 用户"+str(randint(10000,99999999))+" 用户"+str(randint(10000,99999999)))
                    sleep(3)
                    qing()
                    while m.count(1)>1:
                        qing()
                        print("你是"+str(idf)+"号玩家")
                        print("A.防御 B.蓄力",end="")
                        if d[idf]>0:
                            print(" C.打一枪",end="")
                            if d[idf]>=2:
                                print("D.打两枪",end="")
                            if d[idf]>=3:
                                print("E.打三枪",end="")
                        pp=input()
                        qing()
                        print("针对几号位要填数字！")
                        if pp=="A":
                            pp="防御"
                        elif pp=="B":
                            pp="蓄力"
                            xl[idf]=xl[idf]+1
                            d[idf]=d[idf]+1
                        elif pp=="C" and d[idf]>0:
                            pp="打枪"
                            d[idf]=d[idf]-1
                            xl[idf]=0
                            cp[idf]=input("针对几号位:")
                            if cp[idf]==idf:
                                print("不能针对自己！已自动切换为防御！")
                                pp="防御"
                        elif pp=="D" and d[idf]>1:
                            pp="两枪"
                            d[idf]=d[idf]-2
                            xl[idf]=0
                            cp[idf]=input("针对几号位:")
                            cp2[idf]=input("还需要针对几号位(没有可以不填):")
                            if cp[idf]==idf or cp2[idf]==idf:
                                print("不能针对自己！已自动切换为防御！")
                                pp="防御"
                        elif pp=="E" and d[idf]>2:
                            pp="三枪"
                            d[idf]=d[idf]-3
                            xl[idf]=0
                            cp[idf]=input("针对几号位:")
                            cp2[idf]=input("还需要针对几号位(没有可以不填):")
                            cp3[idf]=input("还需要针对几号位(没有可以不填):")
                            if cp[idf]==idf or cp2[idf]==idf or cp3[idf]==idf:
                                print("不能针对自己！已自动切换为防御！")
                                pp="防御"
                        else:
                           pp="防御" 
                        qing()
                        print("你是"+str(idf)+"号玩家")
                        print("你:",end="")
                        if "枪" in pp:
                            print("针对",cp[idf],cp2[idf],cp3[idf],"号玩家发起",end="")
                        print(pp)
                        for i in range(1,6):
                            if i!=idf and m[i]!=0:
                                df[i]=randint(1,5)
                                if (df[i]==3 or df[i]==4 or df[i]==5) and d[i]==0:
                                    while df[i]!=3 and df[i]!=4 and df[i]!=5:
                                        df[i]=randint(1,5)
                                if df[i]==1:
                                    df[i]="防御"
                                elif df[i]==2:
                                    df[i]="蓄力"
                                    xl[i]=xl[i]+1
                                    d[i]=d[i]+1
                                elif df[i]==3 and d[i]>0:
                                    df[i]="打枪"
                                    d[i]=d[i]-1
                                    xl[i]=0
                                    cp[i]=randint(1,5)
                                    if cp[i]==i:
                                        df[i]="防御"
                                elif df[i]==4 and d[i]>1:
                                    df[i]="两枪"
                                    d[i]=d[i]-2
                                    xl[i]=0
                                    cp[i]=randint(1,5)
                                    cp2[i]=randint(0,5)
                                    if cp[i]==i or cp2[i]==i:
                                        df[i]="防御"
                                elif df[i]==5 and d[i]>2:
                                    df[i]="三枪"
                                    d[i]=d[i]-3
                                    xl[i]=0
                                    cp[i]=randint(1,5)
                                    cp2[i]=randint(0,5)
                                    cp3[i]=randint(0,5)
                                    if cp[i]==i or cp3[i]==i or cp2[i]==i:
                                        df[i]="防御"
                                else:
                                   df[i]="防御" 
                        sleep(uniform(2.0,5.0))
                        for i in range(1,6):
                            if i!=idf and m[i]!=0:
                                print(str(i)+"号玩家:",end="")
                                if "枪" in df[i]:
                                    print("针对",cp[i],cp2[i],cp3[i],"号玩家发起",end="")
                                print(df[i])
                                if df[i]=="打枪" and df[cp[i]]=="蓄力":
                                    m[cp[i]]=0
                                    print(str(cp[i])+"号玩家出局！")
                                    if df[cp[i]]=="两枪" or df[cp[i]]=="三枪":
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                if df[i]=="两枪" and (df[cp[i]]=="蓄力" or df[cp[i]]=="打枪"):
                                    m[cp[i]]=0
                                    print(str(cp[i])+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp[cp[i]]==i or cp2[cp[i]]==i or cp3[cp[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp2[cp2[i]]==i or cp[cp2[i]]==i or cp3[cp2[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp[cp3[i]]==i or cp2[cp3[i]]==i or cp3[cp3[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                if df[i]=="两枪" and (df[cp2[i]]=="蓄力" or df[cp2[i]]=="打枪"):
                                    m[cp2[i]]=0
                                    print(str(cp2[i])+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp2[cp2[i]]==i or cp[cp2[i]]==i or cp3[cp2[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp[cp3[i]]==i or cp2[cp3[i]]==i or cp3[cp3[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                    if df[cp[i]]=="三枪" and (cp[cp[i]]==i or cp2[cp[i]]==i or cp3[cp[i]]==i):
                                        m[i]=0
                                        print(str(i)+"号玩家出局！")
                                if df[i]=="三枪" and (df[cp2[i]]=="蓄力" or df[cp2[i]]=="打枪" or df[cp2[i]]=="两枪"):
                                    m[cp2[i]]=0
                                    print(str(cp2[i])+"号玩家出局！")
                                if df[i]=="三枪" and (df[cp[i]]=="蓄力" or df[cp[i]]=="打枪" or df[cp[i]]=="两枪"):
                                    m[cp[i]]=0
                                    print(str(cp[i])+"号玩家出局！") 
                                if df[i]=="三枪" and (df[cp3[i]]=="蓄力" or df[cp3[i]]=="打枪" or df[cp3[i]]=="两枪"):
                                    m[cp3[i]]=0
                                    print(str(cp3[i])+"号玩家出局！")
                        for i in range(1,6):
                            if cp[i]==idf or cp2[i]==idf or cp3[i]==idf:
                                if df[i]=="三枪" and (pp=="蓄力" or pp=="打枪" or pp=="两枪") :
                                    print("你被打死了")
                                    fi=1
                                    break
                                if df[i]=="两枪" and (pp=="蓄力" or pp=="打枪"):
                                    print("你被打死了")
                                    fi=1
                                    break
                                if df[i]=="打枪" and pp=="蓄力":
                                    print("你被打死了")
                                    fi=1
                                    break
                        sleep(5)
                        if fi==1:
                            break
                    if m[idf]==1:
                        print("你赢了！")
                elif pp=="E":
                    b("单人赛玩法")
                    b("防御:游戏中敲A代表防御，此功能可以免受一次打枪\n蓄力:游戏中敲B代表蓄力，此功能可以制造一枚枪的子弹\n打枪:游戏中敲C代表打枪，每次只能打一枚子弹，且需要一次蓄力来制造一枚子弹，此功能可以攻击对方。")
                    b("如果你出枪，对方出蓄力，你赢了。相反则是你输了。如果两人都出枪，那么就是平局。")
                    b("大乱斗玩法")
                    b("大乱斗可以连续开2、3枪。两枪可以攻击针对你想针对的玩家，两枪可以攻破蓄力和一枪。三枪则可以攻破所有技能")
                elif pp=="X":
                    break
                else:
                    print("开发中，敬请期待。")
                input("Enter键继续")
                sleep(3)
                qing()
                continue
        elif prog=="35768":
            while 1:
                print("\033[0m\033[7m            Pan启动管理器            ")
                print("\033[0m选择要更改的选项")
                print("\nA.切换系统")
                print("B.Settings")
                print("退出选项在Settings里面")
                prog=input()
                qing()
                if prog=="A":
                    qing()
                    sleep(2)
                    print("\033[7m            Pan启动管理器            ")
                    print("\033[0m选择要更改的选项")
                    print("\nA.Pan TSE 2")
                    print("B.Pan PE")
                    prog=input()
                    if prog=="B":
                        obj=1
                        break
                    else:
                        qing()
                        break
                elif prog=="B":
                    print("\033[7m        Pan启动管理器            ")
                    print("\033[0m选择要更改的选项")
                    print("\nA.重置系统")
                    print("B.系统属性\nC.声音\nD.显示\nE.时间\nF.个性化主题\nG.激活Pan\nX.退出")
                    if llqjh==0:
                        b("\033[91m个性化设置没有开通，因为你尚未激活Pan\033[0m")
                    prog=input()
                    qing()
                    print("\033[7m        Pan启动管理器            ")
                    print("\033[0m",end="")
                    if prog=="A":
                        print("正在恢复......")
                        name=None
                        password=None
                        key=None
                        ds_2=0
                        ds_3=0
                        ds_4=0
                        ds_5=0
                        sleep(2)
                        print("恢复成功！开始重启...")
                        sleep(3)
                        qing()
                        for i in range(3):
                            print("_")
                            sleep(0.2)
                            qing()
                            sleep(0.2)
                        sleep(1)
                        for i in range(randint(2,6)):
                            for j in range(10):
                                print("        \033[101m  \033[0m\033[102m  \033[0m")
                                print("        \033[104m  \033[0m\033[103m  \033[0m")
                                print("\n\n"+"  "*j+"......")
                                sleep(0.1)
                                qing()
                            qing()
                        sleep(2)
                        qing()
                        name=input("请输入您的姓名:")
                        while name=="Administrator" or name=="guest" or name=="SYSTEM":
                            qing()
                            name=input("用户已存在，请重新输入:")
                        password=input("请输入您的密码:")
                        qing()
                        password_yz=None
                        password_yz=input("请再次输入您的密码:")
                        while password_yz!=password:
                            password_yz=input("\033[91m密码错误，请输入您的密码:")
                        print("\033[94mo 欢迎"+name)
                        break
                    elif prog=="B":
                        b("\033[90mPan版本")
                        b("\033[0mPan TSE 2.1")
                        b("©2020 HOTM workshop。保留所有权利。")
                        b("\n\n\033[90m系统")
                        b("\033[0m处理器:HOTM,X86720P-Virtual Emulator")
                        b("已安装的RAM:536MB(512.1MB可用)")
                        b("笔和触控:没有可用于此显示器的笔或触控输入")
                        b("\n\n\033[90m计算机名，域和工作组设置")
                        b("\033[0m计算机名:START-T8CF78L")
                        b("\033[0m描述:Pan TSE2.1 in Xueersi Coding.")
                        b("工作组:HOTM")
                    elif prog=="G":
                        if llqjh==0:
                            b("输入你的Pan密钥，它在Pan安装光盘里，或在开发者的留言中")
                            b("密钥示例:111-1111111")
                            key=input()
                            if len(key)!=11:
                                key="Error"
                            else:
                                for i in range(0,len(key)):
                                    if key[i]!="-" and i==3:
                                        key="Error"
                                        break
                                    elif key[i]!="-" and not(int(key[i])>=0 and int(key[i])<=9):
                                        key="Error"
                                        break
                            if key=="Error":
                                while key=="Error":
                                    qing()
                                    b("输入你的Pan密钥，它在Pan安装光盘里，或在开发者的留言中")
                                    b("密钥示例:111-1111111")
                                    key=input()
                                    for i in range(0,len(key)):
                                        if key[i]!="-" and i==3:
                                            key="Error"
                                            break
                                        elif not(int(key[i])>=0 and int(key[i])<=9):
                                            key="Error"
                                            break
                            qing()
                            print("密钥提交成功！")
                            print("管理员(180*****260)正在验证...")
                            if randint(0,10)==8:
                                print("管理员验证失败！正在通过Pan官方团队(189*****119)验证...")
                            sleep(5)
                            llqjh=1
                            print("密钥有效，验证通过！")
                        b("Pan已激活(密钥"+str(key[0])+str(key[1])+"*-******"+str(key[10])+")，回车键退出。")
                        input()
                    if llqjh==1:
                        if prog=="C":
                            b("默认方案:Pan默认(无声)")
                            b("A.默认响声")
                            if classic==0:
                                b("B.Steve")
                            prog=input()
                            if prog=="A":
                                play_mp3("lulu.mp3")
                            elif prog=="B":
                                speak("系统默认生音范例，当前讲述人:史蒂夫。讲述人系统测试:你好、谢谢、请走好。测试完毕！")
                        elif prog=="D":
                            b("当前分辨率:874×560")
                            b("\033[90m选择分辨率(不可用):\nA.1366×768\nB.1024×768\nC.874×560(推荐)\nD.800×600\nE.640×480")
                        elif prog=="E":
                            b(ctime())
                            b("UTC+8:00 China(default)")
                            b("\033[90m选择时区(不可用):\nA.UTC-4:00 US\nB.UTC UK\nC.UTC+8:00 China")
                        elif prog=="F":
                            if classic==1:
                                b("当前主题:Pan经典")
                            else:
                                b("当前主题:Pan TSE Basic")
                            b("更改主题:A.Pan经典 B.Pan TSE Basic C.Pan TSE 繁体中文版 D.主题属性")
                            prog=input()
                            qing()
                            print("\033[0m\033[7m        Pan启动管理器            \033[0m")
                            if prog=="A":
                                b("Pan经典")
                                b("背景:PanNT4.0")
                                b("颜色:黄色")
                                b("声音:无声")
                                b("鼠标光标:不支持")
                                prog=input("是否更改为此主题(Y|N)")
                                if prog=="Y":
                                    qing()
                                    print("\033[0m\033[7m        Pan启动管理器            \033[0m")
                                    print("\033[90m请稍等...")
                                    sleep(5)
                                    classic=1
                                    setmode("boy")
                                    print("\033[93m更改成功!")
                                else:
                                    qing()
                                    print("\033[0m\033[7m        Pan启动管理器            \033[0m")
                                    b("好的，您取消了更改")
                            elif prog=="B":
                                b("Pan TSE Basic")
                                b("背景:纯色")
                                b("颜色:蓝色")
                                b("声音:讲述人Steve的语音包(默认关闭)")
                                b("鼠标光标:为支持5点触控及以上的触摸显示屏提供支持")
                                prog=input("是否更改为此主题(Y|N)")
                                if prog=="Y":
                                    qing()
                                    print("\033[0m\033[7m        Pan启动管理器            \033[0m")
                                    print("\033[90m请稍等...")
                                    sleep(5)
                                    classic=0
                                    print("\033[93m更改成功!")
                                else:
                                    qing()
                                    print("\033[0m\033[7m        Pan启动管理器            \033[0m")
                                    b("好的，您取消了更改")
                            elif prog=="C":
                                b("Pan TSE 繁体中文版")
                                b("背景:Harmony")
                                b("颜色:黑色")
                                b("声音:无")
                                b("鼠标光标:不支持")
                                b("\033[90m由于你没有用户SYSTEM的许可，你不能使用这个主题")
                            elif prog=="D":
                                if classic==1:
                                    b("Pan经典")
                                    b("背景:PanNT4.0")
                                    b("颜色:黄色")
                                    b("声音:无声")
                                    b("鼠标光标:不支持")
                                else:
                                    b("Pan TSE Basic")
                                    b("背景:纯色")
                                    b("颜色:蓝色")
                                    b("声音:讲述人Steve的语音包(默认关闭)")
                                    b("鼠标光标:为支持5点触控及以上的触摸显示屏提供支持")
                                input("Enter键返回")
                            else:
                                b("该主题不存在，请联机搜索更多主题。")
                    elif prog=="X":
                        break
                    else:
                        qing()
                        continue
                    sleep(3)
                    qing()
                    continue
            if obj==1:
                break
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
        print("\n10秒后返回开始菜单\033[000m")
        sleep(10)
        qing()
        continue
    if obj==1:
        kfz()

except Exception as e:
    qing()
    error(str(e))