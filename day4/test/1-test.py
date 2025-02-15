# 作者:李一安
# 2025年01月06日22时13分43秒
# 1713450722@qq.com
import module

# 元组Tuple
# 元组是另一种有序列表，但是元组一旦定义就不能修改，元组的元素用逗号隔开。
# 类似于列表，元组也可以进行索引。
# 元组的元素类型可以不同，比如可以是数字、字符串、列表、元组等。
# 元组内置方法只有index()和count()。

tuple1 = (1, 2, 3, 4, 5)

print(tuple1.index(3))
print(tuple1.count(3))


module.line()


# 格式化输出
print("%d %d %d %d %d" % tuple1)
# 其实格式化输出 % 后的内容是一个元组或字典。这也是为什么之前在输出时要加括号()的原因。
# "%d %d %d %d %d" % tuple1
# 以上的是python的一种语法，是将后续的元组中的元素逐个填入前面字符串中的占位符，最终返回完成以后的字符串
str1 = "%d %d %d %d %d" % tuple1
print(str1)


module.line()


# 元组的鉴别
def tuple_type_test():
    a = []
    print(type(a)) # <class 'list'>

    b = ()
    print(type(b)) # <class 'tuple'>

    a = [1]
    print(type(a)) # <class 'list'>

    b = (1)
    print(type(b)) # <class 'int'>

    b = (1,) # <class 'tuple'> 加一个逗号，才被视作为元组
    print(type(b))

    # 在不加逗号的情况下，如果元组只有一个元素，括号被视作一个运算符，运算结果就是这个元素。


tuple_type_test()


module.line()


# 元组与列表的类型转换

def tuple_list_change_test():
    a = [1, 2, 3]
    print(a, type(a), id(a))

    b = (3, 4, 5)
    print(b, type(b), id(b))

    a1 = tuple(a)
    print(a1, type(a1), id(a1))

    b1 = list(b)
    print(b1, type(b1), id(b1))

# python中的类型转换，其实是创建了一个新的对象，并将原对象中的内容复制过去，并且改变其数据类型。
# 在Python中，将浮点型转换为整型时，会发生截断，而不是四舍五入。这意味着浮点数的小数部分会被直接舍去，只保留整数部分。

tuple_list_change_test()