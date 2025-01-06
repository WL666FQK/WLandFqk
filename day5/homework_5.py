# 5、 有 101 个整数，其中有 50 个数出现了两次，1 个数出现了一次， 找出出现了一次的那
# 个数。（大家使用 7 个数即可）
def search_single_num():
    list=[8,3,2,6,3,8,2]   # 所有的数都异或起来，就得到了出现1次的那个数，相同的数异或完为0，0和一个数异或结果还是那个数
    result=0
    for i in list:
        result^=i
    print(result)

# 5、 有 102 个整数，其中有 50 个数出现了两次，2 个数出现了一次， 找出出现了一次的那
# 2个数。（大家使用 8 个数即可）
def find_list102_one():
    list=[8,3,2,6,3,8,2,11]
    result=0
    for i in list:
        result^=i  # 得到的是那两个出现一次的数异或的结果
    split_flag=result&-result   # 一个数跟他的相反数按位与能得到这个数最低位为1的值
    result1=0
    result2=0
    for i in list:   # 分成两堆
        if split_flag & i: # 不为0的一堆
            result1 ^= i   # 相同的数异或完为0，0与单独出现的数异或结果为该数
        else:  # 为0的一堆
            result2 ^= i
    print("出现1次的两个数分别为 %d %d" % (result1,result2))
if __name__ == '__main__':
    # search_single_num()
    find_list102_one()