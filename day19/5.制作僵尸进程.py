# Author: 王璐
# Date: 2025/1/4
# Time: 14:57

import os
import time
from multiprocessing import Process

def run_proc():
    print('我是子进程 pid={},ppid={}'.format(os.getpid(),os.getppid()))
    print('子进程结束')

if __name__ == '__main__':
    child=Process(target=run_proc)  # target代表子进程启动时，运行那个函数
    child.start()
    print('我是父进程 pid={},ppid={}'.format(os.getpid(),os.getppid()))
    # while True:
    #     time.sleep(1)