# Author: 王璐
# Date: 2024/10/19

import random

class MySort:
    def __init__(self,arr_len):
        self.arr=[]
        self.arr_len=arr_len

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0,99))

    def bubble(self):
        arr=self.arr
        i=self.arr_len-1
        while i>0:
            j=0
            flag=1
            while j<i:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                j+=1
            if flag:  # 如果某一趟没有交换过，就代表已经有序
                break
            i-=1

    def test_sort(self,sort_method):
        print(self.arr)
        sort_method()
        print(self.arr)

    def select_sort(self):
        arr=self.arr
        for i in range(self.arr_len-1):
            min_position=i
            for j in range(i+1,self.arr_len):
                if arr[min_position]>arr[j]:
                    min_position=j
            arr[min_position],arr[i]=arr[i],arr[min_position]

    def insert_sort(self):
        arr=self.arr
        i=1
        while i<self.arr_len:
            insert_val=arr[i]
            j=i-1
            while j>=0:
                if arr[j]<insert_val:
                    break
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=insert_val
            i+=1


if __name__ == '__main__':
    temp=MySort(10)
    temp.random_int()
    temp.test_sort(temp.insert_sort)