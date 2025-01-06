# Author: 王璐
# Date: 2024/12/27
# Time: 17:02

def binary_search(arr,elem):
    left=0
    right= len(arr)-1
    while(left<=right):
        mid = (left + right) // 2
        if elem==arr[mid]:
            return mid
        elif elem>arr[mid]:
            left=mid+1
        else:
            right=mid-1

    return -1  # 未找到时返回-1


if __name__ == '__main__':
    arr=[2,3,5,7,9,10,24,33,62]
    print(binary_search(arr,62))
