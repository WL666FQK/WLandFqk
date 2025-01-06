# 4、给定一个 n 个整型元素的列表 a，其中有一个元素出现次数超过 n / 2，求这个元素
list1=[1,2,3,2,5,2,2,3,3,3,3,3]
n=len(list1)/2
for num1 in list1:
    if list1.count(num1)>=n:
        print(num1)
        break
