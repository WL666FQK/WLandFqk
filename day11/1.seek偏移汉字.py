# Author: 王璐
# Date: 2024/12/25

def use_seek():
    file=open('file',mode='r+',encoding='utf8')
    file.seek(3)
    text=file.read()
    print(text)
    file.close()

def write_binary():
    file=open('file',mode='rb+')
    btext=file.read()
    print(btext)
    file.write(b'world')
    file.write('我很帅'.encode('utf8')) # 以字节流形式写入，如果是英文前面加b
    file.close()

if __name__ == '__main__':
    # use_seek()
    write_binary()