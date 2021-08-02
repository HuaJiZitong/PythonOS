while 1:
if 1:
    if 1:
        if 1:
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