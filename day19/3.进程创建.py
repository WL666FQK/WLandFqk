# Author: 王璐
# Date: 2025/1/4
# Time: 14:13

from multiprocessing import Process
import time

# 子进程的代码
def run_proc():
    while True:
        print('---2---')
        time.sleep(1)

if __name__ == '__main__':
    p=Process(target=run_proc)  # run_proc传递时不可以加括号
    p.start()
    while True:
        print('---1---')
        time.sleep(1)