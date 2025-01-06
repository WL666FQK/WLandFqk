# 9 编写代码理解
# 不可变类型，内存中的数据不允许被修改：
# 数字类型 int, bool, float, complex, long(2.x)
# 字符串 str
# 元组 tuple
# 可变类型，内存中的数据可以被修改：
# 列表 list
# 字典 dict

var_type=[10,10.0,"luck",(1,2,3),[1,2,3],set([1,2,3]),{"name":'jhk'}]

for i in var_type:
    t=type(i)
    add1=id(i)
    print("变量类型",t,"初始值",i,"初始内存地址",add1)
    if isinstance(i,int):i+=1
    elif isinstance(i,float):i+=1.0
    elif isinstance(i,str):i+="!"
    elif isinstance(i,tuple):i+=(4,5,6)
    elif isinstance(i,list):i+=[4,5,6]
    elif isinstance(i,set):i.add(4)
    elif isinstance(i,dict):i.update({'sex':'male'})

    add2=id(i)
    print("变量类型",t,"更改值",i,"更改内存地址",id(i))
    if add1==add2:
        print("显而易见，该变量类型原地可更改！！！")
    else:
        print("显而易见，该变量类型不可原地更改！！！")
    print("*"*10)