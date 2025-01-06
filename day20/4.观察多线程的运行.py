# Author: 王璐
# Date: 2025/1/5
# Time: 11:04
import time
from threading import Thread
from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)

if __name__ == '__main__':
    print('---开始---：%s' % ctime())

    t1=Thread(target=sing) # 创建sing的子进程
    t2=Thread(target=dance) # 创建dance子进程

    t1.start()
    t2.start()

    # sleep(5)
    print('---结束---：%s' % ctime())