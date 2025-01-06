#3、 多个缺省参数的传递练习，练习多个缺省参数
def print_info(name,gender="男生",age=18):
    print("%s是%s，年龄%d岁" % (name,gender,age))

if __name__ == '__main__':
    print_info("zhangsan","女生")