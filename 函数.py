# 赵百超
# 创建时间  2023/9/10  20:09

# 组织好的，可重复使用的，用来实现特定功能的代码段

#  定义(def)一个函数  函数名, 函数体, 返回值

def count_len(data):
    count = 0
    for x in data:
        count += 1
    print(f"字符串'{data}'的长度是{count}")


count_len("苦心选中今天想车你回家")


#  函数若无返回值, 默认返回的是None

#  函数的文档说明
def add(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    print(x + y)
    return x + y


add(3, 3)
