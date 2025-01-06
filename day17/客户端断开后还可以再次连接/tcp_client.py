# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

# epoll需要在linux下执行
import socket
import select
import sys

def tcp_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dest_addr=('192.168.79.128',2000)
    client.connect(dest_addr)
    epoll = select.epoll()  # 创建一个epoll对象
    # 让epoll监控new_client sys.stdin
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)

    while True:
        # 谁的缓冲区有数据，就填写到events,events是列表 里边存的是元组(fd，事件)
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == client.fileno():
                data = client.recv(100)
                if data:
                    print("服务器端："+data.decode('utf8'))
                else:
                    print("[服务器端断开了...]")
                    return
            elif fd == sys.stdin.fileno():
                try:
                    data = input()  # 客户端说话，发给对方
                except EOFError:  # 按control d后让客户端断开
                    print("[已下线...]")
                    return
                client.send(data.encode('utf8'))

    client.close()

if __name__ == '__main__':
    tcp_client()