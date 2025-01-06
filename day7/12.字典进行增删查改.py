xiaoming = {"name":"小明",
            "age":18,
            "gender":True,
            "height":1.75}

# 1 新增和修改
xiaoming['408']=120
xiaoming['408']=125
xiaoming.setdefault('408',130)
print(xiaoming)
xiaoming.update({'math':120,'english':110},)
print(xiaoming)
print('-'*50)

# 2 查询
print(xiaoming['math'])  # 如果没有math的话程序就会报错
print(xiaoming.get('math'))  # 如果没有math的话返回None
for key in xiaoming:  #默认是key
    print(key)

for v in xiaoming.values():  # 所有value列表
    print(v)

for i in xiaoming.items():  # 所有(key,value)元组列表
    print(i)

print('-'*50)

# 3 删除
del xiaoming['math']
print(xiaoming)
xiaoming.pop('english')
print(xiaoming)
xiaoming.popitem()  # 随机删除
print(xiaoming)