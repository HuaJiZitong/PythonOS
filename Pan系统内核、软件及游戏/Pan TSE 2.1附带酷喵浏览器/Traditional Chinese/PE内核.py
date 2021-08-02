from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*
import platform
import requests
#-----------------------------------導庫-------------------------------
ds_1=0
ds_2=0
ds_4=0
ds_5=0
wfp=1.5
e=2.0
obj=0
classic=0
jsb=["使用Pan TSE的記事本記録代辦選項"]
ID=randint(10000,99999999)
def error(err):
    print("\033[0;44m")
    qing()
    for i in range(0,100,5):
        sleep(0.46)
        qing()
        print(":(")
        print("你(妳)的電腦遇到問題，需要重開機。")
        print("我們只采集某些錯誤信息，然後爲你(妳)重開機。(完成"+str(i)+"%)")
        print("如果你(妳)想知曉更多信息，則可以稍後查找此錯誤:"+err)
    print("請摁運行鍵繼續...")

def qing():
    system("clear")

def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    print()

def kfz():
    while 1:
        print("\033[0m開始                        SYSTEM")
        print("\033[95m1.命令提示符    \033[93m2.計算機      \033[92m3.記事本     \033[90m4.離開Pan     \033[91m5.手動Ghost")
        print("\033[93mD.管理磁碟機")
        print("\033[0m"+strftime("%H:%M",localtime()))
        kfz=input("\033[0m鍵入程式序號:")
        qing()
        if kfz=="1":
            print("\033[0mHOTM Pan[開發員版本3902]")
            print("版權屬於 (c) 2020 HOTM Workshop。留下所有權利。")
            while 1:
                print("C:\\local>",end="")
                dos=input()
                if dos=="help":
                    print("有關某個命令的詳細信息，請鍵入help名稱")
                    print("break    離開cmd程式，這與exit是壹樣的")
                    print("clear    清掃熒屏")
                    print("cmd      開啟壹個新的Pan命令解釋視窗")
                    print("exit     離開cmd程式")
                    print("help     列舉Pan的所有命令代碼信息")
                    print("panver   查看Pan的版本")
                    print("bsod     自動藍屏而不破壞系統")
                    print("shutdown 離開Pan")
                elif dos=="clear":
                    qing()
                elif dos=="cmd":
                    print("\033[0mHOTM Pan[開發員版本3902]")
                    print("版權屬於 (c) 2020 HOTM Workshop。留下所有權利。")
                elif dos=="break" or dos=="exit":
                    break
                elif dos=="panver":
                    print("HOTM Pan[版本3.65.3902]")
                elif dos=="bsod" or dos=="shutdown":
                    print("請稍等\n正在離開CMD程式")
                    break
                else:
                    print("無效命令代碼")
            if dos=="bsod":
                qing()
                error("Cannot perform normal shutdown")
                break
            elif dos=="shutdown":
                for i in range(5):
                    print("\033[0mo 正在離開Pan")
                    sleep(0.2)
                    system("clear")
                    print("\033[94mo 正在離開Pan")
                    sleep(0.2)
                    system("clear")
                sleep(1)
                qing()
                print("\033[92m現在你(妳)可以安全地關閉你(妳)的電腦了\033[8m")
                break
        elif kfz=="2":
            print("\033[0mSystem(C:)\n6.18京位元組可用/8.00京位元組")
            print("\033[0m備份Ghost(E:)\n"+str(e-0.1)+"京位元組可用/"+str(e)+"京位元組")
            print("\033[90mCD-ROM驅動器(D:)\n不可用\033[0m")
            System32=input("鍵入檔案名，(如C:):")
            qing()
            if System32=="C:":
                print("名稱    類型           修改日期               大小")
                print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1024位元組")
                print("Program 檔案袋         2021年1月27日 17:10    126兆位元組")
                print("local   檔案袋         2020年6月14日 13:25    1.7京位元組")
                print(name+"   檔案袋         2020年12月7日 17:54    100兆位元組")
                System32=input("鍵入檔案名，(如C:):")
                qing()
                if System32=="local":
                    print("名稱    類型           修改日期               大小")
                    print("Start   程式(.exe)      2020年6月14日 13:23    1.3京位元組")
                    print("Touch   擴展驅動(.dll)  2020年6月14日 13:26    153兆位元組")
                    print("program 程式(.exe)      2020年6月14日 13:27    245兆位元組")
                    print("System  配置檔案(.ini)  2020年6月14日 13:30    1兆位元組")
                    print("Startup 程式(.exe)      2020年6月14日 13:31    99萬位元組")
                elif System32=="Program":
                    print("名稱    類型           修改日期               大小")
                    print("program 程式(.exe)     2020年7月19日 13:23    117兆位元組")
                    print(".drives 擴展驅動(.dll) 2021年1月27日 17:10    2.9兆位元組")
                    print(".drives 程式服務(.pnc) 2021年1月27日 17:14    689位元組")
                    print("Taiwan  語言包(.bin)   2021年1月27日 17:15    873位元組")
                    System32=input("輸入文件名，(如C:):")
                    qing()
                    if System32==".drives":
                        b("該服務包含:第三方程式啟動服務(已啟用)")
                    elif System32=="Taiwan":
                        sleep(0.2)
                        print("Your PC language is Traditional Chinese now.")
                    else:
                        print("該檔案不存在或不可更改")
                elif System32==name:
                    print("名稱    類型            修改日期               大小")
                    print("user    擴展驅動(.dll)  2020年12月7日 17:56    957位元組")
                    print("data    備份檔案(.gho)  2020年12月7日 17:57    289位元組")
                else:
                    print("該檔案不存在")
            elif System32=="E:":
                print("名稱    類型             修改日期                大小")
                print("Ghost   擴展驅動(.dll)   2020年7月18日  19:38    53兆位元組")
                print("PanTSE2 系統安裝包(.wim) 2020年10月1日  18:59    46.5兆位元組")
                print("readme  文本(.txt)       2020年10月1日  19:02    407.6千位元組")
                print("TSE21   鏡像(.iso)       2020年11月26日 15:37    904千位元組")
                print("develop 命令檔案(.bat)   2020年11月17日 11:55    78位元組")
                print("data    配置檔案(.ini)   2020年11月18日 0:02     96位元組")
                System32=input("輸入文件名，(如C:):")
                qing()
                if System32=="readme":
                    b("本磁碟機是重置系統備份的磁碟機\n")
                    b("【請勿重新格式化】\n【請勿刪除檔案】\n【請勿添加檔案】\n")
                    b("否則，系統將永久崩潰，切記~~~~~~")
                elif System32=="develop":
                    print("您要如何查看該檔案?")
                    System32=input("A.16位的CMD B.32位的CMD C.記事本")
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
                        print("該檔案不態以程式"+System32+"來打開")
                else:
                    print("該檔案不可預覽")
            elif System32=="D:":
                print("該磁碟機裏沒有可用的安裝檔案(setup.exe或者oemsetup.inf)，也沒有可查看的檔案。")
            else:
                print("該檔案不存在")
        elif kfz=="3":
            while 1:
                qing()
                print("\033[?25h\033[32m歡迎使用記事本!\033[34m鍵入已有記事本名打開,\033[33m鍵入新名字即可創建,\033[31m鍵入exit退出,\033[35m鍵入recycle查看廢紙簍")
                print("\033[33m已有記事本:\033[0m")
                for i in jsb:
                    print(i)
                j=input("\033[36m鍵入記事本名:")
                qing()
                if j.lower()=='exit':
                    print("\033[?25l")
                    break
                elif j.lower()=='recovery':
                    print("\033[36m| Pan Recovered files\033[32m")
                    for i in jsbrc:
                        print("\033[32m記事本名穪 : "+str(i))
                        print("\033[33m記事本內容 : 見下行\n"+str(jsbrc[i]))
                        print()
                    input("\033[36m（recovery內容無法恢複，只支持臨時查看，文章中\033[34m\\n\033[36m代表換行；回車鍵返回。）")  
                elif j.lower()=='recycle':
                    print("\033[36m| 記事本回收站\033[32m")
                    for i in jsbr:
                        print(i)
                    cao = input("\033[36m輸入要執行的操作(1=恢複 2=徹底刪除 3=全部徹底刪除 4=全部恢複)：")
                    if cao != '3' and cao != '4':
                        jj = input("\033[33m輸入要操作的記事本名：")
                    elif cao == '1':
                        if jj in jsbr:
                            jsb[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m恢複成功！")
                        else:
                            print("\033[31m記事本名輸入錯誤")
                    elif cao == '2':
                        if jj in jsbr:
                            jsbrc[jj] = jsbr[jj]
                            del jsbr[jj]
                            print("\033[32m徹底刪除成功！")
                        else:
                            print("\033[31m記事本名輸入錯誤")
                    elif cao == '3':
                        for i in jsbr:
                            jsbrc[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在抹掉......")
                        sleep(0.5)
                        print("\033[32m刪除成功！")
                    elif cao == '4':
                        for i in jsbr:
                            jsb[i] = jsbr[i]
                        del jsbr
                        jsbr = {}
                        print("\033[36m正在恢複......")
                        sleep(0.5)
                        print("\033[32m恢複成功！")
                    else:
                        print("\033[31m無效操作")
                    input("\033[35mEnter鍵返回")
                elif j in jsb:
                    print(jsb[j])
                    print("\033[33m1.更改 \033[31m2.刪除 \033[34m3.重命名 \033[31m其他退出")
                    c=input("\033[0m請選擇：")
                    if c=='1':
                        qing()
                        nr = ''
                        print("\033[32m輸入記事本內容，輸入esc完成，輸入clear清空所有內容。\033[33m")
                        while 1:
                            a = input()
                            if a == 'esc':
                                break
                            elif a == 'clear':
                                nr = ''
                                qing()
                                print("\033[32m輸入更改後的內容，輸入esc完成，輸入clear清空所有內容。\033[33m")
                                continue
                            elif '<fontcolor='in a:
                                if len(a) < 12:
                                    print("\033[31m語法錯誤：<fontcolor=  value error:is no color input\033[33m")
                                    continue
                                if a[11] == '紅':
                                    nr = nr + '\033[31m'
                                elif a[11] == '綠':
                                    nr = nr + '\033[32m'
                                elif a[11] == '黃':
                                    nr = nr + '\033[33m'
                                elif a[11] == '藍':
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
                        print("\033[32m刪除成功，可在回收站查看!")
                    elif c=='3':
                        new=input("\033[36m輸入新記事本名:")
                        if new=='exit':
                            print("\033[31m不可使用關鍵詞exit命名記事本!")
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
                    print("\033[32m輸入記事本內容，輸入esc完成，輸入clear清空所有內容。\033[33m")
                    while True:
                        a = input()
                        if a == 'esc':
                            break
                        elif a == 'clear':
                            nr = ''
                            qing()
                            print("\033[32m輸入記事本內容，輸入esc完成，輸入clear清空所有內容。\033[33m")
                            continue
                        elif '<fontcolor='in a:
                            if len(a) < 12:
                                print("\033[31m語法錯誤：<fontcolor=  value error:is no color input\033[33m")
                                continue
                            if a[11] == '紅':
                                nr = nr + '\033[31m'
                            elif a[11] == '綠':
                                nr = nr + '\033[32m'
                            elif a[11] == '黃':
                                nr = nr + '\033[33m'
                            elif a[11] == '藍':
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
                print("\033[0mo 正在關機")
                sleep(0.2)
                system("clear")
                print("\033[94mo 正在關機")
                sleep(0.2)
                system("clear")
            sleep(1)
            qing()
            print("\033[92m現在你(妳)可以安全地關閉你(妳)的電腦了\033[8m")
            break
        elif kfz=="5":
            setup()
        elif kfz=="D":
            print("\033[0mVirtualDisk(11.6GB)")
            print("\033[90mSystem(C: 8.00GB) \033[94m備份GHOST(E: "+str(e)+"GB) 未分配("+str(wfp)+"GB)  \033[90mEFI恢複分區(0.1GB)")
            print("\033[0m光盤(0Byte)")
            print("\033[90mCD-ROM驅動器(D: 0Byte)")
            disk=input("\033[0m選擇要更改的分區(填寫盤符，沒有盤符填名稱，如E:)")
            qing()
            if disk=="C:" or disk=="D:":
                print("該分區已被組織HOTM鎖定，不可更改")
                sleep(3)
                disk=input("是否繼續更改?(Y|N)")
                if disk=="Y":
                    qing()
                    error("operating system not found")
                    break
                else:
                    print("好的，即將返回桌面")
            elif disk=="EFI恢複分區":
                print("A.查看文件 B.屬性")
                disk=input()
                qing()
                if disk=="A":
                    print("名稱    類型             修改日期               大小")
                    print("BIOS    固件(.bin)       2020年6月14日 13:23    128KB")
                    print("config  數據(.dat)       2020年7月6日 15:42     105KB")
                elif disk=="B":
                    print("EFI恢複分區")
                    print("可用空間:99.77MB")
                    print("總空間:100MB")
                else:
                    print("該操作無效。")
            elif disk=="E:":
                disk=input("A.壓縮卷 B.屬性 C.擴展卷\n")
                print("\033[41m")
                qing()
                if disk=="A":
                    print("歡迎使用壓縮卷功能\n本功能會幫助你(妳)壓縮E盤，節約出壹個空閑空間")
                    print("正在查詢可用空間...")
                    sleep(3)
                    qing()
                    print("歡迎使用壓縮卷\n本功能會幫助你(妳)壓縮E盤，節約出壹個空閑空間")
                    print("可壓縮:"+str(e-0.25)+"GB\n\033[90mTIP:必須要預留壹些空間供磁盤完成任務")
                    disk=input("\033[94m輸入要壓縮的空間:")
                    qing()
                    if float(disk)>e-0.25:
                        print("壓縮後的空間太小！請重新選擇！")
                    else:
                        print("正在壓縮...")
                        wfp=wfp+float(disk)
                        e=e-float(disk)
                        sleep(2)
                        print("壓縮成功！E盤剩余空間爲"+str(e)+"GB!")
                elif disk=="B":
                    print("備份GHOST(E:)")
                    print("\033[94m可用空間:"+str(e-0.1)+"GB")
                    print("已用空間:0.1GB")
                    print("總容量:"+str(e)+"GB")
                elif disk=="C":
                    print("歡迎使用擴展卷功能\n本功能會幫助你(妳)擴大E盤")
                    print("正在查詢可用空間...")
                    sleep(3)
                    qing()
                    print("歡迎使用擴展卷功能\n本功能會幫助你(妳)擴大E盤")
                    print("可擴展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m輸入要擴展的空間:")
                    qing()
                    if float(disk)>wfp:
                        print("要擴展的空間太大！無法擴容！")
                    else:
                        print("正在擴展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("擴展成功！E盤剩余空間爲"+str(e)+"GB!")
                else:
                    print("該操作無效。")
            elif disk=="未分配":
                disk=input("A.屬性 B.與E盤合並")
                if disk=="A":
                    print("未分配")
                    print("\033[92m已准備就緒！等待分配分區中")
                    print("\033[0m總容量:"+str(wfp)+"GB")
                elif disk=="B":
                    print("歡迎使用合並功能\n本功能會幫助你(妳)將未分配與E盤合並")
                    print("正在查詢可用空間...")
                    sleep(3)
                    qing()
                    print("歡迎使用合並功能\n本功能會幫助你(妳)將未分配與E盤合並")
                    print("可擴展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m輸入要擴展的空間:")
                    qing()
                    if float(disk)>wfp:
                        print("要擴展的空間太大！無法擴容！")
                    else:
                        print("正在擴展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("擴展成功！E盤剩余空間爲"+str(e)+"GB!")
            else:
                print("該磁盤不存在")
        else:
            software_len = len(kfz)
            NUMBER = ['壹','二','三','四','五','六','七','八','九','十','十壹','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十壹','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十']
            try:
                software2 = int(kfz)
                YUAN = "您輸入了不合法的編號，請您輸入正確編號~"
            except:
                if kfz == "" or kfz == " " or kfz == " "*software_len:
                    YUAN = "您什麽也沒輸入喲~"
                elif kfz in NUMBER:
                    YUAN = "請輸入阿拉伯數字,不可輸入漢字~"
                elif kfz[0:3] == "www" or kfz[0:4] == "http":
                    YUAN = "不支持輸入網址~"
                else:
                    YUAN = "您輸入了程序名,請輸入編號~"
            qing()
            print()
            print()
            print("\033[33m系統未查找到軟件 - {} -".format(kfz))
            print("\033[36m原因:{}".format(YUAN))
            sleep(0.5)
            input("\033[32mEnter鍵返回開始菜單。")
            qing()
            continue
        print("\n10秒後返回開始菜單\033[000m")
        sleep(10)
        qing()
        continue

def setup():
    print("\033[44m")
    qing()
    print("\033[7mP\033[0;44man Setup")
    print("准備工作...\n備份文件到E盤")
    print("C:\\"+name+"\\user.dll")
    sleep(0.09)
    print("C:\\"+name+"\\data.gho")
    sleep(0.2)
    qing()
    print("\033[7mP\033[0;44man Setup")
    print("\033[107m \033[104m            Finding ISO File            [x]\033[107m \033[44m")
    print("\033[107;30m查找可安裝的鏡像...                          \033[44m")
    sleep(15)
    qing()
    print("\033[7mP\033[0;44man Setup")
    print("\033[107m \033[104m            Choose Operating System            [x]\033[107m \033[44m")
    print("\033[107;30m正在重裝系統                                        \033[44m\n\033[107m選擇你(妳)的系統:(共找到6個鏡像，3個鏡像有效)"+11*" "+"\033[44m\n\033[107mPan TSE 2.1                                         \033[44m\n\033[107mPan TSE2原版                                        \033[44m\n\033[107mPan Developer PE                                    \033[44m\033[107m\n"+52*" ")
    efi=input("\033[101m請輸入(區分大小寫和空格):"+27*" "+"\n\033[1A請輸入(區分大小寫和空格):")
    print("\033[0m")
    qing()
    if efi=="Pan TSE 2.1":
        for i in range(0,904,int(69.5)):
            print("正在解壓ISO("+str(i)+"KB/904KB)")
            sleep(0.2)
            system("clear")
    elif efi=="Pan TSE2原版":
        for i in range(0,int(46.5),int(11.6)):
            print("正在解壓ISO("+str(i)+"MB/46.5MB)")
            sleep(0.2)
            system("clear")
    elif efi=="Pan Developer PE":
        print("正在重置PE")
        print("重新格式化PE系統盤...")
        sleep(3)
        qing()
        print("正在重置PE")
        print("寫入文件...")
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
        print("執行develop.bat...")
        sleep(2)
        system("clear")
        print("重置成功!")
    else:
        print("正在解壓文件(0B/0B)")
        sleep(0.01)
        system("clear")
        print("解壓WIM或ISO失敗，系統中斷重裝!")
        sleep(0.2)
        print("正在回滾操作...")
  
    if efi=="Pan TSE 2.1" or efi=="Pan TSE2原版":
        sleep(3)
        qing()
        print("正在獲取電腦配置")
        sleep(5)
        print("正在配置Pan")
        sleep(20)
        sb=randint(0,10)#沒有罵人，在這裏sb是“失敗”的縮寫
        if sb==5:
            print("配置Pan失敗，正在還原配置")
            sleep(5)
        print("正在複制文件")
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
        print("所有文件都已複制成功")
        sleep(3)
        qing()
        print("准備就緒...")
        sleep(randint(2,15)-2)
        print("\033[44m")
        qing()
        print("\033[7mP\033[0;44man Setup")
        print("\033[107m \033[104m            Preparing Pan            [x]\033[107m \033[44m")
        print("\033[107;90m准備就緒..."+31*" "+"\033[44m")
        sleep(2)
        qing()
        print("\033[7mP\033[0;44man Setup")
        print("\033[107m \033[104m  Registered OK  [x]\033[107m \033[44;90m")
        print("\033[107m准備完成！"+12*" "+"\033[44m\n\033[107m您的數據和用戶信息成功\033[44m\n\033[107m的保存了下來，系統也重\033[44m\n\033[107m裝完成，接下來您可以盡\033[44m\n\033[107m情使用Pan TSE了"+7*" "+"\033[44m\n\033[107m5秒後進入系統         ")
        sleep(5)
        qing()
try:
    print("\033[?25l",end="")
    su1=time()
    sleep(0.3)
    print("BIOS checking system is checking disk",end="")
    sleep(2)
    print("...done")
    sleep(0.1)
    print("Startup Pan TSE 2.1 Traditional Chinese Edition...")
    sleep(1)
    system("clear")
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
    kfz()
except Exception as e:
    qing()
    error(str(e))
