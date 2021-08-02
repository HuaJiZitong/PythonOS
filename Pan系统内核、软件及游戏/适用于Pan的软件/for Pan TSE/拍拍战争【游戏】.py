print("\033[93m通知:这不是玩游戏的最佳分辨率，最佳分辨率是1366×768")
if 1:
    if 1:
        if 1:
            while 1:
                pp=input("(X键退出)\033[91mA.单人赛 \033[92mB.生存大乱斗 \033[90mC.3v3(即将推出) D.5v5(即将推出) \033[93mE.玩法说明\033[0m")
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