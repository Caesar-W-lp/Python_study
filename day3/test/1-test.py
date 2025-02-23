# 作者:李一安
# 2024年12月29日19时39分09秒


import random

# 选择语句

score = 49

def func1():
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")

func1()


print('-'*50)


def func2():
    if score in range(90, 100):
        print("优秀")
    elif score in range(80, 90):
        print("良好")
    elif score in range(60, 80):
        print("及格")
    else:
        print("不及格")

func2()


print('-'*50)


# 随机数演练
# 首先需要在文件顶部开头导入random模块(import random)
# random模块中的randint(a,b)函数可以生成一个闭区间[a,b]内的随机整数，a必须小于等于b。
# if 后面的条件判断语句只能是整数，不能是浮点数
# 且只能是整数参与的比较运算符(>, <, ==,!=, >=, <=)、布尔运算符(and, or, not)、逻辑运算符(not)、位运算符(&, |, ^, ~, <<, >>)、成员运算符(in, not in)、身份运算符(is, is not)。

def func3():

    num1 = int(input("请输入一个位于1-100之间的数字："))

    num2 = random.randint(1,100)

    if num1>num2:
        print("玩家赢了！电脑的数字是%d" % num2)

    elif num1<num2:
        print("电脑赢了！电脑的数字是%d" % num2)

    else:
        print("平局！")


func3()
