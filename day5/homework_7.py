def say_hello(a):
    """
    say_hello内部的注释
    :param a:
    :return:
    """
    for i in range(1,a+1):
        print("hello")

if __name__ == '__main__':
    say_hello(int(input("请输入一个数：")))