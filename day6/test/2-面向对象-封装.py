# 作者:李一安
# 2025年02月04日19时29分00秒
# 1713450722@qq.com


# 封装：把属性和方法封装在一个类中，属性只能通过这个类中的方法来操作

class Animal:
    def __init__(self, name, wight):
        self.name = name
        self.wight = wight

    def run(self):
        self.wight -= 0.5
        print(f"{self.name}正在跑步，跑步后体重为{self.wight}")

    def eat(self):
        self.wight += 1
        print(f"{self.name}正在进食，进食后体重为{self.wight}")

    def __str__(self):
        # 此方法的返回值必须是字符串
        return f"{self.name}当前体重为{self.wight}"


def func1():
    elephant = Animal("elephant", 200)

    elephant.run()

    elephant.eat()

    print(elephant)


if __name__ == '__main__':
    func1()
