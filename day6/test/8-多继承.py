# 作者:李一安
# 2025年02月07日17时03分24秒


class father1:
    def __init__(self, age, *args):# 实际传入的是 年龄 分数
        self.age = age # 吃掉年龄 还剩分数
        super().__init__(*args)# 当前实例对象 分数被传入对


class father2:
    def __init__(self, age):
        pass

class child1(father1, father2):
    def __init__(self, name, *args):
        self.name = name # 姓名被吃掉，剩下 年龄 分数
        super().__init__(*args)# 年龄 分数传入对父类的调用


def function():
    xiaoming = child1("xiaoming", 18, 100) # 姓名 年龄 分数



if __name__ == '__main__':
    print(child1.mro()) # mro是方法解析顺序，输出当前类的继承顺序
    function()



# 总结：
# 在 Python 的类继承机制中，self 是一个指向当前实例对象的引用
# 也就是说无论一个类中出现了多少个对继承类的使用，self都指向当前实例
# 因为在整个继承链中，self 始终是同一个实例对象的引用。
# 无论是 child1、father1 还是 father2 的构造函数，它们操作的都是同一个实例对象 xiaoming。
# super() 的作用之一是将当前实例对象（即 self）传递给父类的构造函数，而不是创建一个新的对象。
# 在多重继承中，super() 的行为是根据 MRO 来决定的，MRO决定了多继承环境中父类的调用顺序
# 当出现多个super().时，会按照顺序逐个使用对应的父类构造函数。
