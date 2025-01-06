# 打印菱形
def print_demo1():
    i=1
    while i<=9:
        # j = 1  # 空格
        # while j<=abs(5-i):
        print(" "*abs(5-i),end="")
            # j=j+1
        j = 1  # 星号
        while j<=9-2*abs(5-i):
            if j%2==0:
                print(" ",end="")
            else:
                print("*",end="")
            j=j+1
        print()
        i=i+1

# 打印空心菱形
def print_demo2():
    i=1
    while i<=9:
        print(" "*abs(5-i),end="")
        j = 1  # 星号
        while j<=9-2*abs(5-i):
            if j==1 or j==9-2*abs(5-i):
                print("*",end="")
            else:
                print(" ",end="")
            j=j+1
        print()
        i=i+1

if __name__ == '__main__':
    # print_demo1()
    print_demo2()