# 作者:李一安
# 2025年02月02日17时42分14秒
# 1713450722@qq.com


# 递归就是一种自调用
# 根据函数栈帧，递归的次数一定是有限的，否则会导致栈溢出

def func1(num):
    print(num, end=' ')

    # 递归函数必须设置终止条件
    if num > 1:
        func1(num-1)

    print(num, end=' ')


def func2(num):

    # 设置递归终止条件
    if num == 1:
        return 1

    # 递归调用
    return num + func2(num-1)


def func3(num):
    '''
    每次只能走1阶或2阶或3阶，走到第n个台阶有多少种方法
    :param num:
    :return:
    '''
    # 终止条件
    if num == 1 or num == 2:
        return num
    elif num == 3:
        return 4

    # 递归调用
    return func3(num-1) + func3(num-2) + func3(num-3)



if __name__ == '__main__':
    func1(5)
    print()

    print('-' * 50)

    print(func2(5))

    print('-' * 50)

    for i in range(1, 10):
        print(func3(i), end=' ')


