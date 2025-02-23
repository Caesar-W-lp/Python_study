# 作者:李一安
# 2025年01月15日17时24分54秒

import module

# 集合
# 集合set是由一组无序的、唯一的元素组成的。
# 集合的元素可以是任何类型，包括数字、字符串、元组、列表等。
# 由于集合为无序的，因此不能通过索引访问集合中的元素。

def test_set():

    # 去重
    list = [1, 2, 2, 3]
    set1 = set(list)
    print(set1)  # {1, 2, 3}

    module.line()

    # 初始化集合
    set2 = {1, 2, 3}

    module.line()

    # 大括号内为空是空字典,而非空集合
    set3 = {}
    print(set3, type(set3))

    module.line()

    # 空集合的创建
    set4 = set()
    print(set4, type(set4))

    module.line()

    #集合的复制(会产生一个新的集合对象)
    set5 = set2.copy()
    print(set2, type(set2), id(set2))
    print(set5, type(set5), id(set5))




if __name__ == '__main__':

    test_set()


