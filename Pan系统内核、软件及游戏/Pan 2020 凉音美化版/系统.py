from time import *
from xes.ext import *
from random import *
from os import *
from sys import*
from math import*
from string import*
import platform
import requests
import urllib.request
import re

chrome=0
def p81():
    money=0
    dl1=0
    dl2=0
    def b(p):
        for char in p:
            sleep(0.1)
            print(char, end='', flush=True)
            
    
    print('''\033[?25l       \033[94m______    \033[91m ______
            \033[94m|     \   \033[91m|     |    \033[93m|\   |
            \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
            \033[94m|         \033[91m|     |    \033[93m|  \ |
            \033[94m|         \033[91m|     |    \033[93m|   \|
    ''')
    print("\n\n\n\n\033[0m to interrupt normal startup,press Enter")
    sleep(0.2)
    system("clear")
    sleep(2)
    print("\033[107m")
    system("clear")
    print("                                 \033[90mHOTM©\n\n")
    print('''       \033[94m______    \033[91m ______
            \033[94m|     \   \033[91m|     |    \033[93m|\   |
            \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
            \033[94m|         \033[91m|     |    \033[93m|  \ |
            \033[94m|         \033[91m|     |    \033[93m|   \|
    ''')
    print("\033[90m  HOTM")
    print("\033[92m   Pan® 81 Professional Workstation")
    print("\n\033[93m           Starting up...\n",end="")
    print("\033[43m"+40*" ")
    sleep(2)
    print("\033[0m")
    system("clear")
    while 1:
        print("-------PAN 81 PRO-------")
        print("选择登录选项:")
        choo=int(input("1.直接体验 2.用户登录"))
        if choo==2:
            print("▢Pan管家")
            name=input("输入你的名字:")
            system("clear")
            print("-------PAN 81 PRO-------")
            print("选择登录选项:")
            print("1.直接体验 2.用户登录2")
            print("▢Pan管家")
            print("输入你的名字:",name[0]+"**")
            if name=="潘夕习":
                admin=1
                phone=15280411019
                sex="男"
                money=10000
                print("佬潘，识别出你是管理员，为特级VIP")
                speak("尊敬的VIP用户，欢迎回来~")
            elif name=="刘佳昱":
                phone=0
                sex="男"
                money=1000
                print("识别出你是战略合作伙伴，为一级VIP")
                speak("尊敬的VIP用户，欢迎回来~")
            elif name=="叶炳辰" or name=="梅谭晓":
                phone=3474885420
                sex="男"
                money=5000
                print("识别出你是Pan室友，为一级VIP")
                speak("尊敬的VIP用户，欢迎回来~")
            elif name=="曾浩航":
                phone=0
                sex="男"
                money=3500
                print("识别出你是战略合作伙伴，为二级VIP")
                speak("尊敬的VIP用户，欢迎回来~")
            else:
                print("你的Pan账号为试用账号，该账号将在系统关机前有效。")
                sleep(2.7)
            system("clear")
            break
        elif choo==1:
            system("clear")
            break
        else:
            continue
    
    while 1:
        date=strftime("%Y年%m月%d日",localtime())
        local=strftime("%H:%M",localtime())
        if date=="2021年01月20日":
            print(date,"腊八节")
        elif date=="2021年02月12日":
            print(date,"春节")
        elif date=="2021年02月26日":
            print(date,"元宵节")
        elif date=="2021年03月14日":
            print(date,"植树节")
        elif date=="2021年04月01日":
            print(date,"愚人节")
        elif date=="2021年06月01日":
            print(date,"儿童节")
        elif date=="2021年09月10日":
            print(date,"教师节")
        elif date=="2021年10月01日":
            print(date,"国庆节")
        elif date=="2021年10月24日":
            print(date,"程序员节")
        else:
            print(date)
        print(local)
        print('''0.关机
1.计算器（平均数）
2.计算器
3.计算器（鸡兔同笼）
4.计算器（年龄）
5.更新
6.口算赢红包
7.Minecraft
8.Python所有函数
9.测网速
10.鲁大师
11.微信读书
12.三国杀
13.应用商城
14.佬潘解说骗赞程序
15.支付宝
16.学而思网校
17.加入Pan工作室
18.意见反馈
19.幻觉
20.“错误”的代码
21.申请加入PanVIP会员
22.Pan工作室logo
23.教你如何与女生斗嘴
24.关于假“代码运行结束”的区分
25.开启斜体特效
26.开启下划线特效
27.关闭特效
28.护眼模式''')
        if dl1==1:
            print("29.百度")
        elif dl2==1:
            print("30.抖音")
        prog=int(input("输入程序序号"))
        system("clear")
        if prog==0:
            print("o 正在关机")
            sleep(2)
            break
        elif prog==2:
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
                print("Error:invalid syntax")
        elif prog==1:
            gs=int(input("有几个数"))
            pjs=0
            for i in range(gs):
                s=int(input("输入数字："))
                pjs=pjs+s
            pjs=pjs/gs
            print("平均数是:",pjs)
        elif prog==3:
            feet=int(input("有几只脚"))
            chicken=feet-(head*2)
            rabbit=chicken/4
            chicken=head-rabbit
            print("鸡有",int(chicken),"只，兔有",int(rabbit),"只")
        elif prog==4:
            new=int(input("输入已知年龄"))
            old=int(input("已知年龄到了这个年纪之后，老的多少岁？(已知年龄<未知年龄)"))
            print("老的年龄是",(old-new)/2,"岁")
        elif prog==5:
            print("正在检测更新······")
            sleep(2)
            print("运行Pro版本:PanNT内核v5.2(Pan TSE 2.1 SP1)，已是最新")
            sleep(0.85)
            print("运行XP（学生版）版本:PanTSE1适用于老系统的XP版本，已是最新")
        elif prog==6:
            print("剩余金币:",money)
            print("算一道题得10金币。")
            t=int(input("你要算几题:"))
            for i in range(t+1):
                js1=randint(0,100)
                js2=randint(0,100)
                print(js1,"+",js2,"= ？")
                h=int(input())
                if h==js1+js2:
                    print("哇哦，答对了，奖励10金币")
                    m=m+10
                    speak("你真牛皮class")
                    play_mp3("lala.mp3")
                else:
                    print("你答错了！，答案是",js1+js2)
                    print("失败是成功之母，下次努力！")
                    play_mp3("try again.mp3")
                    sleep(2)
                    system("clear")
        elif prog==7:
            print("启动Minecraft")
            speak("欢迎游玩Minecraft（我的世界）1.2.3")
            c=int(input("选择模式:\n1.建造 2.生存"))
            w=input("输入世界名称（输入0不命名）:")
            if w!="0":
                print(w,".mcw")
            else:
                print("新世界1.mcw")
            print("*.mcw*是MC世界的后缀。")
            sleep(2)
            system("clear")
            if c==1:
                print("你在一个森林里。")
                print("现在最要紧的是建个房子，以防僵尸吃人。")
                print("你要去_____找材料。")
                c=int(input("1.砍树 2.采矿"))
                if c==1:
                    print("你弄了许多木头，但是你觉得还缺了什么。")
                    c=int(input("1.去溺僵尸 2.去矿洞"))
                    if c==1:
                        print("你和僵尸同归于尽了。")
                    elif c==2:
                        print("你挖了许多矿物，做了许多装备。")
                        print("你建好了房，但是房里有一处还是很可疑。")
                        print("1.查看 2.不查看")
                        c=int(input())
                        if c==1:
                            print("你移开了衣柜，看到有一个传送门。")
                            print("突然你到了某班级门口，你打开门")
                            print("发现卫生角那边也有一个可疑的地方。")
                            print("这里也有一个传送门。")
                            print("不好！是传送到了僵尸的基地")
                            print("幸好，那边时间是凌晨1点，他们都还在睡觉。")
                            print("你正在找通往家里的传送门。")
                            print("一个巡逻的僵尸走过来了。")
                            print("你发现他的肚皮上有一个门的纹身。")
                            print("你不管三七二十一，直接冲了过去。")
                            print("没想到你穿透了他的【肚皮】到了家里。")
                            print("成功逃脱！")
                        elif c==2:
                            print("天色已晚，你准备睡觉")
                            print("(～﹃～)~zZ")
                            print("睡到半夜，你没想到头顶上有个TNT，你还没来得及逃脱，就被炸死了。")
                elif c==2:
                    print("没想到僵尸就在矿洞里吃喝玩乐，你躲过了他们。")
                    print("血量:80")
                    print("等他们走了，你开始采矿")
                    print("前面有一个箱子，你觉得好奇，打开了它。")
                    print("有一个超级强的僵尸把你内部掏空，吃掉了。(P·S:没想到他这么捞)")
                    print("血量:10")
                    print("最后你在挖矿的时候，体力不支，死了。")
            elif c==2:
                print("你出生在一个沙漠绿洲，旁边有电锯和斧头，捡哪个？")
                c=int(input("1.电锯 2.斧头 3.不捡"))
                d=int(input("要不要砍树？（1.砍 2.不砍）"))
                if d==1:
                    if c==1 or c==2:
                        print("你砍了许多树，建了房子和装备库")
                        print("你的房子：?")
                        print("你安心地过了一夜\n成功！")
                    elif c==3:
                        print("你正在徒手砍树，正好僵尸路过，把你给吃了。Y(x_x)Y")
                elif d==2:
                        print("你没有房子，僵尸找到了你，把你给吃了Y(x_x)Y")
        elif prog==8:
            print("不骗人（不信你去掉字符串颜色会不会变）");print("and exec not");
            print("""assert	finally	or
    break for pass
    class from print
    continue global	raise
    def	if return
    del	import try
    elif in	while
    else is	with
    except lambda yield""");print('''str bytes list 
    tuple set frozenset
    dict int float
    complex bool''');
        elif prog==9:
            print("正在测网速···");sleep(2);print("诊断结果:");
            print("上传速度:",uniform(0,11.8),"K/s 下载速度:",uniform(0,13.9),"K/s")
        elif prog==10:
            print("鲁大师|Pan管家");sleep(1.6);
            print("电池:",randint(80,100),"% CPU用量:",uniform(5.8,35.2),"% CPU温度:",randint(37,58),"℃")
        elif prog==11:
            print("灰太狼之死http://code.xueersi.com/home/project/detail?lang=code&pid=3189214&version=cpp&form=cpp\n大叶的心脏http://code.xueersi.com/home/project/detail?lang=code&pid=3196863&version=cpp&form=cpp\n逃脱森林http://code.xueersi.com/home/project/detail?lang=code&pid=3198218&version=cpp&form=cpp\n")
            print("糖果山杀人http://code.xueersi.com/home/project/detail?lang=code&pid=3206365&version=cpp&form=cpp\n皮卡丘失踪之谜http://code.xueersi.com/home/project/detail?lang=code&pid=3265638&version=cpp&form=cpp\n日常沙雕1_http://code.xueersi.com/home/project/detail?lang=code&pid=3325725&version=cpp&form=cpp")
        elif prog==12:
            print("三国杀八人国战\n一共有8人玩，你的武将是：主将曹操，副将乐进，国家是魏，技能有:护驾，奸雄，骁果。");sleep(1.5)
            print("开始了,你选了【桃园结义】【杀】【闪】【南蛮入侵】4张牌")
            sleep(1.2)
            print("五号位向你打出了一张【杀】（你是二号位），是否打出一张【闪】(y|n)")
            c=input()
            if c=="y":
                print("你打出了一张闪，成功避免了一滴血的失去（你一共有3滴血）")
                sleep(1.3)
            elif c=="n":
                print("你因为没有反抗，1滴血已经没了❣（一共有3滴）")
                sleep(1.4)
            c=input("是否打出【杀】，作为对五号位的回报(杀|南蛮)")
            if c=="杀":
                print("他打出了一张【闪】")
            elif c=="南蛮":
                print("除了一号位之外，所有人都打出了一张【杀】")
                sleep(1.6)
                c=input("一号位快GG了，是否打出一张【桃】给他补血(y|n)？")
                if c=="y":
                    print("你没有【桃】")
                elif c=="n":
                    print("\033[93m五谷丰登\033[0m等待选牌")
                    sleep(2)
                    print("你刚好摸出了一张【桃】，给一号位补血")
            sleep(1)
            c=input("是否发动“奸雄”技能，继续怼5号位？(y|n)")
            if c=="y":
                print("他已经被你给弄死了")
            elif c=="n":
                print("你被他打死了")
            sleep(3)
            print("过了一会儿，已经进入了鏖战模式，只有你和六号位在")
            sleep(2)
            c=input("你的武将形象盛气凌人，让他一看就发毛，是否打出一张【杀】给他最后一击(y|n)")
            if c=="y":
                print("他没有打出【桃】被你打死了。")
                sleep(0.8)
                print("恭喜你在本场获胜！")
            elif c=="n":
                print("你被他打死了")
                sleep(1.2)
                print("恭喜你在本场失败?！")
        elif prog==13:
            print("        欢迎来到Pan5G应用商城")
            print("如果下载速度太慢，可以先去鲁大师那里测一下网速")
            print("\033[92m1.百度")
            print("\033[96m2.抖音")
            print("\033[91m3.学而思网校")
            app=int(input())
            if app==1:
                dl1=1
            elif app==2:
                dl2=1
            if app==1 or 2:
                print("正在安装···")
                sleep(2)
                print("安装完毕！")
            elif dl1==1 or dl2==1 or app==3:
                print("已安装此程序！")
            else:
                print("程序不存在。")
        elif prog==14:
            print("     《什么都没打印就超长》")
            print("www=“”")
            print("while True:")
            print("   print(www)")
            print("     《你的电脑即将在30秒后爆炸?》")
            print('''from time import sleep
    from random import randint
    a = 30
    while a > 0:
        print("你的电脑将在", a ,"秒后爆炸?")
        a -= 1
        sleep(1)
    b = randint(0, 100000)
    print("启动中.....")
    sleep(3)
    s = []
    while True:
        s.append(b)
        b = randint(0, 100000)
        print(s)''')
        elif prog==15:
            print("剩余金币:",money)
            print("1.PanNT4的支持（150）2.临时VIP（90）3.PanTSE1的平板技术支持（50）4.Pan冬季礼包（250）")
            buy=int(input("请输入你想买的东西:"))
            if buy==1 and money>=150:
                print("恭喜获得：PanNT4的支持")
                money=money-150
            elif buy==2 and money>=90:
                print("恭喜获得：临時VIP(四级VIP)")
                money=money-90
            elif buy==3 and money>=50:
                print("恭喜获得：PanTSE1的平板技术支持")
                money=money-50
            elif buy==4 and money>=250:
                print("恭喜获得：Pan冬季礼包")
                money=money-250
            else:
                print("该商品不存在或没有金币购买。")
        elif prog==16:
            print("今日\033[33m1\033[33m讲课程")
            print("\033[0m2020-1-16 坑爹小游戏 \033[33m马锦羽")
            print("\033[31m直播进行中")
            cla=input("上课还是不上(y|n)")
            if cla=="y":
                print("1.o o o几个球")
                q=int(input("请输入答案:"))
                if q==7:
                    print("正确！奖励10金币！")
                    money=money+10
                else:
                    print("错误！答案是7")
                print("【详解】隐藏球球")
                print("3.1+2=___")
                q=int(input("1.4 2.1 3.8 4.2__"))
                if q==3:
                    print("正确！奖励10金币！")
                    money=money+10
                else:
                    print("错误！答案是3")
                print("2.不要点击对或错")
                sleep(2)
                print("（此题不发互动）【详解】什么都不写不就行了吗")
                print("4.皇帝今年几岁？")
                q=int(input("请输入答案:"))
                if q==10000:
                    print("正确！奖励10金币！")
                    money=money+10
                else:
                    print("错误！答案是10000")
                print("【详解】吾皇万岁！")
                q=input("5.你猜，世界上最富有的人是:")
                if q=="你":
                    print("正确！奖励10金币！")
                    money=money+10
                else:
                    print("错误！答案是“你”")
                print("【详解】你就是天选之子！")
            elif cla=="n":
                print("那白白了ヾ(•ω•`)o")
        elif prog==17:
            print("PanPy工作室招人，内容如下:")
            txt="【程序部】（选一完成）要求：会Scratch,Python,C++（重要）要求不高，但作品需要精致，不抄袭，不骗赞\n【文艺部】要求：精通Scratch，工作：进行录音/拍摄等一些工作\n【宣传部】选一作品或者工作室招人进行宣传，发送到学而思编程官网即可\n【后勤部】要求和程序部一样，修改程序部的bug即可。\nPS:无需QQ和微信，如果有英语不行的，关注微信公众号:Eng-Knows"
            print(txt)
            print("加入方式：在编程社区发“回复月高工作室邀请函”，待室长审核。")
            print("工作室网页：https://pi20308303.icoc.vc/")
        elif prog==18:
            conton=input("输入您对此产品的建议:")
            result=send_msg(18900263119,conton)
            if result=="成功":
                print("✔ 发送成功:HOTM会加急处理这条信息")
            else:
                print("❌  失败:系统繁忙，请稍后再尝试。")
        elif prog==19:
            print("\033[93m代码运行结束")
            sleep(6)
            print("\033[37m什么？你还没走？")
            print("那试试这样子吧")
            break
        elif prog==20:
            print('''  File "main.py", line 423
        print(
                ^
    SyntaxError: EOF while scanning triple-quoted string literal''')
        elif prog==21:
            print("\033[90m特级VIP 剩余0个名额")
            print("成为月高工作室高管和Pan系统管理员可以免费获得\n")
            print("\033[91m一级VIP 剩余2个名额")
            print("成为与月高工作室合作伙伴可以免费获得")
            print("1个月:20￥ 3个月:50￥ 6个月:100￥ 一年:250￥\n")
            print("\033[92m二级VIP 剩余9个名额")
            print("1个月:免费 3个月:35￥ 6个月:60￥ 一年:125￥\n")
            sleep(3)
            b("\033[0m支付方式\n微信:pjf420137013 QQ:420137013\n")
            input("Enter键继续")
        elif prog==22:
            print("\033[44m                                      ")
            print("\033[42m                                      ")
            print("\033[44m          \033[42m                            ")
            print("\033[44m          \033[42m                            ")
            print("\033[44m                                      ")
            print("\033[44m          \033[41m                   \033[44m         ")
            print("\033[43m                                      ")
            print("\033[0m\033[92m               Pan工作室")
        elif prog==23:
            print("女：烦 男：烦就和我聊天")
            sleep(1)
            print("女：滚 男：地不干净")
            sleep(1)
            print("女：找死 男：死在字典961页")
            sleep(1)
            print("女：晕 男：我有止晕药")
            sleep(1)
            print("女：我服了 男：服了药就不晕了")
            sleep(1)
            print("女：大哥 男：认你这个妹妹了")
            sleep(1)
            print("女：拜托 男：拜可以，不用脱")
            sleep(1)
            print("女：无语，脸已经绿了")
        elif prog==24:
            b("第一种\n \033[0m代码运行结束\n成功率:0.1%\n看颜色是黄还是白")
            sleep(2)
            b("第二种\n \033[33m代码运行结束\n成功率:25.3%\n颜色是暗的")
            sleep(2)
            b("第三种\n \033[93m代码运行结束\n成功率:91.8%\n眼力好才能看出来")
        elif prog==25:
            print("\033[3m斜体模式已打开！")
        elif prog==26:
            print("\033[4m下划线模式已打开！")
        elif prog==27:
            print("\033[0m已关闭所有特效！")
        elif prog==28:
            print("\033[32m护眼模式已打开！")
        elif prog==29 and dl1==1:
            print("\033[92m你可以这样说:")
            print("\033[94m一加一的所有答案 Pan工作室简介 Pan81百科 Pan81如何开启特效 Pan3.0升级不了")
            print("Pan2.0停止支持 PanNT4蓝屏钙事件 Pan3.0永远滴神 编程社区源代码 PanTSE1将采用软件图标技术")
            search=input("搜一搜新鲜事:")
            if search=="一加一的所有答案":
                b("1+1=1，2，3，5，7，10，11，41，王，L，厂，十，二")
            elif search=="Pan工作室简介":
                b("""Pan多语言工作室创建于2019年11月23日，主要产品有毁童年系列等。创建以来，公司以先进的生产设备，完善的售后服务，丰富的生产经验和优质的产品质量而一直受到客户信赖。本公司现有品牌《灰太狼之死》已经在广大客户心目中形成一种品牌效应，质量过关，令客户放心。
        瞻望未来，工作室将以更优质的产品和更完善的服务，力争成为学而思编程工作室行业中的优秀企业者而不断努力拼搏。""")
            elif b=="Pan81百科":
                print("Pan81是Pan工作室研发的较新款操作系统，于2020年1月发布，原名为Pan4.0(不是NT4)，是迄今为止功能多，又实用的操作系统（功能30+，代码500+）")
            elif search=="Pan81如何开启特效":
                b("在系统的桌面上25.26.28都是特效开启哦~")
            elif search=="Pan3.0升级不了":
                b("因为系统原因，暂时不能升级。")
            elif search=="Pan2.0停止支持":
                b("Pan2.0已于7月2日永久停止技术支持，现在在老系统名单的只有Pan3.0了，让我们为3.0继续活下去吧(详见\"Pan3.0永远滴神\")")
            elif search=="PanNT4蓝屏钙事件":
                b("2020年6月8日，某人曝出PanNT4和Pan5.1经常蓝屏，我们在测试版Pan4.0 Built 3857中测试了一下，未发现大bug，小bug已经解决。")
            elif search=="Pan98有专业版吗":
                b("Pan2020为月高工作室于2020年1月26日发布的操作系统，它运用全新的内核设计，使得运行正确率大大提高\nPan 2020 SP2版本已于2020年7月16日发布(同日SP1停止支持)，修复了更多bug\n目前，月高工作室已于2020年9月30日停止支持，Pan2020被列入\"C站最失败的系统\"之一。")
            elif search=="编程社区源代码":
                print('''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="keywords" content="&#x5B66;&#x800C;&#x601D;&#x7F51;&#x6821;,&#x5728;&#x7EBF;&#x5B66;&#x4E60;,&#x5728;&#x7EBF;&#x8F85;&#x5BFC;,&#x76F4;&#x64AD;&#x6388;&#x8BFE;,&#x4E2D;&#x5C0F;&#x5B66;&#x8F85;&#x5BFC;&#x8BFE;&#x7A0B;,&#x89C6;&#x9891;&#x8BFE;&#x7A0B;,&#x7F51;&#x7EDC;&#x8BFE;&#x7A0B;"><meta http-equiv="Cache-Control" content="no-cache"><meta name="description" content="&#x5B66;&#x800C;&#x601D;&#x7F51;&#x6821;&#x4E3A;3-18&#x5C81;&#x5B69;&#x5B50;&#x63D0;&#x4F9B;&#x5C0F;&#x5B66;&#x3001;&#x521D;&#x4E2D;&#x3001;&#x9AD8;&#x4E2D;&#x5168;&#x5B66;&#x79D1;&#x4E00;&#x7AD9;&#x5F0F;&#x8BFE;&#x5916;&#x6559;&#x5B66;&#x3002;&#x201C;&#x76F4;&#x64AD;+&#x8F85;&#x5BFC;&#x201D;&#x53CC;&#x5E08;&#x6559;&#x5B66;&#xFF0C;&#x5B9E;&#x73B0;&#x4E86;&#x76F4;&#x64AD;&#x4E0A;&#x8BFE;&#x3001;&#x5B9E;&#x65F6;&#x4E92;&#x52A8;&#x3001;&#x968F;&#x5802;&#x6D4B;&#x8BD5;&#x3001;&#x8BED;&#x97F3;&#x6D4B;&#x8BC4;&#x3001;&#x53CA;&#x65F6;&#x7B54;&#x7591;&#x3001;&#x4F5C;&#x4E1A;&#x4F5C;&#x6587;&#x6279;&#x6539;&#x3001;&#x9519;&#x9898;&#x8BA2;&#x6B63;&#xFF0C;&#x5927;&#x5E45;&#x5EA6;&#x63D0;&#x5347;&#x5B66;&#x4E60;&#x6548;&#x679C;&#x3002;&#x5168;&#x56FD;200&#x591A;&#x4E2A;&#x57CE;&#x5E02;&#xFF0C;&#x8D85;&#x8FC7;500&#x4E07;&#x4E2D;&#x5C0F;&#x5B66;&#x751F;&#x6B63;&#x5728;&#x5B66;&#x800C;&#x601D;&#x7F51;&#x6821;&#x9AD8;&#x6548;&#x5B66;&#x4E60;"><meta name="renderer" content="webkit"><link href="https://res11.xesimg.com/public/favicon.ico" rel="shortcut icon"><link rel="stylesheet" href="/static/sweetalert/sweetalert2.css?_v=1576741327278"><link rel="stylesheet" href="/static/css/loading.css?_v=1576741327278"><script src="//lib02.xesimg.com/lib/webLog/xes.weblog.common.min.js"></script><script src="//lib04.xesimg.com/lib/webLog/xes.weblog.resource.min.js"></script><script src="/static/python/skulpt.min.js?_v=1576741327278" type="text/javascript"></script><script src="/static/python/skulpt-stdlib.js?_v=1576741327278" type="text/javascript"></script><title>&#x5B66;&#x800C;&#x601D;&#x7F16;&#x7A0B; &#x5B66;&#x800C;&#x601D;&#x7F51;&#x6821;-&#x5728;&#x7EBF;&#x5B66;&#x4E60;&#x66F4;&#x6709;&#x6548;</title><style>/* * {
          font-family: MicrosoftYaHei;
        } */</style><script>var t = "2019-12-19 15:42:07"
        console.log('version RRRR= ', t)
    
        function load() {
          document.getElementById("loading-dom").style.display = "none"
          console.log('%c' + 'Everything is best (beast) arrangment!', 'color:red')
        }
        setTimeout(function () {
          document.getElementById("loading-dom").style.display = "none"
        }, 10000)</script><link href="/code/static/css/app.2a1be4c26e17c0eb209e03497331399a.css" rel="stylesheet"></head><body onload="load()"><div id="app"></div><div id="loading-dom" class="cpt-loading-mask animated fadeInNoTransform column" data-name="flash-loading" style="background: rgba(0, 0, 0, 0.2); z-index: 1000001; position: absolute;"><div class="div-loading" style="background: rgba(0, 0, 0, 0); width: 220px; height: 140px; border-radius: 12px;"><p class="loading-title txt-textOneRow" style="color: rgba(255, 255, 255, 0.7);"></p><div class="loading enjoy-code" style="width: 250px; height: 80px;"><div><div class="logo-loading"></div><div class="spinner"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div></div></div><p class="loading-discription txt-textOneRow" style="color: rgba(255, 255, 255, 0.7);"></p></div></div><script src="/static/jquery/jquery.min.js"></script><script src="//lib04.xesimg.com/lib/webLog/xes.weblog.event.min.js"></script><script src="/static/sweetalert/sweetalert2.js?_v=1576741327281"></script><script src="/static/clock/clock.js?_v=1576741327281"></script><script src="/static/qrcanvas/qrcanvas.min.js"></script><button id="log-button" style="display: none">&#x53D1;&#x9001;&#x65E5;&#x5FD7;</button> <img style="display: none;" id="qrlogo" src="/static/images/code-home/qrlogo.png"><script type="text/javascript" src="/code/static/js/manifest.6eff60e751a01626a2a3.js"></script><script type="text/javascript" src="/code/static/js/vendor.d1405083d4e32ef40721.js"></script><script type="text/javascript" src="/code/static/js/app.71481312f9ac6ae64353.js"></script><script type="text/javascript" src="/code/static/js/babel-polyfill.d47384217ee2b79035ce.js"></script></body>
            <script>
              var color = 'blue'
              console.log('%c' + '欢迎来到学而思编程', 'color:' + color)
              console.log('%c' + '我们用科技推动教育进步', 'color:' + color)
              console.log('%c' + '你提出问题我从容应对,不忘初心', 'color:' + color)
              console.log('%c' + '在这里我们全力以赴，不辱使命！', 'color:' + color)
            </script>
          </html>''')
            elif search=="Pan工作室与Microsoft工作室合并":
                b("这个说法不准确，Microsoft是要和Pan工作室联合开发新的操作系统《小曾系统2020 New Pan》。")
                sleep(1)
                b("该操作系统虽然还未上市，就有一张张渲染图曝光，经验证，属于谣言。")
            else:
                print("这个功能我不知道怎么回答你，我会继续学习的^_^")
        elif prog==30 and dl2==1:
            print("抖音热门音乐(2019年年度评选)")
            print('''1.沙漠骆驼
2.38度6
3.燃烧我的卡路里
4.去年夏天
5.年少有为
6.学猫叫
7.体面
8.再见只是陌生人
9.海草舞
10.小跳蛙
11.广东爱情故事
12.最美的期待
13.隔壁泰山
14.平凡之路
15.浪人琵琶
16.怀念青春
17.纸短情长
18.可不可以''')
        else:
            print("功能不存在或未安装此功能")
        sleep(7.5)
        system("clear")
        continue

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

