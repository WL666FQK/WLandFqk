# Author: 王璐
# Date: 2024/10/18

# 4、通过 readline 依次读取文件每一行并打印
file = open('file2.txt',mode='r+',encoding='utf8')
while True:
    text = file.readline()
    if not text:
        break
    print(text,end='')