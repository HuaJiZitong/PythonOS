print("\033[0m1.Pan1.0    2.PanTO    3.Pan3.0")
if 1:
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