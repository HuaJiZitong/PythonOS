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
    print("\033[90m提示：您已绕过学生模式！")
    print("\033[0m------------PAN XP 98---------------")   
    print(strftime("%Y-%m-%d %H:%M:%S",localtime()))
    print('''0.关机
1.设置
2.便签
3.更新
4.信息
5.加入工作室
6.护眼模式
7.你的身材标准吗？
8.待机'')
    prog=input("输入应用序号:")
    system("clear")
    if prog=="1":
        print("\033[92m💻 系统  \033[92m🔊 声音  📅 日期和时间")
        control=input("输入要更改的项目名称:")
        system("clear")
        if control=="系统":
            b("\033[94m有关计算机的基本信息")
            b("\033[0mPan版本")
            b("Pan 98 教育版               \033[41m  \033[0m\033[42m  ")
            b("\033[0m©2019 HOTM studio。保留所有权利。\033[44m  \033[0m\033[43m  ")
            b("评估模式，过期时间2021/8/16")
            b("\033[0m系统")
            b("已安装的内存(RAM):260MB(256MB可用)")
            b("系统类型:64位操作系统，基于x64的处理器")
            b("计算机名、域和工作组设置")
            b("计算机全名:Pan 98-PC")
            b("计算机描述:Lite")
            b("工作组:SCHOOL")
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
        ch=input("输入文本，输好了按回车\n")
        print("您输入的是不是:",ch)
    elif prog=="3":
        print("检测中······")
        sleep(1)
        print("🙂  您的Pan版本已是最新，Pan建议您开启学生模式以保证您的学习机的安全")
    elif prog=="4":
        phone = input("\033[32m请输入手机号码[真的可以发到手机里，建议不要输入陌生号码]:")
        if len(phone)<5:
            system("clear")
            print("请输入正确的手机号码!")
            sleep(1)
            system("clear")
        conten = input("请输入发送内容[Enter发送]:")
        send_msg(int(phone),conten)
        print("发送成功\033[42m ✔ \033[0m")
    elif prog=="5":
        print("""【程序部】（选一完成）要求：会Scratch,Python,C++（重要）要求不高，但作品需要精致，不抄袭，不骗赞
【文艺部】要求：精通Scratch，工作：进行录音/拍摄等一些工作
【宣传部】选一作品或者工作室招人进行宣传，发送到学而思编程官网即可
【后勤部】要求和程序部一样，修改程序部的bug即可。
PS:有意者请加QQ:420137013 如果有英语不行的，关注微信公众号:Eng-Knows""")
    elif prog=="6":
        if hy==0:
            print("\033[32m护眼模式已打开！")
            hy=1
        else:
            print("\033[37m护眼模式已关闭！")
            hy=0
    elif prog=="7":
        cm=int(input("输入你的身高（单位：厘米）"))
        kg=int(input("输入你的体重（单位：千克）"))
        std=(cm-100)*0.9
        if kg>std*1.1:
            print("你偏胖")
        elif kg<std*0.9:
            print("你偏瘦")
        else:
            print("你的身材很标准?！")
    elif prog=="8":
        sl=int(input("输入待机秒数，不超过2.5分钟"))
        if sl<=150:
            for i in range(0,sl):
                print(sl)
                sl=sl-1
                sleep(1)
        
        else:
            print("时间超限！")
        while inp != pw:
            print("忘记密码服务：你的密码是",pw)
            sleep(3)
            system("clear")
            inp=input("请输入密码：")
        print("O欢迎！")
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
    