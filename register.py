import module
def power(inputpasswords):
    with open('password.json', 'r') as f:
    password = json.load(f)
    awa = len(str(password))
    if awa == 4:
        if inputpasswords == password:
            module.out("本次启动时长1秒")
            return
    else:
        module.out("第一次启动，设置新用户")
        with open('password.json', 'w') as f:
            json.dump(password, f)
        module.out("密码设置成功")
        return
