# Author: 王璐
# Date: 2024/12/26
# Time: 20:24

# 完成选择排序

def select_sort(arr):
    print(arr)
    i=0
    while i< len(arr):
        min_pos=i
        for j in range(i+1, len(arr)):  # range左闭右开！
            if arr[j]<arr[min_pos]:
                min_pos=j
        arr[i],arr[min_pos]=arr[min_pos],arr[i]  # 交换元素应该这样！而不能直接复制
        i += 1

    print(arr)


if __name__ == '__main__':
    arr=[2,4,1,5,3,8,7,6]
    select_sort(arr)