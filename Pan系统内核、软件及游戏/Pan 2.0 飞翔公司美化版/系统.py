from time import *
from xes.ext import *
from random import *
from os import *
def b(poem):
    for char in poem:
        sleep(0.1)
        print(char, end='', flush=True)
    print()

print("\033[?25l")
print("HIHEM is testing system disk...done")
system("clear")
print("\033[30m|||")
print("©HOTM workshop")
sleep(0.1)
system("clear")
print("\033[90m|||")
print("©HOTM workshop")
sleep(0.1)
system("clear")
for i in range(randint(2,6)):
    print("\033[0m",end="")
    for j in range(0,5,1):
        print("    "*j+"|||")
        print("©HOTM workshop")
        sleep(0.13)
        system("clear")
sleep(2)
pw=input("你好！请设置你的密码:")
system("clear")
print("o 欢迎")
hy=0
pjs=0
s=0
system("clear")
while 1:
    print("\033[0m------------PAN PRO 3---------------")   
    print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
    print('''0.关机
1.设置
2.计算器
3.平均数计算器
5.鸡兔同笼计算器
6.年龄计算器
7.记事本
9.小游戏
10.更新
11.信息
12.成绩预测
13.你的身材标准吗？''')
    prog=input("输入应用序号:")
    system("clear")
    if prog=="1":
        print("\033[92m💻 系统  \033[92m🔊 声音  📅 日期和时间")
        control=input("输入要更改的项目名称:")
        system("clear")
        if control=="系统":
            b("\033[94m有关计算机的基本信息")
            b("\033[0mPan版本")
            b("Pan 3.0 企业专业版               \033[41m  \033[0m\033[42m  ")
            b("\033[0m©2019 HOTM studio。保留所有权利。\033[44m  \033[0m\033[43m  ")
            b("\033[0m系统")
            b("已安装的内存(RAM):260MB(256MB可用)")
            b("系统类型:64位操作系统，基于x64的处理器")
            b("计算机名、域和工作组设置")
            b("计算机全名:Pan 3.0-PC")
            b("计算机描述:A Virtual PC in Xueersi coding(not in another OS)")
            b("工作组:HOTM")
        elif control=="声音":
            b("baba.mp3\ntry again.mp3\nlala.mp3\nlulu.mp3\noh no.mp3\ngoodbye.mp3")
            v=input("输入声音名称(如:baba.mp3):")
            play_mp3(v)
        elif control=="日期和时间":
            for i in range(10):
                print(ctime())
                sleep(1)
                system("clear")
        else:
            print("该功能不存在")
    elif prog=="2":
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
    elif prog=="3":
        gs=int(input("有几个数"))
        pjs=0
        for j in range(0,gs):
            s=int(input("输入数字："))
            pjs=pjs+s
        print("平均数是:",pjs/gs)
    elif prog=="5":
        head=int(input("有几个头"))
        feet=int(input("有几只脚"))
        chicken=feet-(head*2)
        rabbit=chicken/4
        chicken=head-rabbit
        print("鸡有",int(chicken),"只，兔有",int(rabbit),"只")
    elif prog=="6":
        new=int(input("输入已知年龄"))
        old=int(input("已知年龄到了这个年纪之后，老的多少岁？(已知年龄<未知年龄)"))
        print("老的年龄是",(old-new)/2,"岁")
    elif prog=="7":
        ch=input("输入文本，输好了按回车\n")
        print("您输入的是不是:",ch)
    elif prog=="9":
        for i in range(1,16):
            num=random.randint(0,10)
            score=0
            print("😜"+" "*num+"\(·□·)\ ")
            sum1=int(input("输入目测距离(误差不超过1个空格):"))
            if sum1==num or sum1==num-1 or sum1==num+1:
                print("吃到emoji小人，加两分！")
                score=score+2
            else:
                print("粉身碎骨，扣一分！")
                score=score-1
            print("你的得分为：",score)
    elif prog=="10":
        print("检测中······")
        sleep(1)
        print("❌  尽管有新更新存在，但由于您的Pan版本较低，将不会收到任何更新。")
    elif prog=="11":
        phone = input("\033[32m请输入手机号码[真的可以发到手机里，建议不要输入陌生号码]:")
        if len(phone)<5:
            system("clear")
            print("请输入正确的手机号码!")
            sleep(1)
            system("clear")
        conten = input("请输入发送内容[Enter发送]:")
        send_msg(int(phone),conten)
        print("发送成功\033[42m ✔ \033[0m")
    elif prog=="12":
        print("预计你某科的成绩为",randint(45,100),"分")
    elif prog=="13":
        cm=int(input("输入你的身高（单位：厘米）"))
        kg=int(input("输入你的体重（单位：千克）"))
        std=(cm-100)*0.9
        if kg>std*1.1:
            print("你偏胖")
        elif kg<std*0.9:
            print("你偏瘦")
        else:
            print("你的身材很标准?！")
    elif prog=="16":
        print("\033[93m代码运行结束")
        sleep(3*2)
        print("\033[37m什么？你还没走？")
        print("那试试这样子吧")
        break
    elif prog=="0":
        print("正在关机······")
        sleep(2)
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
            elif prog=="13" and ds_1==0:
                YUAN = "您还没有安装此软件"
            else:
                YUAN = "您输入了程序名,请输入编号~"
        system("clear")
        print()
        print()
        print("\033[33m系统未查找到软件 - {} -".format(prog))
        print("\033[36m原因:{}".format(YUAN))
        sleep(0.5)
        input("\033[32mEnter键返回开始菜单。")
        system("clear")
        continue
    sleep(6.5)
    system("clear")
    continue
    