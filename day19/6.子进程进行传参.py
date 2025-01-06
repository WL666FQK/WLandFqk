# Author: 王璐
# Date: 2025/1/4
# Time: 15:54

import os
import time
from multiprocessing import Process

def run_proc(name,age,**kwargs):
    for i in range(10):
        print('子进程{} {} ,{}'.format(name,age,kwargs))
        time.sleep(0.2)

if __name__ == '__main__':
    p=Process(target=run_proc,args=('xiongda',5),kwargs={'408':120})
    p.start()
    time.sleep(1)
    p.terminate() # 给子进程发信号杀掉他
    p.join()  # 一直等子进程，子进程结束，资源会被回收
    print('我是父进程')
