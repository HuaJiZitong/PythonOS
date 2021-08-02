print("\033[44m")
    if 1:
        if 1:
            if 1:
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
                        print("?  Your PC is out of support")
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