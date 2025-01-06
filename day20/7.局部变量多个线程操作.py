# Author: 王璐
# Date: 2025/1/5
# Time: 11:28

import time
from threading import Thread

def work1(nums):
    nums.append(44)
    print("----in work1----",nums)

def work2(nums):
    time.sleep(1)  # 延时一会，保证t1线程中的事情做完
    print("----in wrok2----",nums)

def main():
    g_nums=[11,22,33]
    t1=Thread(target=work1,args=(g_nums,))
    t1.start()

    t2=Thread(target=work2,args=(g_nums,))
    t2.start()

if __name__ == '__main__':
    main()
