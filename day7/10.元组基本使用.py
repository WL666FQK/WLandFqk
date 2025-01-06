info_tuple=(50,)  # 元组一个元素要加逗号，不加逗号就是整型元素

print(type(info_tuple))

info_tuple = ("zhangsan",18,1.75,"zhangsan")

# 1.取值和取索引
print(info_tuple[0])
print(info_tuple.index("zhangsan"))

print(info_tuple.count("zhangsan"))
print(len(info_tuple))