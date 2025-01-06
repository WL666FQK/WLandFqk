# 24、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
# 25、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
# 26、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
dict1={'Alice': 20, 'Beth': 18, 'Cecil': 21}
print("all keys:",list(dict1.keys()))
print("all values:",list(dict1.values()))
print("all items:",tuple(dict1.items()))

# 27、向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新 Cecil
# 的值为 17。
dict2={'Alice': 20, 'Beth': 18, 'Cecil': 21}
dict2['David']=19
dict2['Cecil']=17
print(dict2)

# 28、删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的 Beth 键后，清空该字典。
dict3={'Alice': 20, 'Beth': 18, 'Cecil': 21}
del dict3['Beth']
print(dict3)
dict3.clear()
print(dict3)

# 29、判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
dict3={'Alice': 20, 'Beth': 18, 'Cecil': 21}
keys=['David','Alice']
for key in keys:
    if dict3.get(key):
        print("{} 在字典中，值为{}".format(key,dict3[key]))
    else:
        print(key,"不在字典中")

# 30、遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
dict3={'Alice': 20, 'Beth': 18, 'Cecil': 21}
for key,val in dict3.items():
    print("key:{} value:{}".format(key,val))

# 32、以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是 0，创建一个字典。
keys=['A','B','C','D','E','F','G','H']
dict4={}
for key in keys:
    dict4[key]=0
print(dict4)

# 33、将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
a=[['a',1],['b',2]]
b=(('x',3),('y',4))
print(dict(a))
print(dict(b))
# 34、将元组 (1,2) 和 (3,4) 合并成一个元组。
a=(1,2)
b=(3,4)
print(a+b)

# 35、将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
x,y,z=(1,2,3)
print(x,y,z)

# 36、返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
a=('Alice','Beth','Cecil')
print(a.index('Cecil'))

# 37、返回元组 (2,5,3,2,4) 中元素 2 的个数。
a=(2,5,3,2,4)
print(a.count(2))


# 38、判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
a=('Alice','Beth','Cecil')
if 'Cecil' in a:
    print("{}在元组中".format('Cecil'))
else:
    print("{}不在元组中".format('Cecil'))

# 39、返回在元组 (2,5,3,7) 索引号为 2 的位置插入元素 9 之后的新元组。
a=(2,5,3,7)
a=a[:2]+(9,)+a[2:]
print(a)

# 40、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。

s1=set().union(['x','y','z'])
print(s1)

# 41、删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合。
s1=set(['x','y','z'])
s1.remove('z')
s1.add('w')
print(s1)
s1.clear()
print(s1)

# 42、返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
# 43、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
# 44、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
# 45、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
# 46、判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
a=set(['A','D','B'])
b=set(['E','D','C'])
print("差集",a.difference(b))
print("并集",a.union(b))
print("交集",a.intersection(b))
print(a.union(b)-a.intersection(b))

if a.intersection(b):
    print('存在交集',a.intersection(b))
else:
    print('不存在交集')


# 47、判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
a=set(['A','C'])
b=set(['D','C','E','A'])
if a.union(b)==b:
    print("是子集")
else:
    print("不是子集")

# 48、去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
a=[1,2,5,2,3,4,5,'x',4,'x']
a=list(set(a))  # 集合中不能有重复元素
print(a)

# 49、返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
# 50、判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
s='abCdEfg'
print("全部都为大写：",s.upper())
print("全部都为小写：",s.lower())
print("转换大小写后：",s.swapcase())
print("是否全小写：",s.islower())
print("是否全大写：",s.isupper())

# 51、返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
# 52、判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
# 53、返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
# 54、返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
s='this is python'
print(s.capitalize())
print(s.title())
print('以this开头',s.startswith("this"))
print('以python结尾',s.endswith("python"))
print('is出现次数',s.count('is'))
print("首次出现的位置：{} 最后1次出现的位置：{}".format(s.index('is'),s.rindex('is')))
# 55、将字符串 ‘this is python’ 切片成 3 个单词。
print(s.split(" "))
# 56、返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
s='blog.csdn.net/xufive/article/details/102946961'
print(s.split('/'))
# 57、将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
s='2.72, 5, 7, 3.14'
list=s.split(',')
list2=[]
for i in list:
    if '.' in i:
        list2.append(float(i))
    else:
        list2.append(int(i))
print(list2)

# 58、判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母？
s='adS12K56'
if s.isalnum():
    print("全为数字、字母")
elif s.isnumeric():
    print("全为数字")
elif s.isalpha():
    print("全为字母")

# 59、将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。
s='there is python'
print(s.replace('is','are'))

# 60、清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
s='\t python \n'
print(s)
print("清除左侧空白",s.lstrip())
print("清除右侧空白",s.rstrip())
print("清除左右两侧空白",s.strip())

# 61、 将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
list=['ok', 'hello', 'thank you']
l=len(list[2])
print("左对齐")
for i in list:
    print(i.ljust(l))
print("*"*10)
print("右对齐")
for i in list:
    print(i.rjust(l))
print("*"*10)
print("中间对齐")
for i in list:
    print(i.center(l))

# 63、将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补 0 成同样长度。
list=['15', '127', '65535']
max=0
for i in list:
    if len(i)>max:
        max= len(i)
for i in list:
    print(i.rjust(max,'0'))

# 64、将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。
list=['a','b','c']
s=""
for i in list:
    s += i
    if list.index(i)+1<len(list):
        s+='|'
print(s)
# 65、将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
s='abc'
print(','.join(s))

# 66、从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
# phone=input("输入手机号:")
# print('Mobile:'+phone)

# 74、将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
a1=[]
a=[[1,2],[2,3],[4,5]]
for i in a:
    for j in i:
        a1.append(j)
print('a1 =',a1)

a='A B C D E'.split()
b=range(len(a))
dic=dict(zip(a,b))
print(dic)
