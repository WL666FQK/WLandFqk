# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

import socket
import select
import sys


def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.79.128',2000)
    s.bind(addr)  # 绑定，端口没有激活
    s.listen(128)  # listen时，端口才激活

    epoll=select.epoll()  # 创建一个epoll对象
    # 让epoll监控s sys.stdin
    epoll.register(s.fileno(),select.EPOLLIN)
    epoll.register(sys.stdin.fileno(),select.EPOLLIN)
    client_list=[] # 存储所有的client对象

    while True:
        # 谁的缓冲区有数据，就填写到events，events是列表，里边存的是元组，(fd,事件
        events=epoll.poll(-1)
        for fd,event in events:
            if fd == s.fileno():
                # 有客户端连接，就连上，得到客户端new_client，放入列表，注册它
                new_client, client_addr = s.accept()
                print(client_addr)
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client=None
                for client in client_list: #遍历所有的客户端对象
                    if client.fileno()==fd:
                        data=client.recv(1000) #接受对应客户端发过来的数据
                        if data: #拿到数据，群发给其他的客户端
                            for other_client in client_list:
                                if other_client is client:
                                    pass
                                else:
                                    other_client.send(data)
                        else:  # 断开了就记录一下
                            remove_client=client
                if remove_client:
                    print('%s已离开聊天室...' % remove_client.fileno())
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()

    new_client.close()
    s.close()

if __name__ == '__main__':
    tcp_server()