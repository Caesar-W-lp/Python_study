# 作者:李一安
# 2025年02月03日18时02分49秒
# 1713450722@qq.com

# python内置着一个最基本的类object类，这个类是所有类的父类，所有的类都会继承object类中的所有方法
# 类中的方法是唯一的，无论用同一个类构建多少对象，对象中的方法都指向同一个内存空间，不会重复创建相同的方法
# 但是属性却不是，即使属性的数值相同，不同对象的属性的内存空间也不同
# 自创建对象都是可变数据类型


class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    # 对象中的方法都是用于影响对象中的属性的
    # 每个方法在定义时都要在括号内加上形参self，而实际使用时：对象.方法()，括号中并没有实参传入，而是用对象.的方式来传入

    def run(self):
        print(f"{self.name}正在奔跑...")

    def eat(self):
        print(f"{self.name}正在吃东西...")

    def sleep(self):
        print(f"{self.name}正在睡觉...")


def func1():
    Caesar = Person("李一安", 24, "男", "182", "65kg")

    print(f"姓名:{Caesar.name}, 年龄:{Caesar.age}, 性别:{Caesar.gender}, 身高:{Caesar.height}, 体重:{Caesar.weight}")

    Caesar.run()

    Caesar.eat()

    Caesar.sleep()

    # dir就是用于查询能够用对象.这种方式调用的内容

    print(dir(Caesar))


class Dog:
    # 属性
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 方法
    def bark(self):
        print("汪汪汪")

    def happy(self):
        print("摇尾巴")


def func2(people):
    # 构建对象
    wangCai = Dog("wangcai", color="黄色")

    if people == "熟人":
        wangCai.happy()

    else:
        wangCai.bark()


if __name__ == '__main__':
    func1()

    print("-" * 50)

    people = "熟人"
    func2(people)
