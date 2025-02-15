# 作者:李一安
# 2025年02月04日15时54分09秒
# 1713450722@qq.com

# __方法名__格式的方法是python内置的方法，实际上也就是基类object中写好的方法
# 基类object类中有很多这样的方法，而我们手写的类默认继承了这些方法，但是我们可以更新此方法，即再写一遍覆盖

# 内置方法：
# __init__方法：为方法内的属性赋值并开辟内存空间，对象被初始化时，会被自动调用
# __del__方法：对象从内存中被销毁时，会自动调用
# __str__方法：返回对象的描述信息，用于print("对象")



class Cat:
    # 初始化属性
    def __init__(self, name):
        self.name = name

    # 自定义方法
    def eat(self):
        print("吃东西")

    def drink(self):
        print("喝东西")

    # 对象销毁的方法
    def __del__(self):
        print("此对象被销毁")

    # 对象返回值的方法
    def __str__(self):
        return f'对象返回值{self.name}'


def func1():

    tom = Cat("tom")
    # 手动销毁
    del tom

    # 即使不手动销毁，所在代码块运行结束时也会自动调用__del__方法销毁对象
    bob = Cat("bob")

    print(bob)


if __name__ == '__main__':

    func1()