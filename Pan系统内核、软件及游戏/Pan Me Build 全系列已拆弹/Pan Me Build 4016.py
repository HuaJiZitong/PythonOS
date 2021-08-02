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
obj=0
classic=0
jsb=["使用Pan Me的记事本记录代办选项"]
ID=randint(10000,99999999)
def error(err):
    print("\033[44m")
    qing()
    print("A problem has been detected and pan has been shut down to\nprevent damage to your computer.")
    print("\nThe problem seems to be caused by the following file: Start.exe\n")
    print("Technical information:\n")
    print("*** STOP: "+err)
    print("\nPress \"运行\" to continue...")

def qing():
    system("clear")

def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    print()

def kfz():
    print("\033[?25l")
    qing()
    for i in range(3):
        print("_")
        sleep(0.5)
        qing()
        sleep(0.5)
    sleep(1)
    print("\n\033[30m\033[2m©HOTM Workshop\033[0m")
    sleep(0.2)
    qing()
    print("\n\033[30m©HOTM Workshop")
    sleep(0.2)
    qing()
    print("\n\033[90m©HOTM Workshop")
    sleep(0.2)
    qing()
    print("\n\033[0m©HOTM Workshop")
    sleep(uniform(0.3,3.1))
    qing()
    wfp=1.5
    e=2.0
    while 1:
        jsb={}               #记事本
        jsbr={}              #记事本回收站
        jsbrc={}             #记事本内容找回
        global llqjh
        global password
        qing()
        print("\033[0m开始                        SYSTEM")
        print("\033[95m1.命令提示符    \033[93m2.计算机      \033[92m3.记事本     \033[90m4.关机     \033[91m5.重装系统助手")
        print("\033[93mD.管理磁盘  \033[91mK.Pan激活工具(谨慎使用) \033[94mP.系统密码破解")
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
                qing()
                sleep(1)
                print("\033[92m现在你可以安全地关闭你的电脑了\033[8m")
                break
        elif kfz=="K":
            b("您当前使用的系统:Pan PE")
            b("您要激活的系统:Pan TSE 2.1(或Pan Me Beta版)")
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
            print("\033[0mUltimate(C:)\n2.68GB可用/4.00GB")
            print("\033[0mHomeSTD(D:)\n768MB可用/2.00GB")
            print("\033[0mStarter(E:)\n1.25GB可用/2.00GB")
            print("\033[0m备份Ghost(X:)\n"+str(e-0.1)+"GB可用/"+str(e)+"GB")
            print("\033[90mCD-ROM驱动器(F:)\n不可用\033[0m")
            System32=input("输入文件名，(如C:):")
            qing()
            if System32=="C:":
                print("名称    类型           修改日期               大小")
                print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1KB")
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
            elif System32=="D:":
                    print("名称    类型            修改日期               大小")
                    print("Boot    系统安装包(.wim)2021年2月19日 18:01    225MB")
                    print("Start   快捷方式(.lnk)  2020年6月14日 13:23    1KB")
                    print("Program 文件夹          2021年1月27日 17:10    119.9MB")
                    print("local   文件夹          2020年6月14日 13:25    887MB")
                    print(name+"   文件夹          2020年12月7日 17:54    100MB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="local":
                        print("名称    类型            修改日期               大小")
                        print("Start   软件(.exe)      2020年6月14日 13:23    640MB")
                        print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                        print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                        print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                    elif System32=="Program":
                        print("名称    类型           修改日期               大小")
                        print("program 软件(.exe)     2020年7月19日 13:23    117MB")
                        print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                        print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
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
            elif System32=="E:":
                if 1:
                    print("Name    Type            Modify date            Size")
                    print("Boot    .wim            2021-2-19 18:01        128MB")
                    print("Start   .lnk            2020-6-14 13:23        1KB")
                    print("Program Folder          2021-1-27 17:10        2.9MB")
                    print("local   Folder          2020-6-14 13:25        304MB")
                    print(name+"   Folder          2020-12-7 17:54        100MB")
                    System32=input("Enter filename(sample:\"C:\"):")
                    qing()
                    if System32=="local":
                        print("Name    Type            Modify date            Size")
                        print("Start   .exe            2020-6-14 13:23        256MB")
                        print("program .exe            2020-6-14 13:27        47MB")
                        print("System  .ini            2020-6-14 13:30        1MB")
                        print("Startup .exe            2020-6-14 13:31        56KB")
                    elif System32=="Program":
                        print("Name    Type           Modify date            Size")
                        print(".drives .dll           2021-1-27 17:10        2.9MB")
                        print(".drives .drv           2021-1-27 17:14        1KB")
                        print("Notes   .dat           2020-6-30 23:31        1KB")
                        System32=input("Enter filename(sample:\"C:\"):")
                        qing()
                        if System32==".drives":
                            b("Этот сервис содержит:Приложение стартового обслуживания для третьей стороны(Отключена)")
                        elif System32=="Taiwan":
                            sleep(0.2)
                            print("This program cannot run in x64 mode.")
                        else:
                            print("Bad command or file name.")
                    elif System32==name:
                        print("Name    Type            Modify date            Size")
                        print("user    .dll            2020-12-7 17:56        1KB")
                        print("data    .gho            2020-12-7 17:57        1KB")
                    else:
                        print("Bad command or file name.")
            elif System32=="X:":
                print("名称    类型             修改日期               大小")
                print("Ghost   扩展驱动(.dll)   2020年7月18日  19:38    53MB")
                print("PanMe3e 系统安装包(.wim) 2020年10月1日  18:59    46.6MB")
                print("readme  文本(.txt)       2020年10月1日  19:02    407.6KB")
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
            elif System32=="F:":
                print("该磁盘里没有可用的安装文件(setup.exe或者oemsetup.inf)，也没有可查看的文件。")
            else:
                print("该文件不存在")
        elif kfz=="P":
            b("欢迎来到密码破解系统！\nA.重置密码为空 B.更改密码")
            disk=input()
            if disk=="A":
                password=None
                b("重置成功，注销账号后生效")
            elif disk=="B":
                password=input("输入新密码:")
                b("更改成功，注销账号后生效")
            else:
                b("None")
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
            qing()
            sleep(1)
            print("\033[92m现在你可以安全地关闭你的电脑了\033[0m")
            qing()
            break
        elif kfz=="5":
            sst=input("这是你的安装密钥:\n357-2856739\n\n记住你的密钥，然后按下Enter键，安装Starter版本按1")
            if sst=="1":
                ss()
            else:
                setup()
        elif kfz=="D":
            print("\033[0mVirtualDisk(11.6GB)")
            print("\033[90mUltimate(C: 4.00GB) HomeSTD(D: 2.00GB) Starter(E: 2.00GB)\033[94m备份GHOST(X: "+str(e)+"GB) 未分配("+str(wfp)+"GB)  \033[90mEFI恢复分区(0.1GB)")
            print("\033[0m光盘(0Byte)")
            print("\033[90mCD-ROM驱动器(F: 0Byte)")
            disk=input("\033[0m选择要更改的分区(填写盘符，没有盘符填名称，如E:)")
            qing()
            if disk=="C:" or disk=="D:" or disk=="F:":
                print("该分区已被组织HOTM锁定，不可更改")
                sleep(3)
                disk=input("是否继续更改?(Y|N)")
                if disk=="Y":
                    qing()
                    error("operating system not found")
                    break
                else:
                    print("好的，即将返回桌面")
            elif disk=="E:":
                print("B.属性")
                disk=input()
                qing()
                if disk=="B":
                    print("Starter (E:)")
                    print("可用空间:1.25GB")
                    print("总空间:2.00GB")
                else:
                    print("该操作无效。")
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
            elif disk=="X:":
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

def ss():
    global name
    global llqjh
    global key
    print("Setup will install Pan Me in your computer\nIt can help you to setting your disk:")
    print("    - Start Pan Me\n    - Open Pan application")
    b("When you are ready,press Enter to continue")
    input()
    qing()
    input("Do you want to install a mouse driver?\nif you don't know,please press Enter again.")
    qing()
    input("Do you want to install a display driver?\nif you don't know,please press Enter again.")
    qing()
    print("Setup is restarting your computer...")
    stu=randint(1,10)
    sleep(2)
    qing()
    print("\033[?25hVirtualDisk(11.6GB)...No Media.")
    sleep(1)
    print("CDROM-Driver(46.6MB)...Found at Pan TSE 2.1")
    qing()
    name="Owner"
    llqjh=1
    key="233-9887346"
    print("Copying System files(0% completed)")
    sleep(randint(3,7))
    qing()
    print("Copying System files(69% completed)")
    sleep(randint(1,4))
    qing()
    print("Copying System files(100% completed)")
    qing()
    b("Pan was already installed in your computer,Xueersi Tools manual installation is required.")
def setup():
    global llqjh
    global key
    global ds_2
    global ds_3
    global ds_4
    global ds_5
    global name
    global password
    print("\033[0m")
    qing()
    quick=input("需要进行快速安装吗?\n需要敲\"y\"，不需要请敲\"n\"")
    if quick=="y" or quick=="Y":
        name=input("输入你的姓名:")
        while name=="Administrator" or name=="guest" or name=="SYSTEM" or name==" "*len(name):
            qing()
            name=input("\033[91m你可以使用你喜欢的任何名称，前提是不使用Administrator、SYSTEM、guest和空名称:\033[0m")
        qing()
        password=None
        llqjh=1
        key="229-3838577"
        ds_2=0
        ds_3=0
        ds_4=0
        ds_5=0
        qing()
        print("正在复制系统文件(完成0%)\n\n这可能需要一点时间，请坐和放宽。")
        sleep(randint(3,7))
        qing()
        print("正在复制系统文件(完成69%)\n\n这可能需要一点时间，请坐和放宽。")
        sleep(randint(1,4))
        qing()
        print("正在复制系统文件(完成100%)\n\n这可能需要一点时间，请坐和放宽。")
        qing()
    elif quick=="n" or quick=="N":
        print("安装程序将会把Pan Me安装到你的电脑上\n它还可以帮助您以最有效的方式设置磁盘:")
        print("    - 启动Pan Me\n    - 打开Pan应用程序\n    - 使用Pan驱动打印机")
        b("当你准备好，请继续按Enter")
        input()
        qing()
        input("要安装鼠标驱动程序吗?\n如果你不知道，请继续按Enter")
        qing()
        input("要安装显示器驱动程序吗?\n如果你不知道，请继续按Enter")
        qing()
        input("要安装打印机驱动程序吗?\n如果你不知道，请继续按Enter")
        qing()
        print("安装程序正在重启电脑...")
        stu=randint(1,10)
        sleep(2)
        qing()
        sleep(2)
        print("\033[?25h",end="")
        while 1:
            print("Pan Boot Manager")
            print("==================")
            print("Choise operating system:\n[1]Install Pan Me(Enter)\n[2]Pan PE\n[3]Shutdown the system\nEnter your choise:")
            panme=input()
            qing()
            if panme=="1" or panme==" "*len(panme):
                print("Copyright © 2019-2021 HOTM studio.")
                print("Loading F:\\Linux\\Ubuntu\\CD1\\Boot.wim")
                sleep(2)
                print("Loading F:\\Linux\\Ubuntu\\CD1\\setup.exe")
                sleep(1)
                print("Type 3 \"128Mb CD ROM\" is fixed disk 1")
                print("BusX86: 64Mb ROM at 0xf7003")
                sleep(1)
                print("Starting Pan...found at C:\\cmd.exe")
                qing()
                break
            elif panme=="2":
                print("Pan Boot Manager")
                print("==================")
                print("Pan cannot startup")
                print("Because Disk \"VirtualDisk\" hadn't been ready.")
            elif panme=="3":
                print("Bad command or file name.")
    
        print("\033[?25l",end="")
        if 1:
            if 1:
                qing()
                print("正在复制系统文件(完成1%)")
                input("请插入以下光盘:\nPan Me安装光盘_CD2\n输入光盘路径，不输入默认为这个路径:F:\\Linux\\Ubuntu\\CD2")
                qing()
                name=input("输入你的姓名:")
                while name=="Administrator" or name=="guest" or name=="SYSTEM" or name==" "*len(name):
                    qing()
                    name=input("\033[91m你可以使用你喜欢的任何名称，前提是不使用Administrator、SYSTEM、guest和空名称:\033[0m")
                qing()
                key=input("请输入你的产品密钥，它在Pan安装光盘里，如果没有，请向管理员索要\n产品密钥像这样:357-2856739\n")
                if len(key)!=11:
                    key="Error"
                else:
                    for i in range(0,len(key)):
                        if key[i]!="-" and i==3:
                            key="Error"
                            break
                        elif key[i]!="-" and not(int(key[i])>=0 and int(key[i])<=9) and i!=3:
                            key="Error"
                            break
                if 1:
                    while key=="Error":
                        qing()
                        key=input("请输入你的产品密钥，它在Pan安装光盘里，如果没有，请向管理员索要\n产品密钥像这样:357-2856739\n")
                        for i in range(0,len(key)):
                            if key[i]!="-" and i==3:
                                key="Error"
                                break
                            elif not(int(key[i])>=0 and int(key[i])<=9) and i!=3:
                                key="Error"
                                break
                password=input("输入你的密码:")
                qing()
                input("请插入以下光盘:\nPan Me安装光盘_CD1\n输入光盘路径，不输入默认为这个路径:F:\\Linux\\Ubuntu\\CD1")
                qing()
                for i in range(0,100,stu):
                    qing()
                    print("正在复制系统文件(完成"+str(i)+"%)\n\n这可能需要一点时间，请坐和放宽。")
                    sleep(stu/10)
                qing()
            b("恭喜！恭喜！Pan Me已成功地安装到你的电脑上，请按Enter键继续。")
            if 1:
                ds_2=0
                ds_3=0
                ds_4=0
                ds_5=0
                password=None
                llqjh=0
            input()
            qing()
            b("Xueersi Tools具有很多功能，能改善鼠标移动性，显示和性能，按下y键开始安装")
            xtools=input()
            qing()
            if xtools=="y" or xtools=="Y":
                print("Xueersi Tools 2.4\nCopyright © 2009-2021 Xueersi Corporation.\nPreparing to install...")
                print("Loading vcredit64.msi.......")
                sleep(2)
                print("Loading Xueersi Tools64.msi....")
                sleep(1)
                print("\033[44m")
                qing()
                print("\n \033[40m \033[44m")
                print("\n\n\n                 \033[107m \033[104;30m            Xueersi Tools            \033[101m x \033[107m \033[44m")
                print("                 \033[107;30mPan正在安装设备驱动程序,请稍后...         \033[40m \033[44m")
                print("                 \033[107;30m(*)浏览器 (*)应用商店 (*)实用插件包       \033[40m \033[44m")
                print("                      \033[40m"+38*" "+"\033[44m")
                sleep(randint(3,17))
                qing()
                b("安装完毕，接下来你可以放心使用Pan Me了")
            else:
                b("您取消了安装，接下来需要手动安装以解锁更多功能。")
llqjh=0
ds_3=0
#---------------------------------定义---------------------------------
try:
    while 1:
        print("\033[?25hPan Boot Manager")
        print("==================")
        print("Choise operating system:\n[1]Pan Me Ultimate\n[2]Pan Me Home\n[3]Pan Me Starter\n[4]Pan PE\n[5]Shutdown the system\nEnter your choise:")
        panme=input()
        system("clear")
        try:
            if int(panme)==4:
                kfz()
            elif int(panme)<=3:
                break
            elif int(panme)==5:
                print("\033[92m现在你可以安全地关闭你的电脑了\033[8m")
                break
        except:
            continue
    print("\033[?25l",end="")
    if panme=="3":
        jsb=["Use Pan ME notepad to checking to-do options","\"Jet Rebase\" is missing,you cannot check the recycle bin"]
        print("Copyright © 2019-2021 HOTM studio.")
        print("Loading C:\\local\\Startup.exe.......")
        sleep(2)
        print("Loading C:\\Program\\program.exe....")
        sleep(1)
        print("Type 3 \"2Gb Hard Disk\" is fixed disk 1")
        print("BusX86: 256Mb ROM at 0xf7003")
        sleep(1)
        print("Starting Pan...found at C:\\Boot.wim")
        sleep(3)
        qing()
        classic=1
        name="Owner"
        llqjh=1
        key="233-9887346"
        while 1:
            print("\033[90mPan Preview version\nAssessment copy.Overdue time 2021/5/20.\033[0m")
            print("\033[103m")
            qing()
            print("It's ",ctime())
            print("\033[90m0.Shutdown\n\033[91m1.Calculator")
            print("\033[31m2.Notepad\n\033[92m3.Restart")
            print("\033[32m4.System property")
            print("\033[34m5.Computer\n\033[35m6.Pan introduction\n\033[96m7.Get more Apps")
            print("\033[94m8.Reinstall system")
            prog=input("\033[0;103mEnter program's number:")
            print("\033[0m")
            qing()
            print("\033[90mPan Preview version\nAssessment copy.Overdue time 2021/5/20.\033[0m")
            if prog=="0":
                for i in range(5):
                    print("\033[0mo Shutting down...")
                    sleep(0.2)
                    system("clear")
                    print("\033[94mo Shutting down...")
                    sleep(0.2)
                    system("clear")
                sleep(1)
                qing()
                print("\033[92mIt's now safe to turn off your computer.\033[8m")
                break
            elif prog=="1":
                qing()
                print("\033[35m+===============Pan Calculator===============+")
                print("\033[31m| Calculator")
                print("\033[36m1=Normal      ")
                print("\033[33m2=Combined formula    ")
                print("\033[35m3=Average      \033[36m4=Leap year")
                print("\033[32m5=Date interval")
                print("\033[31m| Conversion")
                print("\033[36m7=Currency")
                ji_xuan = input("\033[33mEnter mode's number:")
                if ji_xuan == "1":
                    while 1:
                        try:
                            qing()
                            print("\033[32m    - Normal Calculator -")
                            kaishi1 = input("\033[33mPress Enter to begin(a char to exit)：")
                            if kaishi1 == "":
                                qing()
                                number1 = input("\033[33mEnter first number: ")
                                number2 = input("\033[32mEnter second number: ")
                                leixin = input("\033[34mEnter operative symbol:(\033[31m1.Plus \033[32m2.Subtraction \033[33m3.Multiplication \033[36m4.Division): ")
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
                                print("\033[31mCalculating...\033[33m")
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
                                    print("\033[36m - Vertical for reference only - ")
                                    print()
                                elif fu == "+":
                                    print(" "+ number1)
                                    print(fu + number2)
                                    print("-------------------------")
                                    number1 = int(number1)
                                    number2 = int(number2)
                                    print("",number1+number2)
                                    print("\033[36m - Vertical for reference only - ")
                                    print()
                                elif fu == "-":
                                    print(" "+ number1)
                                    print(fu + number2)
                                    print("-------------------------")
                                    number1 = int(number1)
                                    number2 = int(number2)
                                    print("",number1 - number2)
                                    print("\033[36m - Vertical for reference only - ")
                                    print()
                                elif fu == "*" and len(number1) <= 2 and len(number2) <= 2:
                                    print(" "+ number1)
                                    print(fu + number2)
                                    print("-------------------------")
                                    number1 = int(number1)
                                    number2 = int(number2)
                                    print("",number1 * number2)
                                    print("\033[36m - Vertical for reference only - ")
                                    print()
                                elif fu == "*" and len(number1) > 2 and len(number2) > 2:
                                    qing()
                                    print()
                                    print()
                                    print("\033[33m○ Loading vertical\033[31m")
                                    print()
                                    print()
                                    sleep(2)
                                    qing()
                                    print("     ?    ")
                                    print("Failed to load")
                                    print()
                                    print("\033[36m - Vertical for reference only - ")
                                    print()
                                elif fu == "/":
                                    print("\033[31mDoesn't support division vertical~")
                                    #类型判断并运算
                                    number1 = int(number1)
                                    number2 = int(number2)
                                    if leixin == "1":
                                        print("\033[34m"+str(number1)+"+"+str(number2)+"=",number1 + number2)
                                    elif leixin == "2":
                                        print("\033[34m"+str(number1)+"-"+str(number2)+"=",number1 - number2)
                                    elif leixin == "3":
                                        print("\033[34m"+str(number1)+"x"+str(number2)+"=",number1 * number2)
                                    elif leixin == "4":
                                        leixinofchu = input("\033[33mEnter division type：(1.decimal division 2.remainder):")
                                        if leixinofchu == "1":#小数计算
                                            print("\033[34m"+str(number1)+"÷"+str(number2)+"=",number1 / number2)
                                        elif leixinofchu == "2":#余数计算
                                            answer_of_chu = str(number1 // number2)+"······"+str(number1 % number2)
                                            print("\033[34m"+str(number1)+"÷"+str(number2)+"=",answer_of_chu)
                                        else:
                                            print("\033[31mInvalid option~")
                                else:
                                    qing()
                                    print("\033[31mInvalid option~")
                                input("\033[33mPress Enter to complete：")
                                qing()
                            else:
                                qing()
                                print("\033[31mExiting...")
                                sleep(1)
                                break
                        except ZeroDivisionError:
                            print("Divisor cannot be 0")
                        except ValueError:
                            print("Operation Error") 
                elif ji_xuan == "2":
                    qing()
                    shss_1 = input("\033[33mEnter formula(sample:1*5+6/2-1):")
                    try:
                        print("\033[32mThis formula is equal:")
                        print(shss_1,"=",eval(shss_1))
                        print("\033[36mRecursion equation:Coming soon")
                    except:
                        print("\033[31mError")
                elif ji_xuan == "3":
                    qing()
                    pl = []
                    qpjsgs = int(input("\033[33mEnter the number of sum:\033[32m"))
                    for i in range(qpjsgs):
                        str1 = 'Sum '+str(i+1)+' is:'
                        p = int(input(str1))
                        pl.append(p)
                        qing()
                    qing()
                    psum = sum(pl)
                    pa = psum/qpjsgs
                    print("\033[34mThe average number is ",pa)
                elif ji_xuan == "5":
                    qing()
                    a = int(input('\033[33mWhat year is this:'))
                    qing()
                    if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
                        print('\033[32mThe year is:Leap year')
                    else:
                        print('\033[34mThe year is:Common year')
                elif ji_xuan == "6":
                    qing()
                    print("\033[36msample:2020-01-01")
                    date1 = input("\033[32mEnter 1st date:")
                    date2 = input("\033[34mEnter 2nd date:")
                    try:
                        days = date_diff(date1,date2)
                        print("\033[93mThe answer is:"+str(days)+" days\033[0m")
                    except:
                        print("\033[91mFormat error or System error,Operation is failed\033[0m")
                elif ji_xuan == "7":#货币
                    qing()
                    print("\033[33m1=RMB>Euro")
                    print("\033[32m2=RMB>Yen")
                    print("\033[34m3=RMB>Dollar")
                    print("\033[35m4=RMB>Won")
                    mode = input("\033[31m>>>")
                    qing()
                    if mode == "1":
                        q = int(input("\033[36mEnter the sumo of RMB:"))
                        a = q * 0.1318
                        print("\033[32m"+str(q)+"RMB="+str(a)+"Euros")
                    elif mode == "2":
                        q = int(input("\033[36mEnter the sumo of RMB:"))
                        a = q * 15.6430
                        print("\033[32m"+str(q)+"RMB="+str(a)+"Yens")
                    elif mode == "3":
                        q = int(input("\033[36mEnter the sumo of RMB:"))
                        a = q * 0.1410
                        print("\033[32m"+str(q)+"RMB="+str(a)+"Dollars")
                    elif mode == "4":
                        q = int(input("\033[36mEnter the sumo of RMB:"))
                        a = q * 176.8076
                        print("\033[32m"+str(q)+"RMB="+str(a)+"Won")
                    else:
                        print("\033[31mDoesn't have this unit")
                input("\033[33mpress Enter to return")
            elif prog=="2":
                while 1:
                    qing()
                    print("\033[?25h\033[32mWelcome to notepad!\033[34mEnter notepad's name to open,\033[33mEnter new name to create,\033[31mEnter exit to exit")
                    print("\033[33mThis computer have these notepads:\033[0m")
                    for i in jsb:
                        print(i)
                    j=input("\033[36mEnter notepad's name:")
                    qing()
                    if j.lower()=='exit':
                        print("\033[?25l")
                        break
                    elif j.lower()=='recycle':
                        print("\033[36m| Recycle bin\033[32m")
                        b("Jet Rebase is missing\ncopy a new module,and then restart the computer")
                    elif j in jsb:
                        print(jsb[j])
                        print("\033[33m1.modify \033[31m2.delete \033[34m3.rename \033[31mtype other to exit")
                        c=input("\033[0mPlease choise:")
                        if c=='1':
                            qing()
                            nr = ''
                            print("\033[32mEnter notepad's content,Enter esc to finish,Enter clear to clear all content.\033[33m")
                            while 1:
                                a = input()
                                if a == 'esc':
                                    break
                                elif a == 'clear':
                                    nr = ''
                                    qing()
                                    print("\033[32mModify notepad's content,Enter esc to finish,Enter clear to clear all content.\033[33m")
                                    continue
                                elif '<fontcolor='in a:
                                    if len(a) < 12:
                                        print("\033[31m<fontcolor=  value error:is no color input(The parameter must be in Chinese characters)\033[33m")
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
                                print("\033[32mSuccessfully to modify!")
                        elif c=='2':
                            del jsb[j]
                            print("\033[32mSuccessfully to delete!")
                        elif c=='3':
                            new=input("\033[36mEnter new name:")
                            if new=='exit':
                                print("\033[31mThis name had been used!")
                                sleep(2)
                                continue
                                jsb[new] = jsb[j]
                                del jsb[j]
                                print("\033[32mSuccessfully to modify!")
                        else:
                            continue
                        sleep(2)
                    else:
                        nr = ''
                        print("\033[32mEnter notepad's content,Enter esc to finish,Enter clear to clear all content.\033[33m")
                        while True:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                qing()
                                print("\033[32mEnter notepad's content,Enter esc to finish,Enter clear to clear all content.\033[33m")
                                continue
                            elif '<fontcolor='in a:
                                if len(a) < 12:
                                    print("\033[31m<fontcolor=  value error:is no color input(The parameter must be in Chinese characters)\033[33m")
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
                            print("Successfully to create!")
                            sleep(2)
                    print("\033[?25l")
            elif prog=="3":
                for i in range(5):
                    print("\033[0mo Restarting Pan")
                    sleep(0.2)
                    system("clear")
                    print("\033[94mo Restarting Pan")
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
            elif prog=="4":
                print("\033[101m  \033[0m\033[102m  \033[0m")
                print("\033[104m  \033[0m\033[103m  \033[0mPan\033[92mMultiple Edition")
                print("\033[0mHOTM Pan")
                print("Version 5.11(Build 4016)")
                print("Copyright ©2021 HOTM Workshop.All Rights Reserved.")
                print("PanMe Starter Edition operating system and UI is protected by trademark laws and other pending or promulgated intellectual property laws of PRC and other countries/regions")
                input("if you had already seen it,press Enter")
            elif prog=="5":
                print("\033[0mStarter(C:)\n1.25GB free for 2.00GB")
                System32=input("Enter filename(sample:\"C:\"):")
                qing()
                if System32=="C:":
                    print("Name    Type            Modify date            Size")
                    print("Boot    .wim            2021-2-19 18:01        128MB")
                    print("Start   .lnk            2020-6-14 13:23        1KB")
                    print("Program Folder          2021-1-27 17:10        2.9MB")
                    print("local   Folder          2020-6-14 13:25        304MB")
                    print(name+"   Folder          2020-12-7 17:54        100MB")
                    System32=input("Enter filename(sample:\"C:\"):")
                    qing()
                    if System32=="local":
                        print("Name    Type            Modify date            Size")
                        print("Start   .exe            2020-6-14 13:23        256MB")
                        print("program .exe            2020-6-14 13:27        47MB")
                        print("System  .ini            2020-6-14 13:30        1MB")
                        print("Startup .exe            2020-6-14 13:31        56KB")
                    elif System32=="Program":
                        print("Name    Type           Modify date            Size")
                        print(".drives .dll           2021-1-27 17:10        2.9MB")
                        print(".drives .drv           2021-1-27 17:14        1KB")
                        print("Notes   .dat           2020-6-30 23:31        1KB")
                        System32=input("Enter filename(sample:\"C:\"):")
                        qing()
                        if System32==".drives":
                            b("Этот сервис содержит:Приложение стартового обслуживания для третьей стороны(Отключена)")
                        else:
                            print("Bad command or file name.")
                    elif System32==name:
                        print("Name    Type            Modify date            Size")
                        print("user    .dll            2020-12-7 17:56        1KB")
                        print("data    .gho            2020-12-7 17:57        1KB")
                    else:
                        print("Bad command or file name.")
                else:
                    print("Bad command or file name.")
            elif prog=="6":
                print("\033[0m1.English introduction 2.系统特点(中文)")
                rm=input()
                qing()
                if rm=="2":
                    b("PanMe入门版是一款被大幅度精简了无用内容的特色虚拟系统，精简过后的PanMe入门版的体积被大幅度的消减但是运行的流畅度却没有因为精简而有丝毫的影响。")
                    b('''PanME入门版特色：
1、开机速度相比Pan其他的操作系统提升了47%，更加可靠。
2、Pan NT 5.x内核的操作系统改进了计算准确率和用户管理。
3、用户体验将更加高级，自动整合应用使用率来精简应用。
4、PanMe大幅缩减了Pan的启动速度，系统加载时间一般不超过15秒。
5、PanMe将会让使用信息更加简单，包括本地和Internet功能。
6、在数据保护和协作之间搭建桥梁,同时也会开启工作室级的数据保护和权限许可。''')
                    b('''PanMe入门版亮点：
1、开始菜单加入新选项和新功能。
2、记事本输入法上下文词语联想提升。
3、引入复古经典UI，标准键盘已经支持英语、俄语、简中、繁中四种常用语言。
4、设置改进和提升、声音设置挪到了启动管理器中
5、系统功能全自动静音
6、英文和俄文字体引入，输入更流畅，词语显示更准确，空格距离联想更精确。(仅限Windows用户)
7、浏览器、资源管理器等都加入了这一功能，只要设备支持上网即可，就可以在Internet共享文件。
''')
                    b("PanMe入门版说明：\nPanMe入门版系统可以为用户带来更加流畅的使用并且各种系统的运行也绝不会因为精简而出现各种问题。")
                    b("1.以Pan TSE 2.0为母盘精简化\n2.不加载多余dll\n3.禁用第三方应用和应用商店\n4.关闭自动更新\n5.优化磁盘格式系统\n6.仅保留管理员，享受最高权限(无密码)\n7.日常使用基本无蓝屏\n8.系统经过优化，命令提示符启动更能提高查错(debug)效率")
                elif rm=="1":
                    b('''PanME Starter is a feature installed system that has been stripped of unnecessary content. The stripped down Panme Starter has been stripped down in size but has not lost any of its smoothness. )
Panme Starter Edition Features:
1. Boot-up speed is 47% faster than other PAN operating systems, making it more reliable.
2. Pan NT 5.x kernel operating system improves computational accuracy and user management.
3. The user experience will be more advanced, automatically integrating application usage to streamline applications.
4. Panme greatly reduces the startup speed of the PAN, and the system load time is generally less than 15 seconds.
5. Panme will make it easier to use information, including local and Internet capabilities.
6. Bridging the gap between data protection and collaboration, as well as opening up data protection and licensing at the studio level. "')
Panme Starter Highlights:
1. Add new options and functions to Start Menu.
2, Notepad input method context word association improvement.
3, the introduction of retro classic UI, the standard keyboard has supported English, Russian, simple Chinese, traditional Chinese four common languages.
4. Settings improvements and enhancements, sound Settings moved to the boot manager
5. Automatic mute of system function
6, the introduction of English and Russian fonts, more smooth input, words display more accurate, space distance association more accurate. (Windows users only)
7. Browsers, resource managers, and so on have added this function. As long as the device supports Internet access, you can share files on the Internet.
                    ''')
                    b("PanME Starter specification:1.Take Pan TSE 2.0 as the mother disk to streamline\n2.Don't load too much .dll file\n3.Disabled third party application and App store")
                    b("4.Disabled Pan update\n5.Optimize disk format system(NTFS)\n6.Reserve Administrator only,to have higher permissions(No password)")
                    b("7.There is no Blue Screen of death(BSOD) for daily use\n8.The system has been optimized, and the command prompt startup can improve the efficiency of debug")
            elif prog=="7":
                print("\033[42m")
                qing()
                print("📺    You are offline,App store cannot start.")
            elif prog=="8":
                ss()
            elif prog=="35768":
                while 1:
                    print("\033[0m\033[7m            Pan Boot Manager            ")
                    print("\033[0mPlease choise a option")
                    print("\nA.change system")
                    print("B.Settings")
                    print("to exit,please enter to Settings")
                    prog=input()
                    qing()
                    if prog=="A":
                        qing()
                        sleep(2)
                        print("\033[7m            Pan Boot Manager            ")
                        print("\033[0mPlease choise a option")
                        print("\nA.Pan Me Build 4016")
                        print("B.Pan PE")
                        prog=input()
                        if prog=="B":
                            obj=1
                            break
                        else:
                            qing()
                            break
                    elif prog=="B":
                        print("\033[7m        Pan Boot Manager            ")
                        print("\033[0mPlease choise a option")
                        print("\nA.Reset system")
                        print("B.System property\nC.Sound\nD.Display\nE.Time\nF.Themes\nG.Active Pan\nX.Exit")
                        prog=input()
                        qing()
                        print("\033[7m        Pan Boot Manager            ")
                        print("\033[0m",end="")
                        if prog=="A":
                            print("Resetting......")
                            key=None
                            ds_2=0
                            ds_3=0
                            ds_4=0
                            ds_5=0
                            sleep(2)
                            print("Successfully to reset,now begin to restart...")
                            sleep(3)
                            qing()
                            for i in range(3):
                                print("_")
                                sleep(0.2)
                                qing()
                                sleep(0.2)
                            sleep(3)
                            qing()
                            break
                        elif prog=="B":
                            b("\033[90mPan Version")
                            b("\033[0mPan Me Starter")
                            b("©2021 HOTM workshop.All rights reversed.")
                            b("\n\n\033[90mSystem")
                            b("\033[0mCPU:HOTM,X86720P-Virtual Emulator")
                            b("RAM:275MB(256.1MB free)")
                            b("Touch service:Disabled")
                            b("\n\n\033[90mComputer name,domain,and workgroup Settings")
                            b("\033[0mComputer name:START-T8CF78L")
                            b("\033[0mDescribe:Pan Me in Xueersi Coding.")
                            b("Workgroup:HOTM")
                        elif prog=="G":
                            b("Pan had been actived (key:"+str(key[0])+str(key[1])+"*-******"+str(key[10])+"),Press Enter to return.")
                            input()
                        if llqjh==1:
                            if prog=="C":
                                b("Plan:No sounds")
                                b("A.Ding")
                                prog=input()
                                if prog=="A":
                                    play_mp3("lulu.mp3")
                                else:
                                    b("Bad command or file name.")
                            elif prog=="D":
                                b("Screen.currentResolution:640×480")
                                b("\033[90mChoise a Resolution(Disabled):A.800×600\nB.640×480(recommended)")
                            elif prog=="E":
                                b(ctime())
                                b("UTC+4:00 US(default)")
                                b("\033[90mChoise a time(disabled):\nA.UTC-4:00 US\nB.UTC UK")
                            elif prog=="F":
                                b("Theme:Pan classic")
                                b("Modift theme:A.Pan Classic B.Theme property")
                                prog=input()
                                qing()
                                print("\033[0m\033[7m        Pan Boot Manager            \033[0m")
                                if prog=="A":
                                    b("Pan classic")
                                    b("Background:PanNT4.0")
                                    b("Color:Yellow")
                                    b("Sound:No sound")
                                    b("Mouse:Disabled")
                                    prog=input("Whether to change this theme(Y|N)")
                                    if prog=="Y":
                                        qing()
                                        print("\033[0m\033[7m        Pan Boot Manager            \033[0m")
                                        print("\033[90mPlease wait...")
                                        sleep(5)
                                        setmode("boy")
                                        print("\033[93mSuccessfully to modify!")
                                    else:
                                        qing()
                                        print("\033[0m\033[7m        Pan Boot Manager            \033[0m")
                                        b("You were cancel to modify just now.")
                                elif prog=="B":
                                    b("Pan classic")
                                    b("Background:PanNT4.0")
                                    b("Color:Yellow")
                                    b("Sound:No sound")
                                    b("Mouse:Disabled")
                                    input("Press Enter to return.")
                                else:
                                    b("This theme is not found.Please go to internet to search more themes.")
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
                print("Bad command or file name.")
                sleep(0.5)
                input("\033[32mPress Enter to return.")
                qing()
                continue
            print("\nReturn to the desktop after 10 seconds\033[000m")
            sleep(10)
            qing()
            continue
        if obj==1:
            kfz()
    if panme=="2":
        for i in range(3):
            print("_")
            sleep(0.2)
            qing()
            sleep(0.2)
        print("\033[107m")
        sleep(1)
        qing()
        print("                                 \033[90mHOTM©\n\n")
        print('''            \033[94m______    \033[91m ______
            \033[94m|     \   \033[91m|     |    \033[93m|\   |
            \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
            \033[94m|         \033[91m|     |    \033[93m|  \ |
            \033[94m|         \033[91m|     |    \033[93m|   \|
        ''')
        print("\033[90m  HOTM")
        print("\033[93m   Pan® Me Home STD Edition")
        print("\n\033[92m           Starting up...\n",end="")
        print("\033[42m"+40*" ")
        sleep(3)
        print("\033[0m")
        qing()
        sleep(2)
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
            print("\033[90mPan 公测版本\n评估副本。过期时间2021/5/20。\033[0m")
            if classic==0 or classic==2:
                if classic==2:
                    print("\033[101m")
                    qing()
                print("\033[0m开始                        "+name)
                print("\033[90m0.关机  \033[91m1.计算器")
                print("\033[31m2.记事本     \033[92m3.重启")
                print("\033[32m4.系统属性    \033[33m5.有道     \033[94m6.地图 ")
                print("\033[95m7.浏览器        \033[34m8.计算机      \033[35m9.Pan系统入门 \033[96m10.应用商店")
                prog=input("\033[0m请输入应用序号:")
            else:
                print("\033[103m")
                qing()
                print("现在是",strftime("%Y年%m月%d日 %H点%M分%S秒",localtime()))
                print("\033[90m0.关机\033[91m1.计算器")
                print("\033[31m2.记事本\n\033[92m3.重启")
                print("\033[32m4.系统属性\n\033[33m5.有道\n\033[94m6.地图 ")
                print("\033[95m7.浏览器\n\033[34m8.计算机\n\033[35m9.Pan系统入门\n\033[96m10.应用商店")
                prog=input("\033[0;103m请输入应用序号:")
    
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
            if classic==0:
                print("\033[0m"+strftime("%H:%M",localtime()))
            
            print("\033[0m")
            qing()
            print("\033[90mPan 公测版本\n评估副本。过期时间2021/5/20。\033[0m")
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
            elif prog=="2":
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
            elif prog=="3":
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
            elif prog=="4":
                print("\033[101m  \033[0m\033[102m  \033[0m")
                print("\033[104m  \033[0m\033[103m  \033[0mPan\033[92mMultiple Edition")
                print("\033[0mHOTM Pan")
                print("版本5.11(内部版本 Build 4016)")
                print("版权所有 ©2021 HOTM Workshop。保留所有权利。")
                print("PanMe 家庭标准版 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
                input("看完按Enter")
            elif prog=="5":
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
            elif prog=="6":
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
            elif prog=="7":
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
            elif prog=="8":
                print("\033[0mHome STD(C:)\n768MB可用/2.00GB")
                print("\033[0mStarter(D:)\n1.25GB可用/2.00GB")
                print("\033[0m💽 CD-ROM驱动器(F:)")
                if ds_3==1:
                    print("0Byte可用/6.55GB NTFS磁盘格式")
                else:
                    print("驱动器不可用 RAW磁盘格式")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="C:":
                    print("名称    类型            修改日期               大小")
                    print("Boot    系统安装包(.wim)2021年2月19日 18:01    225MB")
                    print("Start   快捷方式(.lnk)  2020年6月14日 13:23    1KB")
                    print("Program 文件夹          2021年1月27日 17:10    119.9MB")
                    print("local   文件夹          2020年6月14日 13:25    887MB")
                    print(name+"   文件夹          2020年12月7日 17:54    100MB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="local":
                        print("名称    类型            修改日期               大小")
                        print("Start   软件(.exe)      2020年6月14日 13:23    640MB")
                        print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                        print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                        print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                    elif System32=="Program":
                        print("名称    类型           修改日期               大小")
                        print("program 软件(.exe)     2020年7月19日 13:23    117MB")
                        print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                        print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
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
                elif System32=="D:":
                    print("Name    Type            Modify date            Size")
                    print("Boot    .wim            2021-2-19 18:01        128MB")
                    print("Start   .lnk            2020-6-14 13:23        1KB")
                    print("Program Folder          2021-1-27 17:10        2.9MB")
                    print("local   Folder          2020-6-14 13:25        304MB")
                    print(name+"   Folder          2020-12-7 17:54        100MB")
                    System32=input("Enter filename(sample:\"C:\"):")
                    qing()
                    if System32=="local":
                        print("Name    Type            Modify date            Size")
                        print("Start   .exe            2020-6-14 13:23        256MB")
                        print("program .exe            2020-6-14 13:27        47MB")
                        print("System  .ini            2020-6-14 13:30        1MB")
                        print("Startup .exe            2020-6-14 13:31        56KB")
                    elif System32=="Program":
                        print("Name    Type           Modify date            Size")
                        print(".drives .dll           2021-1-27 17:10        2.9MB")
                        print(".drives .drv           2021-1-27 17:14        1KB")
                        print("Notes   .dat           2020-6-30 23:31        1KB")
                        System32=input("Enter filename(sample:\"C:\"):")
                        qing()
                        if System32==".drives":
                            b("Этот сервис содержит:Приложение стартового обслуживания для третьей стороны(Отключена)")
                        elif System32=="Taiwan":
                            sleep(0.2)
                            print("This program cannot run in x64 mode.")
                        else:
                            print("Bad command or file name.")
                    elif System32==name:
                        print("Name    Type            Modify date            Size")
                        print("user    .dll            2020-12-7 17:56        1KB")
                        print("data    .gho            2020-12-7 17:57        1KB")
                    else:
                        print("Bad command or file name.")
                elif System32=="F:" and ds_3==1:
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
                    if System32=="F:":
                        print("无法读取这个磁盘，请检查磁盘是否被拔出或移动，再检查是否安装磁盘管理软件。")
                    else:
                        print("该磁盘不存在")
            elif prog=="9":
                print("\033[0m1.开机和登录 2.软件 3.浏览器问题 4.升级Pan 5.重装系统")
                rm=input()
                qing()
                if rm=="1":
                    b("1)360报告卡顿现象\n清理电脑垃圾或重启机器即可，如问题严重，请换个浏览器(推荐Chrome)或重装系统(推荐win8.1，iPadOS)。\n2)基本信息可以不填么?\n可以，但是最好填(也可以在开始菜单打开命令提示符输入modify更改)，姓名栏可以写您的真实名字，也可以写您的昵称。")
                    b("\n3)用电脑能正常运行PanMe吗?\n能，系统最好Win7以上，如果只想体验触摸系统(平板系统)，建议使用iPad\n4)为什么我一启动机器就会报告蓝屏?\n可能是您在开机时输入了一些东西或者系统发生了一些小错误导致的，如果问题严重，可以降级到PanTSE 2.1")
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
            elif prog=="10":
                print("\033[42m")
                qing()
                print("📺    你尚未联网，应用商店需要联网才能使用，请检查网络后重试。")
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
                            b("\033[0mPan Me Home")
                            b("©2021 HOTM workshop。保留所有权利。")
                            b("\n\n\033[90m系统")
                            b("\033[0m处理器:HOTM,X86720P-Virtual Emulator")
                            b("已安装的RAM:536MB(512.1MB可用)")
                            b("笔和触控:没有可用于此显示器的笔或触控输入")
                            b("\n\n\033[90m计算机名，域和工作组设置")
                            b("\033[0m计算机名:START-T8CF78L")
                            b("\033[0m描述:Pan Me in Xueersi Coding.")
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
                                    b("当前主题:Pan Me Basic")
                                b("更改主题:A.Pan经典 B.Pan Me Basic C.Pan Me Aero D.主题属性")
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
                                    b("Pan Me Basic")
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
                                    b("Pan Me Aero")
                                    b("背景:Harmony")
                                    b("颜色:蓝色")
                                    b("声音:不支持")
                                    b("鼠标光标:为支持5点触控及以上的触摸显示屏提供支持")
                                    b("\033[90m由于你的显卡不支持此主题，你不能使用这个主题")
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
    elif panme=="1":
        for i in range(3):
            print("_")
            sleep(0.2)
            qing()
            sleep(0.2)
        print("\033[107m")
        sleep(1)
        qing()
        print("                                 \033[90mHOTM©\n\n")
        print('''            \033[94m______    \033[91m ______
            \033[94m|     \   \033[91m|     |    \033[93m|\   |
            \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
            \033[94m|         \033[91m|     |    \033[93m|  \ |
            \033[94m|         \033[91m|     |    \033[93m|   \|
        ''')
        print("\033[90m  HOTM")
        print("\033[92m   Pan® Me Ultimate Edition")
        print("\n\033[93m           Starting up...\n",end="")
        print("\033[43m"+40*" ")
        sleep(3)
        print("\033[0m")
        qing()
        sleep(2)
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
            print("\033[90mPan 公测版本\n评估副本。过期时间2021/5/20。\033[0m")
            if classic==0 or classic==2:
                if classic==2:
                    print("\033[101m")
                    qing()
                print("\033[0m开始                        "+name)
                print("\033[90m0.关机  \033[30m1.待机    \033[91m2.计算器")
                print("\033[31m3.记事本        \033[92m4.重启（不会丢失数据)")
                print("\033[32m5.系统属性    \033[93m6.命令提示符    \033[33m7.有道     \033[94m8.地图 ")
                print("\033[95m9.浏览器        \033[34m10.计算机      \033[35m11.Pan系统入门 \033[96m12.应用商店")
                prog=input("\033[0m请输入应用序号:")
            else:
                print("\033[103m")
                qing()
                print("现在是",strftime("%Y年%m月%d日 %H点%M分%S秒",localtime()))
                print("\033[90m0.关机\n\033[30m1.待机\n\033[91m2.计算器")
                print("\033[31m3.记事本\n\033[92m4.重启（不会丢失数据)")
                print("\033[32m5.系统属性\n\033[33m6.命令提示符\n\033[33m7.有道\n\033[94m8.地图 ")
                print("\033[95m9.浏览器\n\033[34m10.计算机\n\033[35m11.Pan系统入门\n\033[96m12.应用商店")
                prog=input("\033[0;103m请输入应用序号:")
    
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
            if classic==0:
                print("\033[0m"+strftime("%H:%M",localtime()))
            
            print("\033[0m")
            qing()
            print("\033[90mPan 公测版本\n评估副本。过期时间2021/5/20。\033[0m")
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
                print("\033[104m  \033[0m\033[103m  \033[0mPan\033[92mMultiple Edition")
                print("\033[0mHOTM Pan")
                print("版本5.11(内部版本 Build 4016)")
                print("版权所有 ©2021 HOTM Workshop。保留所有权利。")
                print("PanMe 旗舰版 操作系统及其用户界面受中国大陆和其他国家/地区的商标法和其他待颁布或已颁布的知识产权法保护")
                input("看完按Enter")
            elif prog=="6":
                print("\033[0mHOTM Pan[版本5.11.4016]")
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
                        print("HOTM Pan[版本5.11.4016]")
                        print("版权所有 (c) 2021 HOTM Workshop。保留所有权利。")
                    elif dos=="break" or dos=="exit":
                        break
                    elif dos=="panver":
                        print("HOTM Pan[版本5.11.4016]")
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
                print("\033[0mUltimate(C:)\n2.68GB可用/4.00GB")
                print("\033[0mHomeSTD(D:)\n768MB可用/2.00GB")
                print("\033[0mStarter(E:)\n1.25GB可用/2.00GB")
                print("\033[0m💽 CD-ROM驱动器(F:)")
                if ds_3==1:
                    print("0Byte可用/6.55GB NTFS磁盘格式")
                else:
                    print("驱动器不可用 RAW磁盘格式")
                System32=input("输入文件名，(如C:):")
                qing()
                if System32=="C:":
                    print("名称    类型           修改日期               大小")
                    print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1KB")
                    print("Program 文件夹         2021年1月27日 17:10    119.9MB")
                    print("local   文件夹         2020年6月14日 13:25    1.7GB")
                    print(name+"   文件夹         2020年12月7日 17:54    100MB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="local":
                        print("名称    类型            修改日期               大小")
                        print("Start   软件(.exe)      2020年6月14日 13:23    931MB")
                        print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                        print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                        print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                    elif System32=="Program":
                        print("名称    类型           修改日期               大小")
                        print("%temp%  缓存(.tmp)     2020年7月19日 13:23    27KB")
                        print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                        print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
                        print("Notes   数据(.dat)     2020年6月30日 23:31    1KB")
                        System32=input("输入文件名，(如C:):")
                        qing()
                        if System32==".drives":
                            b("该服务包括:第三方程序启动服务(已启用)")
                        else:
                            print("该文件不存在或不可更改")
                    elif System32==name:
                        print("名称    类型            修改日期               大小")
                        print("user    扩展驱动(.dll)  2020年12月7日 17:56    1KB")
                        print("data    备份文件(.gho)  2020年12月7日 17:57    1KB")
                    else:
                        print("该文件不存在")
                elif System32=="D:":
                    print("名称    类型            修改日期               大小")
                    print("Boot    系统安装包(.wim)2021年2月19日 18:01    225MB")
                    print("Start   快捷方式(.lnk)  2020年6月14日 13:23    1KB")
                    print("Program 文件夹          2021年1月27日 17:10    119.9MB")
                    print("local   文件夹          2020年6月14日 13:25    1.7GB")
                    print(name+"   文件夹          2020年12月7日 17:54    100MB")
                    System32=input("输入文件名，(如C:):")
                    qing()
                    if System32=="local":
                        print("名称    类型            修改日期               大小")
                        print("Start   软件(.exe)      2020年6月14日 13:23    640MB")
                        print("program 软件(.exe)      2020年6月14日 13:27    245MB")
                        print("System  配置文件(.ini)  2020年6月14日 13:30    1MB")
                        print("Startup 软件(.exe)      2020年6月14日 13:31    992KB")
                    elif System32=="Program":
                        print("名称    类型           修改日期               大小")
                        print("program 软件(.exe)     2020年7月19日 13:23    117MB")
                        print(".drives 扩展驱动(.dll) 2021年1月27日 17:10    2.9MB")
                        print(".drives 软件服务(.pnc) 2021年1月27日 17:14    1KB")
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
                else:
                    if System32=="F:":
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
                print("📺    你尚未联网，应用商店需要联网才能使用，请检查网络后重试。")
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
                            b("\033[0mPan Me Ultimate")
                            b("©2021 HOTM workshop。保留所有权利。")
                            b("\n\n\033[90m系统")
                            b("\033[0m处理器:HOTM,X86720P-Virtual Emulator")
                            b("已安装的RAM:536MB(512.1MB可用)")
                            b("笔和触控:没有可用于此显示器的笔或触控输入")
                            b("\n\n\033[90m计算机名，域和工作组设置")
                            b("\033[0m计算机名:START-T8CF78L")
                            b("\033[0m描述:Pan Me in Xueersi Coding.")
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
                                    b("当前主题:Pan Me Basic")
                                b("更改主题:A.Pan经典 B.Pan Me Basic C.Pan Me Aero D.主题属性")
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
                                    b("Pan TSE Aero")
                                    b("背景:Harmony")
                                    b("颜色:绿色")
                                    b("声音:Vista(远景)")
                                    b("鼠标光标:为支持5点触控及以上的触摸显示屏提供支持")
                                    b("\033[90m由于你的显卡不支持此主题，你不能使用这个主题")
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
