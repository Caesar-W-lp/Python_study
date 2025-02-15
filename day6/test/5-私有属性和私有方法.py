# 作者:李一安
# 2025年02月07日12时58分55秒
# 1713450722@qq.com

# 属性名或方法名前面加两个下划线__就是私有方法和私有属性
# 私有属性 和 私有方法 只能在类内进行访问
# 私有属性和私有方法依然会被继承给子类，但是无法用子类对象去访问，需要使用从父类继承来的


class Women:
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age

    def __str__(self):
        return f"{self.name}的年龄是{self.__age}"

    def __secret(self):
        print(self.__age)

    def tell(self):
        self.__secret()


def func():
    xiaohong = Women('xiaohong', 20)
    print(xiaohong.name)
    # print(xiaohong.__age) 私有属性无法使用除对象内置方法以外的方法去访问
    print(xiaohong)

    # xiaohong.secret() 私有方法无法使用除对象内置方法以外的方法去访问
    xiaohong.tell()



if __name__ == '__main__':
    func()