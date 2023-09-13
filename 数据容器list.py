# 赵百超
# 创建时间  2023/9/10  22:00

#  数据容器: 存储多个元素的Python数据类型
#  数据容器根据特点的不同，分为五类
#  列表(list), 元组(tuple), 字符串(str), 集合(set), 字典(dict)

# 列表(list)   里面的元素类型不受限制, 可以既存储字符串, 又存数字等 , 还可进行列表的嵌套 , 允许数据重复
# 定义: [x,y,z,...]
# 空列表定义: [] 或  list()

name_list = ["陈奕迅", "富士山下", "what's going on"]
print(name_list)
print(type(name_list))
num_list = [[1, 2, 3], [4, 5, 6]]
print(num_list)
print(type(num_list))

#   列表的下标索引, 从0开始 ,  也可反向索引，从后向前, 从-1(代表倒数第一)开始(-1,-2,-3...)  ,  超出列表范围, 会报错, 无法取出元素
print(name_list[0])
print(name_list[-1])
#  嵌套索引
print(num_list[0][0])

#   列表的常用操作方法
name = name_list.index("陈奕迅")  # 查看该元素的下标
print(name)
name_list[0] = "李克勤"  # 修改特定下标索引值
print(name_list)
name_list.insert(1, "蒙面歌王")  # 在特定位置插入元素
print(name_list)
name_list.append("陈奕迅")  # 追加元素到尾部
print(name_list)
name1 = ["周杰伦", "汪峰", "那英"]
name_list.extend(name1)  # 拼接其它数据容器的数据
print(name_list)
#  列表下标元素的删除  list.del(下标)  或者  list.pop(下标)(该方法有一个返回值, 返回删除的元素)
#  列表指定元素的删除(匹配到的第一个)  list.remove()
#  列表清空  list.clear
#  统计指定元素的数量  list.count()
#  统计列表的元素数量  len(list)


