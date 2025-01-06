# Author: 王璐
# Date: 2024/12/26
# Time: 19:44

# 完成冒泡排序

def bubble_sort(arr):
    print("排序前:",arr)
    j= len(arr)-1
    flag=0
    while j>0:
        for i in range(len(arr)-1,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                flag=1
        if flag==0:
            break
        j-=1
    print("排序后:",arr)

if __name__ == '__main__':
    arr=[2,4,3,5,9,6,7,8]
    bubble_sort(arr)