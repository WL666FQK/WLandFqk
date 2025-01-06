# num1 和num2 是形参
def sum_2_num(num1,num2):
    result = num1 + num2
    print('%d+%d=%d' % (num1,num2,result))
    return result


# 10 和 50 是实参
result=sum_2_num(10,50)
print(result)