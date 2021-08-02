print("今日\033[33m1\033[33m讲课程")
if 1:
    if 1:
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