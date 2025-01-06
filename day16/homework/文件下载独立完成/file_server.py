# Author: 王璐
# Date: 2025/1/3
# Time: 8:37

import socket

def get_file_content(file_name):
    try:
        with open(file_name,'rb') as f:
            content=f.read(1024)
            return content
    except:
        print("没有要下载的文件：%s" % file_name)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr=('192.168.188.1',2000)
    s.bind(addr)
    s.listen(128)
    new_client,client_addr=s.accept()


    while True:
        file_name = new_client.recv(1024)
        data=get_file_content(file_name)
        if data:
            new_client.send(data)

    new_client.close()

    s.close()

if __name__ == '__main__':
    main()