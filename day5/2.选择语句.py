def use_if():
    # 1.定义年龄变量
    age = 17

    # 2.判断是否满18岁
    # if语句以及缩进部分的代码是一个完整的代码块
    if age >= 18:
        print("可以进网吧嗨皮...")
        print('打游戏')

    # 3.思考！-无论条件是否满足都会执行
    print("这句代码什么时候执行?")


def use_if2():
    python_score = 50
    c_score = 50

    # 要求只要有一门成绩 > 60分就算合格
    if not python_score > 60 or c_score > 60:
        print("考试通过")
    else:
        print("再接再厉！")


def use_elif():
    holiday_name = "平安夜"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊...")


if __name__ == '__main__':
    # use_if()
    # use_if2()
    use_elif()