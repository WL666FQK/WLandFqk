# Author: 王璐
# Date: 2024/12/27
# Time: 16:23

# 自己写的没有优化的代码
def count_sort(arr):
    i=0
    max_value=0  # 找最大值可以用max函数
    while i< len(arr):
        if arr[i]>max_value:
            max_value=arr[i]
        i+=1
    arr2=[0]*(max_value+1)
    j=0
    while j < len(arr):
        arr2[arr[j]]+=1
        j+=1
    for i in range(0, len(arr2)):
        for j in range(0,arr2[i]):
            print(i,end=" ")

# 经过chatgpt优化的代码
def count_sort_improvement(arr):
    max_value=max(arr)

    count=[0]*(max_value+1)
    for num in arr:
        count[num]+=1
    sorted_arr=[]

    for i in range(0, len(count)):
        for j in range(0,count[i]):
            sorted_arr.append(i)
    print(sorted_arr)


if __name__ == '__main__':
    arr=[2,3,4,7,1,1,2,5,3,3]
    # count_sort(arr)
    count_sort_improvement(arr)