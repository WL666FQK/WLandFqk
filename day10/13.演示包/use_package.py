# Author: 王璐
# Date: 2024/10/17

import  wd_message # 导包
import pygame

def use_package():
    wd_message.send_message.send()

    txt=wd_message.recv_message.receive()
    print(txt)

if __name__ == '__main__':
    use_package()