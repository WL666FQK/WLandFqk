# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

import socket

def tcp_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dest_addr=('192.168.188.1',2000)
    client.connect(dest_addr)
    while True:
        # 先说话
        data=input()  # 会卡住
        client.send(data.encode('utf8'))
        data=client.recv(1000)  # 收对方说的话
        print(data.decode('utf8'))
    client.close()

if __name__ == '__main__':
    tcp_client()