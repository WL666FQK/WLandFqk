# Author: 王璐
# Date: 2024/12/31
# Time: 15:10

import socket

def tcp_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dest_addr=('192.168.188.1',2000)
    client.connect(dest_addr)
    client.close()

if __name__ == '__main__':
    tcp_client()