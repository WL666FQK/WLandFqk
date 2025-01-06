# Author: 王璐
# Date: 2025/1/5
# Time: 11:01

from time import sleep

def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)

if __name__ == '__main__':
    sing()
    dance()