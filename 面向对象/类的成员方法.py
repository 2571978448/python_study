# 赵百超
# 创建时间  2023/9/12  15:04

# 定义在类内部的函数叫做方法
# 定义方法的语法
# def function1 (self,形参1,形参2,形参3,形参4,..)   其中self必须填写, 表示类对象自身的意思, 在方法内部, 想要访问类的成员变量, 必须使用self, 在调用的时候, 可以不理会
#     方法体
class Student:
    name = None
    sex = None
    phone = None

    def say_hi(self):
        print(f"大家好我的名字是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好我的名字是{self.name}")
        print(msg)


stu1 = Student()
stu1.name = "陈奕迅"
stu1.say_hi()

stu2 = Student()
stu2.name = "张学友"
stu2.say_hi2("转身")