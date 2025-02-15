# 作者:李一安
# 2025年02月07日13时14分03秒
# 1713450722@qq.com

# 继承：由于子类会集成父类的所有属性和方法，所以可以将所有子类都共有的属性和方法写入一个父类，做到方便
# 继承是用在子类的定义上
# 若子类有与父类相同的属性或方法，会覆盖掉父类的属性或方法

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eating')

    def drink(self):
        print('drink')

    def run(self):
        print('running')

    def sleep(self):
        print('sleeping')


class Dog(Animal):
    def __init__(self, name):
        self.name = name # 覆盖,但是这种方法一般不用，都是用调用

    def bark(self):
        print('bark')


class FlyDog(Dog): # 多重继承

    def fly(self):
        print('fly')


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) # 子类对象调用父类的init方法中的name属性，而非覆盖，super()代表父类
        self.color = color

    def run(self):# 对父类方法的覆盖
        super().run()
        print(f"{self.name} is running")


    def catch(self):
        print('catch')


class SuperCat(Cat):
    def __init__(self, name, color, age):
        super().__init__(name, color)# 这个是根据继承的父类来进行调用，即根据()里所写的类
        self.age = age

    def fly(self):
        print('fly')


def func():
    xiaogou = Dog('xiaogou')
    xiaogou.eat()
    xiaogou.drink()
    xiaogou.run()
    xiaogou.sleep()
    xiaogou.bark()

    print("-"*50)
    xiaotianquan = FlyDog('xiaotianquan')
    xiaotianquan.fly()


    print("-" * 50)

    xiaomao = Cat('xiaomao', 'blue')
    xiaomao.eat()
    xiaomao.drink()
    xiaomao.run()
    xiaomao.sleep()
    xiaomao.catch()

    print("-" * 50)

    chaomao = SuperCat('chaomao', 'blue', 1)
    chaomao.fly()
    chaomao.catch()


if __name__ == '__main__':
    func()