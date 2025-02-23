# 作者:李一安
# 2025年02月07日14时49分57秒



class A:

    def method_1(self):
        print("A的第一个方法")

    def method_2(self):
        print("A的第二个方法")


class B():
    def method_1(self):
        print("B的第一个方法")

    def method_2(self):
        print("B的第二个方法")


class C(A, B):# 这里(A, B)和(B, A)是不一样的，这里的先后顺序决定了使用同名方法时的覆盖关系，其实就是mro的顺序
    pass


def func():
    c = C()
    c.method_1()


if __name__ == '__main__':
    func()
    print(C.mro())# 这个接口是

