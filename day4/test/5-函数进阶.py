# 作者:李一安
# 2025年01月31日21时53分17秒
# 1713450722@qq.com


def function_1(x, y):
    return x+y, x-y, x*y, x/y


def function_2(x, y):
    x, y = y, x
    return x, y


def function_3(x, y):
    x += y
    return x


def function_4(x, y=3):
    return x+y




if __name__ == '__main__':

    # 函数返回多个值
    # 返回的多个值默认以元组的形式返回
    ret = function_1(1, 2)
    print(ret)  # (3, -1, 2, 0.5)


    # 多个变量交换值
    ret = function_2(2, 3)
    print(ret)  # (3, 2)


    # +=的实质就是对extend()方法的调用
    ret = function_3(1, 2)
    print(ret)  # 3

    ret = function_3([1, 2], [3, 4])
    print(ret)  # [1, 2, 3, 4]


    # 缺省参数
    # 即形参带有默认值，当调用函数时，如果没有传入该参数，则使用默认值，若传入了该参数，则覆盖默认值
    # 缺省参数只能位于所有非缺省参数的后面
    ret = function_4(1)
    print(ret)  # 4

    ret = function_4(1, 2)
    print(ret)  # 3



