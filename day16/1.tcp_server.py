# Author: 王璐
# Date: 2024/12/31
# Time: 14:57

import socket

def tcp_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.188.1',2000)
    s.bind(addr)
    s.listen(128)
    new_client,client_addr=s.accept()
    print(client_addr)
    new_client.close()
    s.close()


if __name__ == '__main__':
    tcp_server()
