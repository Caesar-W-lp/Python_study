# 作者:李一安
# 2025年02月02日14时53分57秒
# 1713450722@qq.com

def func1(name, age = 18, high = 170, gender = '已入学'):
    # 没有默认值的形参叫位置参数,位置参数是必须要有值传入的，有默认值的形参叫缺省参数，也叫关键字参数
    # 缺省参数必须在位置参数之后，否则会报错
    print(name, age, gender)


def func2(num, *args2, **kwargs2):
    print(num)

    print(args2)

    print(kwargs2)


def func3(*args3, **kwargs3):
    print(f'func3{args3}')
    print(f'func3{kwargs3}')


def func4(*args4, **kwargs4):
    print(f'func4{args4}')  # 此时传入的是一个元组一个字典，都未拆包，都会被视为普通位置参数被*args4吸收
    print(f'func4{kwargs4}')

    func3(args4, kwargs4)
    func3(*args4, **kwargs4)
    # *是给元组解包用的，**是给字典解包用的


if __name__ == '__main__':

    # 若有n个缺省参数，但仅要修改其中m个，m<=n，则在传参时需要写明对应的参数名和值，此时位置参数可换位置：
    func1('张三', gender = '男', high = 175)

    print('-'*50)

    # 多值参数：
    # 函数传入的参数可能是不确定的，此时使用多值参数
    # *args用于接收多个常规位置参数，并将其组成一个tuple，args是这个tuple的名字
    # **kwargs用于接收多个缺省参数，并将其组成一个dict，kwargs是这个dict的名字
    # *args会吃掉所有传入的一系列位置参数，所以若想传入单个位置参数，则其形参必须在*args之前
    # 同理，单个缺省参数也必须在**kwargs之前
    # 缺省参数必须在位置参数之后，所以*args必须在**kwargs之前
    # 若不传入参数，则args和kwargs都为空元组和空字典

    func2(1, 2, 3, 4, 5, name = '张三', age = 18, gender = '男')

    print('-' * 50)

    func4(1, 2, 3, 4, 5, name = '张三', age = 18, gender = '男')



