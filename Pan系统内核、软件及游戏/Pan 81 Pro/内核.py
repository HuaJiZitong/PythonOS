from random import*
from time import*
from os import*
from xes.ext import*
import urllib.request
import re 

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
6.鲁大师
7.意见反馈
8.开启斜体特效
9.开启下划线特效
10.关闭特效
11.护眼模式''')
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
        print("鲁大师|Pan管家");sleep(1.6);
        print("电池:",randint(80,100),"% CPU用量:",uniform(5.8,35.2),"% CPU温度:",randint(37,58),"℃")
    elif prog==7:
        conton=input("输入您对此产品的建议:")
        result=send_msg(18900263119,conton)
        if result=="成功":
            print("✔ 发送成功:HOTM会加急处理这条信息")
        else:
            print("❌  失败:系统繁忙，请稍后再尝试。")
    elif prog==8:
        print("\033[3m斜体模式已打开！")
    elif prog==9:
        print("\033[4m下划线模式已打开！")
    elif prog==10:
        print("\033[0m已关闭所有特效！")
    elif prog==11:
        print("\033[32m护眼模式已打开！")
    else:
        print("功能不存在")
    sleep(7.5)
    system("clear")
    continue
