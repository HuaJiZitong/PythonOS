#book列表存储数据
book = {"少年读史记":"50元","流浪地球":"14.20元","侦探与小偷":"12.20元","舒克贝塔传":"100元","少年读徐霞客游记":"50元","小英雄雨来":"13.10元","孩子读得懂的山海经":"93.90元","滑稽修炼手册":"50元"}
#循环遍历 book 列表的键并输出
for i in book.keys():
    print(i)
while True:
    act = input("请问有什么需要帮助的吗？1-查询价格；2-修改价格")
    if act == "1":
        #变量name中存放的是书籍名称，是字典的键。
        name = input("输入书籍名称：")
        #作答区域。补充完整第27行代码，查询输入的书籍的价格。
        print(name+"的价钱为："+book[name])
    elif act == '2':
        name = input("请输入修改价格的书籍名称：")
        price = input("请输入价格：")
        book[name] = price
        print(book)
        
    else:
        break