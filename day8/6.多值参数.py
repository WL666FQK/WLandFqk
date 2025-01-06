def demo1(*args,**kwargs):
    print(args)
    print(kwargs)

# 可变参数 也叫 多值参数
# 在元组前加*就是解包(unpack),效果就是(1,2,3,4)会变成1,2,3,4
# 在字典前加**就是解包(unpack),效果把{'name': '小明', 'age': 18, 'gender': True}
# 变成name="小明",age=18,gender=True
def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)
    print('-'*50)
    demo1(*args,**kwargs)

demo(1,2,3,4,5,name="小明",age=18,gender=True)