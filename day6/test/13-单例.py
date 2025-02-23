# 作者:李一安
# 2025年02月08日17时45分55秒



# 设计模式（23种）
# 单例模式：即一个类只能创建一个实例对象

class MusicPlayer:

    # 类属性
    instance = None # 用来保存这个唯一对象的引用

    # __new__方法是object父类中已有的方法，在实例化时会自动执行，用于为对象开辟内存空间，并返回对应的引用
    # __new__方法先于__init__方法自动执行
    # 这里为了实现单例模式，需要修改原本默认的实例化对象的方法
    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        if cls.instance is None:
            cls.instance = super().__new__(cls) # 这里用到的是object父类中的__new__，即原本默认的创建实例化对象的方法


        return cls.instance

    # 单例模式虽然不会改变实例的内存位置，但是后续的init会覆盖之前的init
    def __init__(self, name):
        self.name = name




if __name__ == '__main__':
    player1 = MusicPlayer("七里香")
    print(id(player1))

    player2 = MusicPlayer("东风破")
    print(id(player2))


