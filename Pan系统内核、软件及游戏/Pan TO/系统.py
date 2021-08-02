print("           🌁")
if 1:
    if 1:
        if 1:
            if 1:
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
                mm_to=input("请输入密码")
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
                        print("此电脑制造商:\033[3mPan Virtual PC\033[0m")
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