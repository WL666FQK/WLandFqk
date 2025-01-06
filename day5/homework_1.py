def print_odd_sum():
    result=0
    r=1
    while r<=100:
        if r%2==1:
          result+=r
        r=r+1
    print("1到100之间的奇数和为：%d" % result)

if __name__ == '__main__':
    print_odd_sum()