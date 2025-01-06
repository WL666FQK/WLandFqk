# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

# 一人只能轮流说一句
import socket

def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.188.1',2000)
    s.bind(addr)  # 绑定，端口没有激活
    s.listen(128)  # listen时，端口才激活
    new_client,client_addr=s.accept()

    while True:
        data=new_client.recv(100)  # 会卡住
        print(data.decode('utf8'))
        data=input()  # 服务器端说话，发给对方
        new_client.send(data.encode('utf8'))

    new_client.close()
    s.close()

if __name__ == '__main__':
    tcp_server()