# 6、将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
tuple1=(1,2,3)
set1={4,5,6}
# print(type(set1))
tuple2=tuple(set1)
# print(type(tuple2))
list1=list(tuple1+tuple2)
print(list1)

# 7、在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
list2=[1,2,3,4,5,6]
list2.insert(0,7)  #在索引0处添加0，第一个参数是索引，第二个参数是要添加的数据
list2.append(0)
print(list2)

# 8、反转列表 [0,1,2,3,4,5,6,7] 。
list2.reverse()   # 改变list2本身，无返回值，不能用list3直接接收
print(list2)
print(list2.index(5))  # 给出中元素 5 的索引号
print("-"*50)

# 分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2 的元素个数，发现了True为1，False为0
list3=[True,False,0,1,2,1]
print(list3.count(True))
print(list3.count(False))
print(list3.count(0))
print(list3.count(1))
print(list3.count(2))
print("-"*50)

# 11、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
list4=[True,1,0,'x',None,'x',False,2,True]
while "x" in list4:
    list4.remove('x')
print(list4)

# 12、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为 4 的元素。
list5=[True,1,0,'x',None,'x',False,2,True]
list5.pop(4)
print(list5)

# 13、删除列表中索引号为奇数（或偶数）的元素。
list6=[0,1,2,3,4,5,6,7]
del list6[1::2]  # 从索引1开始删除，跨步为2，即删除奇数索引
print(list6)
list6.clear()
print(list6)

# 15、对列表 [3,0,8,5,7] 分别做升序和降序排列。
list7=[3,0,8,5,7]
list7.sort()
print(list7)
list7.sort(reverse=True)
print(list7)
# 16、将列表 [3,0,8,5,7] 中大于 5 元素置为 1，其余元素置为 0。
list7=[3,0,8,5,7]
for index in range(len(list7)):
    if list7[index]>5:
        list7[index]=1
    else:
        list7[index]=0
print(list7)
# 17、遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
list8=['x','y','z']
for value in list8:
    print(value,list8.index(value))

# 18、将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
list9=[0,1,2,3,4,5,6,7,8,9]
list10=[]
list11=[]
for value in list9:
    if value%2==0:
        list10.append(value)
    else:
        list11.append(value)
print(list10)
print(list11)

# 19、分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。
list12=[[6,5],[3,7],[2,8]]
list12.sort()
print(list12)
list12.sort(reverse=True)
print(list12)

# 20、从列表 [1,4,7,2,5,8] 索引为 3 的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
list13=[1,4,7,2,5,8]
list14=['x','y','z']
list15=list13[3:]
print(list15)
list13[3:]=list14
list13=list13+list15
print(list13)

#下面这个方法也能实现
# list13=list13[:3]+list14+list13[3:]
# print(list13)

# 21、快速生成由 [5,50) 区间内的整数组成的列表。
list16=[]
for i in range(5,50):
    list16.append(i)
print(list16)
#a=list(range(5,50))

# 23、将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
list17=['x','y','z']
list18=[1,2,3]
list19=list(zip(list17,list18))
print(list19)

