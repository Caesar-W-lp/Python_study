# 作者:李一安
# 2025年02月09日20时14分43秒
# 1713450722@qq.com

# 私有属性并不继承
# 子类

class A:
    def __init__(self):
        self.__b = 20

    def print_b(self):
        print(self.__b)


class B(A):
    pass

def function():

    a = A()
    b = B()

    a.print_b()

    b.print_b()


if __name__ == '__main__':
    function()