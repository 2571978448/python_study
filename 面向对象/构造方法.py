# 赵百超
# 创建时间  2023/9/12  15:52

# 构建类对象时, 通过传参的方式对属性进行赋值, 使用 __init__()方法, 称之为构造方法, 在创建类对象时, 会自动执行, 将传入参数自动传递给  __init__方法使用
class Student:
    name = None
    sex = None
    phone = None

    def __init__(self, name, sex, phone):
        self.name = name
        self.sex = sex
        self.phone = phone
        print("init方法执行了")


stu1 = Student(name="陈奕迅", sex="man", phone=13576300323)
print(stu1.name)
print(stu1.sex)
print(stu1.phone)