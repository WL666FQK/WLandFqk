# Author: 王璐
# Date: 2025/1/4
# Time: 21:23

# 3、给子进程传参，查看子进程修改了传递的列表中的值以后，父进程中是否会变化，子进程修改全局变量，父进程join子进程后，打印全局变量是否变化

from multiprocessing import Process

age=18

def proc(list):
    print(list)
    list.append(33)
    print(list)
    age=20
    print(age)


if __name__ == '__main__':
    list=[11,22]
    p=Process(target=proc,args=(list,))
    p.start()
    p.join()
    print("---------------")
    print(list)  # 不跟着子进程改变
    print(age)  # 不跟着子进程改变
