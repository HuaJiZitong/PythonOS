import print
def power(inputpasswords):
    fo = open("password.txt","r+") 
    password = fo.read(4)
    print(password)
    strs = str(password)
    awa = len(strs)
    print(awa)
    if awa == 4:
        if inputpasswords == password:
            print.out("本次启动时长1秒")
            return
    else:
        print.out("第一次启动，设置新用户")
        fo.write(inputpasswords)
        print.out("密码设置成功")
        return
