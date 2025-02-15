# 作者:李一安
# 2025年01月15日17时40分16秒
# 1713450722@qq.com

# 容器学后总结

# 不可变类型和可变类型的根本区别是：在堆内存中是否唯一，以及能否在自己的内存基础上做修改。
# 不可变类型有：整型、浮点型、布尔型、字符串、元组。
# 可变类型有：列表、字典、集合。

# 容器是否有序：能否通过索引访问元素。
# 只有序的容器能切片，切片操作返回一个新的容器，不会影响原容器。
# 只有有序容器才能执行：+、*、>=、<=、==、!=、>、<的操作。
# 有序：列表、元组、字符串
# 无序：集合、字典

# 列表为[]，字典和集合为{}，元组为()，字符串为''或""。

# 只有有序容器才能切片，切片操作返回一个新的容器，不会影响原容器。


# 公共方法：
def common_method():
    a = (1, 2, 3)
    b = ('a', 'b', 'c')

    print(list(zip(a, b)))
    print(dict(zip(a, b)))




def list_compare():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    print(a == b)  # True

    print(id(a) == id(b))  # False
    print(a is b)  # False
    print(a is a)  # True


def index_count():
    str1 = "hello hello"

    # 统计子字符串出现的次数
    print(str1.count("llo"))  # 2
    print(str1.count("abc"))  # 0

    # 找出子字符串第一次出现的索引
    print(str1.index("llo"))  # 2
    print(str1.index("abc"))  # ValueError: substring not found


# 元组拆包
def tuple_break():
    print("元组拆包")

    tuple = ('name', 'age', 'city')
    name, age, city = tuple

    print(name, age, city)


tuple_break()


if __name__ == '__main__':
    #list_compare()
    index_count()






