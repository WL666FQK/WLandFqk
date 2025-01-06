# Author: 王璐
# Date: 2024/12/26
# Time: 20:57

# 完成插入排序

def insert_sort(arr):
    print(arr)
    for i in range(1, len(arr)):
        insert_val=arr[i]  # 将要插入的值保存到insert_val
        j=i-1 # 前j+1个是已经排好序的元素
        while j>=0 and arr[j]>insert_val:  # 当j<0或者要插入的值比已排好序里的最大值还大时，跳出循环
            arr[j+1]=arr[j]  # 插入排序的思想是将大于insert_val的值往后移动，最后将insert_val插入到合适位置，而不是用交换
            j-=1
        arr[j+1]=insert_val  # 将要插入的值放到合适位置
    print(arr)


if __name__ == '__main__':
    arr=[2,4,3,1,6,2,5]
    insert_sort(arr)