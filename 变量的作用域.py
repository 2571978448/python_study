# 赵百超
# 创建时间  2023/9/10  21:28

#  变量分为全局变量和局部变量，如果全局变量和局部变量同名，则修改局部变量不会影响全局变量，
#  如果想在函数中修改全局变量，需在函数内部进行声明  (global)

num = 999


def test_a():
    print(num)


def test_b():
    num = 888
    print(num)


def test_c():
    global num
    num = 666
    print(num)


test_a()

test_b()

print(num)

test_c()

print(num)
