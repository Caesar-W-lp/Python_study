# 作者:李一安
# 2025年01月05日21时19分59秒


import my_module

# 高级变量类型
# 列表
# 列表类似于C语言中的数组，可以存储多个值，可以随时添加或删除元素。
# 不同的是列表可以存储不同类型的数据，可以包含任意类型的数据。


# 创建列表
# 列表是用方括号[]括起来的元素，用逗号分隔。

list1 = [1, 2, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'orange']
list3 = [1, 'apple', 3.14, True]


my_module.print_line()


# 写在对象内部的函数叫做方法，可以直接在对象上调用。
# 列表对象内部带有自己的方法，可以对列表进行操作。

# 增删改查
# 任何非法的操作都会报错。


# 增：
# 列表.insert(索引, 值)，在指定索引处插入值。
# 列表.append(值)，在列表末尾添加值。
# 列表.extend(另一个列表)，在列表末尾添加另一个列表。

def test_list_add(list1, list2):
    list1.insert(6, 'new')
    print(list1)

    list1.append('end')
    print(list1)

    list1.extend(list2)
    print(list1)

test_list_add(list1, list2)


my_module.print_line()


# 删：
# 列表.del 列表[索引]，删除指定索引处的元素。
# 列表.remove(指定值)，删除列表中第一个值为指定值的元素。
# 列表.pop(n)，若无参数，删除列表末尾的元素，若有参数n，则删除指定索引n处的元素。
# 列表.clear()，清空列表。
# del 列表，删除整个列表。
# del 列表[索引]，删除指定索引处的元素。

def test_list_del(list1):
    del list1[0]
    print(list1)

    list1.remove(2)
    print(list1)

    list1.pop()
    print(list1)

    print(list1[0], list1, id(list1))
    list1.clear()
    # print(list1[0]) # 列表为空，会报错。
    print(list1, id(list1))
    # 清空列表，不是删除整个列表，而是清空列表中的元素，列表本身依然存在，列表内元素个数为0。

    del list1
    # print(list1, id(list1)) # 删除整个列表，列表本身不存在。
    # 注意：del 列表，只是删除栈内存中那个指向堆内存列表对象的变量，而堆内存中的列表对象依然存在，除非因为引用计数为0，才会被自动回收。


test_list_del(list1)


my_module.print_line()


# 改：
# 列表[索引] = 新值，修改指定索引处的值。

def test_list_modify(list1):

    # list1[10] = 'change'
    # print(list1)
    # 越界修改会报错。

    list1[0] = 'change'
    print(list1)

test_list_modify(list3)


my_module.print_line()


# 查：
# 列表[索引]，获取指定索引处的值。
# 列表.len(列表)，获取列表长度。
# len(容器对象)可以统计所有容器的元素个数，它是一个通用的内置函数。
# 查询的元素 in 列表，判断元素是否在列表中。
# 列表.index(指定值)，获取指定值的索引。
# 列表.count(指定值)，获取指定值的出现次数。

def test_list_query(list1):

    print(list1[0])
    # print(list1[8]) # 索引越界，会报错。

    print(len(list1))

    print(2 in list1)
    print(3.14 in list1)

    # print(list1.index(2)) # 若没有找到指定值，会报错。
    print(list1.index(3.14))

    print(list1.count(2))
    print(list1.count(3.14))

test_list_query(list3)


my_module.print_line()


# 排序：
# 列表.sort()，对列表进行升序排序。
# 列表.reverse()，将列表倒过来排列。
# 列表.sort(reverse=True)，对列表进行降序排序。
# 字符串之间的排序是按照对应位置的字符进行逐个比较ASCII码的大小。
# 只有列表中的元素都是同一类型，才可以进行排序。

def test_list_sort(list1):

    list1.sort()
    print(list1)

    list1.reverse()
    print(list1)

list4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
test_list_sort(list4)

list5 = [1.1, 2.2, 3.3, 4.4, 5.5]
test_list_sort(list4)

list6 = ['apple', 'banana', 'orange', 'apple', 'banana']
test_list_sort(list5)


my_module.print_line()


# 遍历列表
# for element in 列表：
# 顺序从列表中依次获得数据，每一次循环过程中，数据都会保存在element这个变量中。


def test_list_for(list):
    for element in list:
        print(element, end=' ')

list7 = ['apple', 'banana', 'orange', 'apple', 'banana']
test_list_for(list7)



# while 循环：

def test_list_while(list):
    i = 0
    while i < len(list):
        print(list[i])
        i += 1

test_list_while(list7)


my_module.print_line()


# 列表生成式：
# 列表推导式是一种创建列表的简洁方式，可以根据某种条件筛选出符合条件的元素，并将其放入新列表中。
# 语法：
# 新列表 = [表达式 for 变量 in 可迭代对象 if 条件]

# 一维列表
new_list = [x for x in range(10) if x % 2 == 0]
print(new_list)

# 实质：
def test_list_comprehension():
    for x in range(10):
        if x % 2 == 0:
            list = []
            list.append(x)
            print(list)


# 二维列表
new_list1 = [[col*row for col in range(5)]for row in range(5)] # [[内层循环]外层循环]
print(new_list1)

# 实质：
def test_list_comprehension1():
    for row in range(5):
        list = []
        for col in range(5):
            list.append(col*row)


# 访问列表元素（类似于数组）
print(new_list1[0])
print(new_list1[0][0])


# 二维转一维
new_list2 = [col for row in new_list1 for col in row] # [外层循环 内层循环]
print(new_list2)

# 实质：
def test_list_comprehension2():
    new_list = []
    for row in new_list1:
        for col in row:
            new_list.append(col)
    print(new_list)

test_list_comprehension2()


my_module.print_line()


# 列表的运算
a = [1, 2, 3]
b = [4, 5, 6]

# a=a+b这种非自增性质的赋值运算，创建一个新的列表来容纳拼接的结果，再让原来的变量a指向这个新的对象，并非在原列表的基础上进行操作，对原列表没有影响。
print(a,id(a))
print(a*2,id(a*2))
print(a+b, id(a+b))
print(a,id(a))

# 而a+=b这种自增性质的赋值运算，是在原列表的基础上进行操作。
a+=b
print(a,id(a))

# 列表对象自增的拼接函数也是在原列表的基础上进行操作。
a.extend(b)
print(a, id(a))





