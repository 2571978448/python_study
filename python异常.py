# 赵百超
# 创建时间  2023/9/11  21:32

# 异常捕获 语法
try:
    f = open("C:/Users/赵百超/Desktop/test.txt", "r", encoding="UTF-8")
except Exception as e:
    print("ERROR")
    f = open("C:/Users/赵百超/Desktop/test.txt", "w", encoding="UTF-8")
else:
    print("没有异常")
finally:
    print("无论如何都执行")
    f.close()

# 异常的传递
