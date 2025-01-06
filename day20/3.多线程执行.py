# Author: 王璐
# Date: 2025/1/5
# Time: 10:56
import time
from threading import Thread

def saySorry():
    print("亲爱的，我错了")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t=Thread(target=saySorry)
        t.start()