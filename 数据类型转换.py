# 赵百超
# 创建时间  2023/9/9  10:32
#  常见的转换语句
#  int(x)  将x转换为一个整数
#  float(x)  将x转换为一个浮点数
#  str(x)  将x转换为一个字符串

# 任何类型可转换为字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(3.1415926)
print(type(float_str),float_str)

str_num = int("3213")
print(type(str_num),str_num)

str_float = float("3.1415926")
print(type(str_float),float_str)

#  并不是所有字符串都能转数字，必须合格
#  整数转浮点数，后面回加  .0
#  浮点数转整数，则取
