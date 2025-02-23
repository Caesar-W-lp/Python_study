# 作者:李一安
# 2025年02月07日17时43分08秒


class Father:
    def __init__(self, city):
        self.city = city



class Son1(Father):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)

class Son2(Father):
    def __init__(self, gender, *args):
        self.gender = gender
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        super().__init__(*args)


def function():
    print(Grandson.__mro__)

    sunzi = Grandson("sunzi", 20, "male", "beijing")

    print(sunzi.name)
    print(sunzi.age)
    print(sunzi.gender)
    print(sunzi.city)


if __name__ == '__main__':

    function()

    # __mro__产生的顺序有点像子节点和父节点的顺序，
    # 子类从左到右，子类完了以后才是父类，父类从左到右，若还有祖父类，则以之前的规律来套用。