def setup():
    global name
    global password
    global password_yz
    print("\033[44m")
    qing()
    print("Pan 2020 安装程序\n==================")
    print("选择要安装Pan 2020系统的磁盘")
    print("\n\n磁盘0:Virtual Disk(8192MB)\n\033[90;107mC:  FAT32              2048MB(1700MB可用)\033[44m")
    input("\033[97m\n\n\n当你选好分区时，请按Enter")
    qing()
    for i in range(0,100,15):
        print("Pan 2020 安装程序\n==================")
        print("请稍后，安装程序正在格式化C盘("+str(i)+"%已完成)")
        sleep(0.2)
        qing()
    print("Pan 2020 安装程序\n==================\n安装程序正在将文件复制到Pan 2020安装文件夹，这可能要花费1分钟左右的时间，请不要断开电源或关闭主机。\n复制文件...")
    print(r"C:\Program\Program.exe")
    sleep(0.2)
    chrome=0
    print(r"C:\Program\Store.bin")
    sleep(0.08)
    print(r"C:\Program\Start.dll")
    print(r"C:\Program\SetupFd.exe")
    sleep(3.15)
    print(r"C:\Program\HIMEM.sys")
    print(r"C:\Program\memory.sys")
    sleep(5.13)
    print(r"C:\Program\pages.sys")
    sleep(1.13)
    print(r"C:\local\Startup.exe")
    sleep(0.2)
    print(r"C:\local\Desktop.dll")
    print(r"C:\local\Start.dll")
    print(r"C:\local\Program.exe")
    sleep(3.13)
    print(r"C:\local\Shutdown.dll")
    print(r"C:\local\Pan2020.ini")
    print(r"C:\local\code.py")
    print(r"C:\local\csrss.exe")
    sleep(4.33)
    print(r"C:\local\check.asm")
    sleep(0.23)
    print(r"C:\local\disc.bin")
    sleep(1.37)
    qing()
    print("Pan 2020 安装程序\n==================")
    input("所有文件都已复制完成，按Enter键重新启动让新的设置生效。")
    print("\033[0m");qing();
    sleep(3)
    print('''\033[?25l       \033[94m______    \033[91m ______
        \033[94m|     \   \033[91m|     |    \033[93m|\   |
        \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
        \033[94m|         \033[91m|     |    \033[93m|  \ |
        \033[94m|         \033[91m|     |    \033[93m|   \|
''')
    print("\n\n\n\n\033[0m to interrupt normal startup,press Enter")
    sleep(0.2)
    system("clear")
    for i in range(3):
        print("_")
        sleep(0.5)
        qing()
        sleep(0.5)
    sleep(1)
    for i in range(5):
        for j in range(10):
            print("  "*j+"|||")
            print("©HOTM Workshop")
            sleep(0.1)
            qing()
        qing()
    print("\033[104m")
    qing()
    sleep(2)
    print("Pan 2020 安装程序\n==================")
    name=input("请输入你的姓名(如不填则默认为安装程序在复制文件时设置的临时账号):")
    if name==" "*len(name):
        name="Setup"
    while name=="Administrator" or name=="guest" or name=="SYSTEM":
        qing()
        name=input("用户已存在，请重新输入:")
    qing()
    print("Pan 2020 安装程序\n==================")
    key=["JCCXW-XTW33-YHPRB-WKXBX-V2JYB","JB8BP-QWD34-VXMHG-92FY3-HPQHM","JCBY9-PGHYF-CPYH8-TDC8B-GTPMB","KQF2H-284RW-GHXM6-Y3W2B-QWGBB","KQF2H-284RW-GHXM6-Y3W2B-QWGBB"]
    my_key=input("输入Pan产品密钥(5个字母，以一个横杠间隔，如KQF2H-284RW-GHXM6-Y3W2B-QWGBB，没有密钥可输入0跳过):")
    if 1:
        while not(my_key in key or int(my_key)==0):
            my_key=input("输入Pan产品密钥(5个字母，以一个横杠间隔，如KQF2H-284RW-GHXM6-Y3W2B-QWGBB，没有密钥可输入0跳过):")
    qing()
    print("Pan 2020 安装程序\n==================")
    password=input("请输入您的密码:")
    password_yz=None
    password_yz=input("请再次输入您的密码:")
    while password_yz!=password:
        password_yz=input("\033[91m密码错误，请输入您的密码:")
    qing()
    print("Pan 2020 安装程序\n==================")
    print("请稍后，Pan 2020正在安装系统组件和其他软件(需要30秒左右)...")
    sleep(randint(25,35))
    qing()
    print("Pan 2020 安装程序\n==================")
    input("恭喜！恭喜！Pan 2020已经成功地安装在了你的电脑上，按Enter键即可体验全新的Pan 2020。")

