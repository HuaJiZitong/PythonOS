if 1:
    if 1:
        if 1:
            if 1:
                print("9*9扫雷")
                checkerboard = [0,"01","02","03","04","05","06","07","08","09"]
                for i in range(10,82) :
                    checkerboard += [str(i)]
                mode = input("1.入门(6个雷) 2.简单(8个雷) 3.普通(10个雷) 4.困难(12个雷) 5.超难(15个雷) 6.自定义(1~80个雷)")
                set_comp = False
                isyou = True
                set_zone = 0
                set_mine = 0
                game_res = 0
                dig = [True] + ([False] * 81)
                game_checkwin = 0
                def showcheckerboard() :
                    system("clear")
                    for i in range(9) :
                        for i2 in range(1,9) :
                            if "\033[3" in checkerboard[i*9+i2] :
                                print(checkerboard[i*9+i2],end="\033[0m ")
                            else :
                                print(checkerboard[i*9+i2],end=" ")
                        if "\033[3" in checkerboard[i*9+i2] :
                            print(checkerboard[i*9+9] + "\033[0m")
                        else :
                            print(checkerboard[i*9+9])
                def do_dig(zone) :
                    global game_res
                    global mine
                    if mine[zone] == 1 :
                        print("你挖到雷了!")
                        print("游戏结束")
                        game_res = 2
                    else :
                        global dig
                        global checkerboard
                        global isyou
                        dig[zone] = True
                        if zone == 1 :
                            if checkerboard[1] == "01" :
                                if mine[2] + mine[10] + mine[11] == 0 :
                                    checkerboard[1] = "  "
                                    isyou = False
                                    do_dig(2)
                                    do_dig(10)
                                    do_dig(11)
                                else :
                                    checkerboard[1] = "\033[34mM" + str(mine[2] + mine[10] + mine[11])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 9 :
                            if checkerboard[9] == "09" :
                                if mine[8] + mine[17] + mine[18] == 0 :
                                    checkerboard[9] = "  "
                                    isyou = False
                                    do_dig(8)
                                    do_dig(17)
                                    do_dig(18)
                                else :
                                    checkerboard[9] = "\033[34mM" + str(mine[8] + mine[17] + mine[18])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 73 :
                            if checkerboard[73] == "73" :
                                if mine[64] + mine[65] + mine[74] == 0 :
                                    checkerboard[73] = "  "
                                    isyou = False
                                    do_dig(64)
                                    do_dig(65)
                                    do_dig(74)
                                else :
                                    checkerboard[73] = "\033[34mM" + str(mine[64] + mine[65] + mine[74])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone == 81 :
                            if checkerboard[81] == "81" :
                                if mine[71] + mine[72] + mine[80] == 0 :
                                    checkerboard[81] = "  "
                                    isyou = False
                                    do_dig(71)
                                    do_dig(72)
                                    do_dig(80)
                                else :
                                    checkerboard[81] = "\033[34mM" + str(mine[71] + mine[72] + mine[80])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [2,3,4,5,6,7,8] :
                            if checkerboard[zone] == ("0" + str(zone)) :
                                if mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [10,19,28,37,46,55,64] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 9] + mine[zone - 8] + mine[zone + 1] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone + 1)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 9] + mine[zone - 8] + mine[zone + 1] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [74,75,76,77,78,79,80] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        elif zone in [18,27,36,45,54,63,72] :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 1] + mine[zone + 8] + mine[zone + 9] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 1] + mine[zone + 8] + mine[zone + 9])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        else :
                            if checkerboard[zone] == str(zone) :
                                if mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10] == 0 :
                                    checkerboard[zone] = "  "
                                    isyou = False
                                    do_dig(zone - 10)
                                    do_dig(zone - 9)
                                    do_dig(zone - 8)
                                    do_dig(zone - 1)
                                    do_dig(zone + 1)
                                    do_dig(zone + 8)
                                    do_dig(zone + 9)
                                    do_dig(zone + 10)
                                else :
                                    checkerboard[zone] = "\033[34mM" + str(mine[zone - 10] + mine[zone - 9] + mine[zone - 8] + mine[zone - 1] + mine[zone + 1] + mine[zone + 8] + mine[zone + 9] + mine[zone + 10])
                            else :
                                if isyou :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                    if game_res == 0 :
                        game_checkwin = 0
                        for i in range(1,82) :
                            if dig[i] != mine[i] :
                                game_checkwin = game_checkwin + 1
                        if game_checkwin == 81 :
                            showcheckerboard()
                            print("胜利!")
                            print("游戏结束")
                            game_res = 1
                if mode == "1" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 6 :
                            if randint(1,81) <= 6 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 6 :
                            set_comp = True
                elif mode == "2" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 8 :
                            if randint(1,81) <= 8 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 8 :
                            set_comp = True
                elif mode == "3" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 10 :
                            if randint(1,81) <= 10 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 10 :
                            set_comp = True
                elif mode == "4" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 12 :
                            if randint(1,81) <= 12 :
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 12 :
                            set_comp = True
                elif mode == "5" :
                    while set_comp == False :
                        set_zone = 0
                        set_mine = 0
                        mine = [0] * 82
                        while set_zone < 81 and set_mine < 15 :
                            if randint(1,81) <= 15:
                                mine[set_zone + 1] = 1
                                set_mine = set_mine + 1
                            set_zone = set_zone + 1
                        if set_mine == 15 :
                            set_comp = True
                else :
                    mine2 = input("输入雷数(1~80)")
                    try :
                        int(float(mine2))
                    except :
                        print("错误:非整数")
                    else :
                        mine2 = int(float(mine2))
                        if mine2 > 80 :
                            print("错误:雷数太高(最高为80)")
                        elif mine2 < 1 :
                            print("错误:雷数太低(最低为1)")
                        else :
                            while set_comp == False :
                                set_zone = 0
                                set_mine = 0
                                mine = [0] * 82
                                while set_zone < 81 and set_mine < mine2 :
                                    if randint(1,81) <= mine2 :
                                        mine[set_zone + 1] = 1
                                        set_mine = set_mine + 1
                                    set_zone = set_zone + 1
                                if set_mine == mine2 :
                                    set_comp = True
                while game_res == 0 :
                    showcheckerboard()
                    isyou = True
                    game_setzone = input("\033[0m请输入操作格(01~81)")
                    try :
                        int(float(game_setzone))
                    except :
                        print("请输入正确的数字!")
                        sleep(0.5)
                    else :
                        if int(game_setzone) in list(range(1,82)) :
                            game_zonectrl = input("请选择操作 1.挖土 2.标旗/取消标旗 3.重选操作格")
                            if game_zonectrl == "1" :
                                game_setzone = int(float(game_setzone))
                                do_dig(game_setzone)
                            elif game_zonectrl == "2" :
                                if checkerboard[int(game_setzone)] == game_setzone :
                                    checkerboard[int(game_setzone)] = "\033[31m" + game_setzone
                                elif checkerboard[int(game_setzone)] == "\033[31m" + game_setzone :
                                    checkerboard[int(game_setzone)] = game_setzone
                                else :
                                    print("此处已经挖过!")
                                    sleep(0.5)
                        else :
                            print("请输入正确的数字!")
                            sleep(0.5)