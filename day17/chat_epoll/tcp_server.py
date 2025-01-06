# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

import socket
import select
import sys


def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 重用对应地址和端口
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    addr=('192.168.79.128',2000)
    s.bind(addr)  # 绑定，端口没有激活
    s.listen(128)  # listen时，端口才激活
    new_client,client_addr=s.accept()
    epoll=select.epoll()  # 创建一个epoll对象
    # 让epoll监控new_client sys.stdin
    epoll.register(new_client.fileno(),select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)

    while True:
        # 谁的缓冲区有数据，就填写到events
        events=epoll.poll(-1)
        for fd,event in events:
            if fd == new_client.fileno():
                data=new_client.recv(100)
                if data:
                    print("客户端："+data.decode('utf8'))
                else:
                    print("[客户端断开了...]")
                    return
            elif fd == sys.stdin.fileno():
                try:
                    data=input()  # 服务器端说话，发给对方
                except EOFError:  # 按control d后让服务器断开
                    print("[已下线...]")
                    return
                new_client.send(data.encode('utf8'))

    new_client.close()
    s.close()

if __name__ == '__main__':
    tcp_server()