# 3、求两个有序数字列表的公共元素，可用set(list1).intersection(list2)

list1=[1,2,3,4]
list2=[2,3,4,5,6,7]

# print(set(list1).intersection(list2))

for num1 in list1:
    for num2 in list2:
        if num1==num2:
            print(num1)