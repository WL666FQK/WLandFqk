

# 查看两个变量的id情况
def var_id():
    a=1
    print(id(a))
    b=1
    print(id(b))
    a=2
    print(id(a))

if __name__ == '__main__':
    var_id()
    print("-" * 50)
    a=10
    print(id(a))