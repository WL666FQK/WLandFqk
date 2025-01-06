# Author: 王璐
# Date: 2024/12/26
# Time: 21:51

# 完成快速排序

def partition(arr,L,R):
    pivot=arr[L]  # 将第一个元素作为枢轴
    while L<R and arr[R]>=pivot:  # 从右往左比对，若值大于等于枢轴则元素不动，R减一，循环此操作
        R-=1
    arr[L]=arr[R]    # 若元素值小于枢轴，则放到枢轴的左边，也就是L所指的位置

    while L<R and arr[L]<=pivot:
        L+=1
    arr[R]=arr[L]
    arr[L]=pivot
    return L

def quick_sort(arr,L,R):
    if L<R:
        mid=partition(arr, L, R)
        quick_sort(arr,L,mid-1)    # 对枢轴左边进行递归
        quick_sort(arr, mid + 1, R)   # 对枢轴右边进行递归

if __name__ == '__main__':
    arr=[2,1,3,5,4,7,6]
    print(arr)   # 初始顺序
    quick_sort(arr, 0, len(arr)-1)
    print(arr)   # 快排后的顺序