try:
    change_p81=0
    print("Startup Pan...")
    print("This computer was not shut down properly,try to recovery...")
    sleep(2)
    print("HIMEM is testing memory...done.")
    sleep(3)
    print("BIOS is checking system is checking disk...done.")
    print("Startup Pan...")
    sleep(0.2)
    qing()
    print("\033[?25l",end="")
    print('''\033[?25l       \033[94m______    \033[91m ______
        \033[94m|     \   \033[91m|     |    \033[93m|\   |
        \033[94m|_____/   \033[91m|_____|    \033[93m| \  |
        \033[94m|         \033[91m|     |    \033[93m|  \ |
        \033[94m|         \033[91m|     |    \033[93m|   \|
''')
    print("\n\n\n\n\033[0m to interrupt normal startup,press Enter")
    sleep(0.2)
    system("clear")
    su1=time()
    for i in range(3):
        print("_")
        sleep(0.5)
        qing()
        sleep(0.5)
    sleep(1)
    for i in range(5):
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
        print("\033[93m本次开机用了"+str(su2)+"秒，超越了全国99%的电脑，获得五星级神机称号")
    elif su2<=12:
        print("\033[93m本次开机用了"+str(su2)+"秒，超越了全国97%的电脑，可能是卡顿情况，此为正常现象")
    elif su2<=20:
        print("\033[93m本次开机用了"+str(su2)+"秒，超越了全国75%的电脑，速度比较慢啊")
    else:
        print("\033[93m本次开机用了"+str(su2)+"秒，超越了全国1%的电脑，你的电脑延迟非常严重，建议检查网络")
    sleep(3)
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
    sleep(2)
    qing()
    while 1:
        print("\033[0m",end="")
        date=int(strftime("%H",localtime()))
        print(strftime("%Y年%m月%d日\n%H:%M分",localtime()))
        if date<=7:
            date="晚上好"
        elif date<=11:
            date="上午好"
        elif date<=13:
            date="中午好"
        elif date<=17:
            date="下午好"
        elif date<=22:
            date="晚上好"
        else:
            date="夜深了"
        print(date+"，"+name)
        print("""1.开始菜单
2.计算器（平均数）
3.计算器
4.计算器（鸡兔同笼）
5.计算器（年龄）
6.更新
7.探索Pan 2020
8.切换系统版本
9.更改密码
10.待机
11.连接Wi-Fi
12.意见反馈
13.Google Chrome
14.高德地图""")
        prog=input("输入要打开的程序的序号:")
        qing()
        if prog=="1":
            while 1:
                print("开始                          "+name)
                print("\033[92m🔋 电源(x)   \033[94m💾 磁盘空间(e)     \033[93m📂 资源管理器(p)    \033[91m🛅 关于计算机(a) \033[95m💻  返回桌面(d)")
                prog=input("请输入字母代码:")
                qing()
                if prog=="x" or prog=="X":
                    b("\033[92m🔌 您的电脑是台式机，没有可用的电池。")
                    b("\033[94m📡 已通过以太网连接网络\"Pan-2020_WLAN\"")
                    b("\033[90m🔊 音量:0% 未安装声卡")
                    b("\033[95m📔 输入法:(中文简体)美式键盘")
                    prog=input("\033[90mE键关机，其他键退出")
                    if prog=="E" or prog=="e":
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
                elif prog=="d" or prog=="D":
                    break
                elif prog=="e" or prog=="E":
                    print("\033[0m💾  Pan(C:)                 💽 Data(D:)")
                    print("\033[44m   \033[40m               \033[0m"+10*" "+"\033[44m \033[40m                 ")
                    print("\033[0m1.66GB可用/2.00GB"+11*" "+"5.64GB可用/6.00GB")
                elif prog=="p" or prog=="P":
                    print("\033[0m💾  Pan(C:)                 💽 Data(D:)")
                    print("\033[44m   \033[40m               \033[0m"+10*" "+"\033[44m \033[40m                 ")
                    print("\033[0m1.66GB可用/2.00GB"+11*" "+"5.64GB可用/6.00GB")
                    S32=input("输入磁盘盘符(大写字母，不带冒号，如\"C\"):")
                    qing()
                    if S32=="C":
                        print("名称    类型           修改日期               大小")
                        print("Desktop 快捷方式(.lnk) 2020年1月23日 14:37    2KB")
                        print("Start   快捷方式(.lnk) 2020年6月14日 13:23    1KB")
                        print("Program 文件夹         2021年1月27日 17:10    119.9MB")
                        print("local   文件夹         2020年6月14日 13:25    118MB")
                        print(name+"   文件夹         2020年12月7日 17:54    100MB")
                        S32=input("输入文件或文件夹名(注意大小写,如\"Program\"):");qing();
                        if S32=="local":
                            print("名称    类型           修改日期                大小")
                            print("Startup 程序(.exe)     2020年1月23日  14:37    2MB")
                            print("Desktop 驱动(.dll)     2020年1月14日  13:23    1KB")
                            print("Start   驱动(.dll)     2020年1月14日  13:25    1KB")
                            print("Program 程序(.exe)     2020年1月13日  18:59    39MB")
                            print("Shutdown驱动(.dll)     2020年2月1日   13:11    1KB")
                            print("Pan2020 配置文件(.ini) 2020年1月23日  14:45    1KB")
                            print("code    直译式代码(.py)2020年1月26日  8:20     27KB")
                            print("csrss   核心程序(.exe) 2020年1月1日   7:26     54MB")
                            print("check   汇编代码(.asm) 2019年12月31日 23:30    3MB")
                            print("disc    未知文件(.bin) 2019年12月31日 22:19    17MB")
                        elif S32=="Program":
                            print("名称    类型           修改日期                大小")
                            print("Program 程序(.exe)     2020年1月23日  14:37    2MB")
                            print("Store   未知文件(.bin) 2020年1月14日  13:23    1MB")
                            print("Start   驱动(.dll)     2020年1月14日  13:25    1KB")
                            print("SetupFd 程序(.exe)     2020年1月13日  18:59    39MB")
                            print("HIMEM   配置文件(.sys) 2020年1月23日  18:59    1KB")
                            print("memory  配置文件(.sys) 2020年1月23日  19:36    64MB")
                            print("pages   配置文件(.sys) 2020年1月23日  19:38    14MB")
                        elif S32==name:
                            print("名称    类型           修改日期                大小")
                            print("Picture 图标(.ico)     2020年1月23日  14:37    36KB")
                            print("data    备份文件(.gho) 2020年1月14日  13:23    37MB")
                            print("user    驱动(.dll)     2020年1月14日  13:25    62MB")
                        else:
                            print("该文件不存在或不可预览")
                    elif S32=="D":
                        print("名称    类型           修改日期                大小")
                        print("chrome  文件夹         2020年1月23日  14:37    357MB")
                        print("Update  未知文件(.bin) 2020年1月14日  13:23    3MB")
                        print("Start   驱动(.dll)     2020年1月14日  13:25    1KB")
                        S32=input("输入文件或文件夹名(注意大小写,如\"chrome\"):")
                        if S32=="chrome":
                            print("名称    类型           修改日期                大小")
                            print("Mgr     文件夹         2020年1月23日  14:37    1KB")
                            print("chrome  未知文件(.bin) 2020年1月14日  13:23    354MB")
                            print("Search  脱机网页(.html)2020年1月14日  13:25    2MB")
                            print("Search  网页(.url)     2020年1月23日  0:21     1KB")
                        else:
                            print("该文件不存在或不可预览")
                elif prog=="a" or prog=="A":
                    b("\033[94m有关计算机的基本信息")
                    b("\033[0mPan版本")
                    b("Pan 2020 凉音美化版               \033[41m  \033[0m\033[42m  ")
                    b("\033[0m©2019 HOTM studio。保留所有权利。\033[44m  \033[0m\033[43m  ")
                    b("\033[0m系统")
                    b("已安装的内存(RAM):69MB(64MB可用)")
                    b("系统类型:64位操作系统，基于x64的处理器")
                    b("计算机名、域和工作组设置")
                    b("计算机全名:Pan 2020-PC")
                    b("计算机描述:jl19646425-1.icoc.vc")
                    b("工作组:HOTM")
                else:
                    print("该项目不存在")
        elif prog=="3":
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
                print("Error:invalid syntax")
        elif prog=="2":
            gs=int(input("有几个数"))
            pjs=0
            for i in range(gs):
                s=int(input("输入数字："))
                pjs=pjs+s
            pjs=pjs/gs
            print("平均数是:",pjs)
        elif prog=="4":
            feet=int(input("有几只脚"))
            chicken=feet-(head*2)
            rabbit=chicken/4
            chicken=head-rabbit
            print("鸡有",int(chicken),"只，兔有",int(rabbit),"只")
        elif prog=="5":
            new=int(input("输入已知年龄"))
            old=int(input("已知年龄到了这个年纪之后，老的多少岁？(已知年龄<未知年龄)"))
            print("老的年龄是",(old-new)/2,"岁")
        elif prog=="6":
            print("正在检查Pan版本...")
            sleep(1)
            print('正在检查python编译器版本...')
            sleep(2)
            print("正在检查系统位数和Linux内核版本...")
            sleep(5)
            qing()
            print("Pan版本:Pan 2020 Liangyin，最新！ python编译器版本:{} 您的系统:位数{} 系统内核:{}".format(version[0:5],platform.architecture()[0],platform.system()))
        elif prog=="7":
            print("\033[0m1.开机和登录 2.软件 3.浏览器问题 4.升级Pan 5.重装系统")
            rm=input()
            qing()
            if rm=="1":
                b("1)360报告卡顿现象\n清理电脑垃圾或重启机器即可，如问题严重，请换个浏览器(推荐Chrome)或重装系统(推荐win7，iPadOS)。\n2)基本信息可以不填么?\n可以，但是最好填(一旦填入姓名将不可更改)，姓名栏可以写您的真实名字，也可以写您的昵称。")
                b("\n3)用iPad能正常运行Pan2020吗?\n能，系统最好iPadOS13.0或Android 8.1以上，如果只想体验桌面系统，建议使用装有Windows 7及以上版本的电脑\n4)为什么我一启动机器就会报告蓝屏?\n可能是您在开机时输入了一些东西或者系统发生了一些小错误导致的，如果问题严重，可以降级到Pan 81")
                b("\n5)为什么我输入自己的密码提示错误?\n可能您拼写不正确或忘记(混淆)了密码，重启机器即可解决。")
            
            #elif rm=="2":
                #b("0功能，关闭机器\n1功能，休眠，您可以在这时候放松一下，放松完按Enter键重新进入开始菜单\n2功能，计算器，解决生活中的数学问题，如果您在做作业，不建议这样做。")
                #b("3功能，记事本，将一天要做的事记录下来，Pan会帮你存储到c盘中。\n4功能，重启，如果您的机器遇到问题可以打开此功能，如果是大问题，请按停止键再按运行键。\n5功能，系统属性，可以查看系统的基本信息。(也可以在命令提示符输入panver查看版本)\n")
                #b("6功能，MS-DOS，现在改名为CMD,用在一些专业的行业当中\n7功能，有道，可以轻松翻译英，韩，日，中四国语言\n8功能，地图，如果迷路了，可以通过它来找到回家的路(前提是你得有钱坐公交)\n")
                #b("9功能，浏览器，运行正式版会崩，所以这里统一用极速版了(酷喵的，已经授权了)\n10功能，计算机(我可不是2功能哦)，类似于PanNT4的\"我的电脑\"\n11功能就是我啦，可以给刚刚入坑的Pan小白一些帮助\n12功能，应用商店，可以购买应用或找回已卸载的原生应用")
            
            elif rm=="3":
                b("1)在浏览器运行过程中蓝屏了怎么办?\n进入2020的源码http://code.xueersi.com/ide/code/14344363找到【浏览器】的脚本，更改一下出错源码位置，或者重新按运行键\n")
                b("2)总是提醒该词条不存在是怎么肥事?\n检查拼写是否正确或者输入\"帮助\"看看浏览器里面都有什么词条。\n")
                b("3)超长了怎么办?\n重按运行键即可。\n4)为什么浏览器退不出来?\n等浏览器返回到主页，输入\"退出\"即可。")
            elif rm=="4":
                b("如果您的电脑运行的是已经停止支持的Pan2.0或者是即将停止支持的Pan3.0，我们建议您升级到Pan2020及以上版本，谢谢配合！")
            elif rm=="5":
                setup()
                print("\033[0m")
            else:
                print("该章节不存在")
        elif prog=="8":
            print("\033[44m");qing();
            print("我们在磁盘0(C: D: ESR:)上找到了2个系统，选择要切换的系统:")
            print("🍳  Pan 2020 凉音美化版(当前)")
            print("\033[7m💼  Pan 81专业版(针对老电脑的经典系统)\033[0;44m\n未选择按X退出")
            esr=input()
            if not(esr=="X" or esr=="x"):
                change_p81==1
                break
        elif prog=="9":
            password=input("输入新密码，不更改密码输入原密码:")
            while password!=password_yz:
                password_yz=input("请验证输入的新密码:")
            print("✔  修改成功！返回桌面将生效")
        elif prog=="10":
            print("\033[0m系统开始待机，回车键退出待机")
            sleep(0.1)
            qing()
            print("\033[0m开始待机，回车键退出")
            sleep(0.1)
            qing()
            print("\033[90m待机，回车键")
            sleep(0.1)
            qing()
            print("\033[30m机，回车")
            sleep(0.1)
            qing()
            print("\033[8m")
            sleep(0.1)
            qing()
            input()
            password=None
            while password!=password_yz:
                password=input("\033[0m你正在尝试重新登录，请输入"+name+"设置的密码:")
            print("\033[94mo 欢迎"+name)
        elif prog=="11":
            b("📡  已通过以太网连接:Pan 2020_Wlan")
            b("🌐  在方圆50米的范围内自动连接这个网络")
            b("⛔  管理员已禁用使用流量制度，断开网络将无法通过流量上网")
        elif prog=="12":
            corton=input("输入反馈内容:")
            send_msg(18006913260,corton)
            print("✔ 信息已发送到HOTM，HOTM会加急处理这条信息的。")
        elif prog=="13":
            if chrome==0:
                password=None
                while password!=password_yz:
                    password=input("输入你的密码以激活Chrome:")
                print("\033[91m激活成\033[92m功，欢\033[93m迎使用\033[94m!!!")
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
        elif prog=="14":
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
                print("\033[94m已连接Internet/以太网但还是未识别到？")
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
        print("\n10秒后返回桌面\033[000m")
        sleep(10)
        qing()
        continue
    if change_p81==1:
        p81()
except Exception as e:
    qing()
    error(str(e))
