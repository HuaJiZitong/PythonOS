print("\033[0mVirtualDisk(11.6GB)")
if 1:
    if 1:
        if 1:
            print("\033[90mSystem(C: 8.00GB) \033[94m备份GHOST(X: "+str(e)+"GB) 未分配("+str(wfp)+"GB)  \033[90mEFI恢复分区(ESP: 0.1GB)")
            disk=input("\033[0m选择要更改的分区(填写盘符，没有盘符填名称，如E:)")
            qing()
            if disk=="C:" :
                print("A.属性 B.重新格式化")
                disk=input()
                qing()
                if disk=="A":
                    b("System(C:)")
                    b("类型:本地磁盘 文件系统:NTFS")
                    b("可用空间:6.18GB 总空间:8.00GB")
                elif disk=="B":
                    disk=input("你确定要格式化吗(Y|N)?")
                    qing()
                    if disk=="Y":
                        print("正在格式化...")
                        sleep(3)
                        print("格式化成功，重启生效")
                        sleep(2)
                        print("检测到C盘内无系统，自动切换到安装系统模式")
                        sleep(0.01)
                        setup()
                    else:
                        print("好的，您取消了格式化")
                else:
                    print("该操作无效。")
            elif disk=="ESP:":
                print("A.查看文件 B.属性")
                disk=input()
                qing()
                if disk=="A":
                    print("名称    类型             修改日期               大小")
                    print("BIOS    固件(.bin)       2020年6月14日 13:23    128KB")
                    print("config  数据(.dat)       2020年7月6日 15:42     105KB")
                elif disk=="B":
                    b("EFI恢复分区(ESP:)")
                    b("类型:本地磁盘 文件系统:FAT32")
                    b("可用空间:99.77MB")
                    b("总空间:100MB")
                else:
                    print("该操作无效。")
            elif disk=="X:":
                disk=input("A.压缩卷 B.属性 C.扩展卷\n")
                print("\033[41m")
                qing()
                if disk=="A":
                    print("欢迎使用压缩卷功能\n本功能会帮助你压缩X盘，节约出一个空闲空间")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用压缩卷\n本功能会帮助你压缩X盘，节约出一个空闲空间")
                    print("可压缩:"+str(e-0.25)+"GB\n\033[90mTIP:必须要预留0.25GB空间供磁盘有能力完成基本任务")
                    disk=input("\033[94m输入要压缩的空间:")
                    qing()
                    if float(disk)>e-0.25:
                        print("压缩后的空间太小！请重新选择！")
                    else:
                        print("正在压缩...")
                        wfp=wfp+float(disk)
                        e=e-float(disk)
                        sleep(2)
                        print("压缩成功！X盘剩余空间为"+str(e)+"GB!")
                elif disk=="B":
                    print("备份GHOST(X:)")
                    print("\033[94m可用空间:"+str(e-0.1)+"GB")
                    print("已用空间:0.1GB")
                    print("总容量:"+str(e)+"GB")
                elif disk=="C":
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大X盘")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用扩展卷功能\n本功能会帮助你扩大X盘")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！X盘剩余空间为"+str(e)+"GB!")
                else:
                    print("该操作无效。")
            elif disk=="未分配":
                disk=input("A.属性 B.与X盘合并")
                if disk=="A":
                    print("未分配")
                    print("\033[92m已准备就绪！等待分配分区中")
                    print("\033[0m总容量:"+str(wfp)+"GB")
                elif disk=="B":
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与X盘合并")
                    print("正在查询可用空间...")
                    sleep(3)
                    qing()
                    print("欢迎使用合并功能\n本功能会帮助你将未分配与X盘合并")
                    print("可扩展:"+str(wfp)+"GB\n")
                    disk=input("\033[94m输入要扩展的空间:")
                    qing()
                    if float(disk)>wfp:
                        print("要扩展的空间太大！无法扩容！")
                    else:
                        print("正在扩展...")
                        wfp=wfp-float(disk)
                        e=e+float(disk)
                        sleep(2)
                        print("扩展成功！X盘剩余空间为"+str(e)+"GB!")
            else:
                print("该磁盘不存在")