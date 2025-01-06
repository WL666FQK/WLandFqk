# Author: 王璐
# Date: 2025/1/5
# Time: 11:15

import time
from threading import Thread

g_num=100

def work1():
    global g_num
    for i in range(3):
        g_num+=1

    print("----in work1,g_num is %d----" % g_num)

def work2():
    global g_num
    print("----in wrok2,g_num is %d----" % g_num)

if __name__ == '__main__':
    t1=Thread(target=work1)
    t1.start()
    time.sleep(1)
    t2=Thread(target=work2)
    t2.start()
