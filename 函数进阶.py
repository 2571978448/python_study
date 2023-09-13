# 赵百超
# 创建时间  2023/9/11  16:56

# 函数的多返回值
# 1, 将多个返回值(类型不限)写在同一行, 用一个return进行返回  再用多个变量进行接收
def multi_return():
    return 1, 2, 3


x, y, z = multi_return()
print(x, y, z)


# 函数的多种传参方式  根据方式上的不同, 分为 1,位置   2,关键字  3,缺省  4,不定长

# 1，位置参数 调用函数时根据函数定义的位置来传递参数   * 顺序和数量必须一致
def user_info(name, music, album):
    print(name, music, album)


user_info("陈奕迅", "富士山下", "what's going on")

# 2, 函数调用时通过"键=值"形式传递  可以乱序
user_info(name="陈奕迅", music="富士山下", album="what's going on")


# 3, 缺省参数, 即设置默认值(调用时可不传递), *所有位置参数必须在默认参数前

# 4, 不定长参数, 不确定会传递几个参数  分为   *位置不定长   *关键字不定长
# *位置不定长   所有变量都会被args收集, 形成一个元组tuple
def user_info(*args):
    print(args)


# *关键字不定长  必须传键值对  形成一部字典dict
def user_message(**kwargs):
    print(kwargs)

# 函数作为传递参数  传递逻辑, 而非传入数据

# lambda匿名函数, 无名称   只可使用一次  语法: lambda 传入参数: 函数体(一行代码)

