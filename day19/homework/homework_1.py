# Author: 王璐
# Date: 2025/1/4
# Time: 20:59

# 1、创建子进程（子进程 while True），通过 ps 查看是否有两个进程，同时通过 top 查看两个进程的 CPU 占有率，然后通过 kill 杀掉其中一个进程
from multiprocessing import Process

def proc():
    while True:
        pass

if __name__ == '__main__':
    p=Process(target=proc)
    p.start()