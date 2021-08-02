import requests
import turtle
import pickle


#开始进入Python的世界
print('Api：1.墨天逸 2.韩小韩 3.樱花 4.小歪')
api = int(input('请输入API的数字来选择图片来源'))
ps = int(input('请输入图片数量'))
if (api == 1):
    print('墨天逸Api')
    for __count in range(ps):
        response = requests.get('http://api.mtyqx.cn/api/random.php')
        file = open('网站.txt', mode='a')
        file.write(('\n' + str(response.url)))
        file.close()
if (api == 2):
    print('韩小韩Api')
    for __count in range(ps):
        response = requests.get('https://api.vvhan.com/api/acgimg')
        file = open('网站.txt', mode='a')
        file.write(('\n' + str(response.url)))
        file.close()
if (api == 3):
    print('樱花Api')
    for __count in range(ps):
        response = requests.get('https://www.dmoe.cc/random.php')
        file = open('网站.txt', mode='a')
        file.write(('\n' + str(response.url)))
        file.close()
if (api == 4):
    print('小歪Api')
    for __count in range(ps):
        response = requests.get('https://api.ixiaowai.cn/api/api.php')
        file = open('网站.txt', mode='a')
        file.write(('\n' + str(response.url)))
        file.close()
