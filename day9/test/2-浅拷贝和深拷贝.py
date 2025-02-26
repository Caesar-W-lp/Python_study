# 作者:李一安
# 2025年02月25日22时34分26秒

# 赋值、浅拷贝、深拷贝
# 浅拷贝和深拷贝只适用于可变数据类型，不可变数据类型是按值传递的

# 赋值
def assignment():
    """
    赋值
    赋值传递的是引用, 即两个变量指向同一个对象.
    :return:
    """
    a = [1, 2, 3]
    print(f"a的id为{id(a)}")

    b = a
    print(f"b的id为{id(b)}")

    b[0] = 10
    print(a)  # [10, 2, 3]
    print(b)  # [10, 2, 3]


assignment()
print('-' * 50)


# 浅拷贝1
def shallow_copy_1():
    """
    浅拷贝1
    列表自身带有一个拷贝接口.copy()
    :return:
    """
    a = [1, 2, 3]
    print(f"a的id为{id(a)}")

    b = a.copy()
    print(f"b的id为{id(b)}")

    b[0] = 10
    print(a)  # [1, 2, 3]
    print(b)  # [10, 2, 3]


shallow_copy_1()
print('-' * 50)


# 浅拷贝2
import copy
def shallow_copy_2():
    """
    浅拷贝2
    导入copy模块, 并使用copy.copy()
    优于.copy()方法, 因为它可以作用于所有的可变数据类型
    :return:
    """
    a = [1, 2, 3]
    print(f"a的id为{id(a)}")

    b = copy.copy(a)
    print(f"b的id为{id(b)}")

    b[0] = 10
    print(a)  # [1, 2, 3]
    print(b)  # [10, 2, 3]


shallow_copy_2()
print('-' * 50)



# .copy()方法和copy.copy()方法都是浅拷贝方法
# 浅拷贝仅会将第一层指向的对象拷贝，最终产生地址不同的第一层对象和第一层对象副本
# 但是若有嵌套n层对象，则指向第二层到第n层的对象的引用依然相同

def use_shallow_copy():
    """
    copy是浅copy，只做第一层copy
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))

    # 这里使用的a是最初始的a，而非拷贝后产生的a，初始与副本的地址不同
    a[0] = 10

    print(f'c--{c}')
    print(f'd--{d}')
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


use_shallow_copy()
print('-' * 50)



# 深拷贝
# 将对象及其内部嵌套指向的所有对象全都拷贝一个副本存放在新的地址空间中
# id()的作用是返回所指向的对象的内存空间地址

def use_deep_copy():
    """
    递归去copy，不管有多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))

    # 这里使用的a是最初始的a，而非拷贝后产生的a，初始与副本的地址不同
    a[0] = 10

    print(f'c--{c}')
    print(f'd--{d}')
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


use_deep_copy()
print('-' * 50)



# 浅拷贝：第二层对象是不可变数据类型时使用：[1, 2, 3]
# 深拷贝：第二层对象存在可变数据类型时使用：[[1, 2], [3, 4]]

class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子', '指环']

    def __repr__(self):
        return repr((self.name, self.blood, self.equipment, id(self.name), id(self.blood), id(self.equipment)))



# 若深度拷贝的对象中既有嵌套不可变类型，也有可变类型，则深度拷贝仅会拷贝所有层级的可变类型
def use_copy_object():
    """
    实际对于自定义对象的练习
    :return:
    """
    old_hero = Hero('蚂蚁', 90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80  #新对象修改后，原对象不会受到任何影响
    new_hero.equipment.append('药水')
    print(old_hero)
    print(new_hero)

    # 不可变类型作为二层及以后的对象，即使经历了深度拷贝，原数据与副本的指向依然相同
    # 其实就像一条链子被复制，只有链子尾部才是不可变数据类型，中间的链子是可变数据类型
    # 原链子和链子副本只有尾部的指向相同，因为不可变数据类型在内存中是唯一的


use_copy_object()