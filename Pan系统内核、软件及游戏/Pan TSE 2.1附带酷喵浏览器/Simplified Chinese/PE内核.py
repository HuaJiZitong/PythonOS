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
    while 1:
        print("\033[0m开始                        SYSTEM")
        print("\033[95m1.命令提示符    \033[93m2.计算机      \033[92m3.记事本     \033[90m4.关机     \033[91m5.手动Ghost")
        print("\033[93mD.管理磁盘")
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
        elif kfz=="2":
            print("\033[0mSystem(C:)\n6.18GB可用/8.00GB")
            print("\033[0m备份Ghost(E:)\n"+str(e-0.1)+"GB可用/"+str(e)+"GB")
            print("\033[90mCD-ROM驱动器(D:)\n不可用\033[0m")
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
    kfz()
except Exception as e:
    qing()
    error(str(e))