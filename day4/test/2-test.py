# 作者:李一安
# 2025年01月07日15时39分17秒

import module


# 字典
# 仅次于列表使用频率
# 是一种无序集合,它的索引是自定义的，其中的元素是键值对字典是一种映射类型，它存储的是键值对。
# 字典的每个键值对用冒号分隔，每个键值对之间用逗号分隔。
# 在字典（dictionary）中，键（key）是唯一的，但值（value）可以重复。每个键只能对应一个值，但不同的键可以对应相同的值。
# 字典是一种可变容器，且可以随时增删
# 字典的键必须是不可变类型(基本数据类型)，一般都是字符串。
# 字典的值可以是任意类型。
# {key1:value1, key2:value2, key3:value3...}


def dict_basic():

    print("字典基本操作")

    # 创建字典

    Wlp = {'name': 'Wlp', 'age': 25, 'city': 'Beijing'}

    print(Wlp)

    module.line()

    # 针对字典对象整体的基本操作

    # 根据索引打印元素
    print(f"Wlp['name']: {Wlp['name']}")

    module.line()

    # 获得所有key列表
    print(f"所有key列表：{Wlp.keys()}")

    module.line()

    # 获得所有value列表
    print(f"所有value列表：{Wlp.values()}")

    module.line()

    # 获得所有(key, value)元组列表
    # 将键值对转换为元组，再将元组作为列表元素，输出列表
    print(f"所有(key, value)元组列表：{Wlp.items()}")

    module.line()

    # 合并字典
    # 格式：dict1.update(dict2)
    # 是将dict2追加到dict1的尾部，如果有相同的键，则后面的键值对会覆盖前面的键值对。
    # 注意：字典的合并是不支持通过自增运算符+=来实现的。

    size = {'high': 175, 'weight': 60, 'age': 24}

    print(id(Wlp), id(size))

    Wlp.update(size)

    print(id(Wlp), id(size))

    print(Wlp)

    module.line()

    # 清空字典
    # 格式：dict.clear()
    # 清空字典中的所有元素，但字典本身依然存在。

    Wlp.clear()

    print(id(Wlp), Wlp)

    module.line()

    # 遍历字典，空表无法遍历
    # 按照key遍历字典

    for key in size:
        print(key,size[key])

    # 按照键值对遍历字典
    for kv in size.items():
        print(kv)

dict_basic()


module.line()


# 针对字典内元素对象的基本操作


#增删改查

# 增

def dict_add():

    print("增加字典元素")

    dict = {'name': 'Wlp', 'age': 25, 'city': 'Beijing'}

    # 增加键值对
    dict['high'] = 175
    print(dict)


dict_add()


module.line()


# 删

def dict_delete():

    print("删除字典元素")


    dict = {'name': 'Wlp', 'age': 25, 'city': 'Beijing'}

    # 删除键值对
    del dict['age'] # 错误的索引会报错
    print(dict)

    dict.pop('city') # 错误的索引会报错
    print(dict)


dict_delete()


module.line()


# 改

def dict_edit():

    print("修改字典元素")

    dict = {'name': 'Wlp', 'age': 25, 'city': 'Beijing'}

    # 修改键值对
    dict['age'] = 24
    print(dict)


dict_edit()


module.line()


# 查

def dict_search():

    print("查询字典元素")

    dict = {'name': 'Wlp', 'age': 25, 'city': 'Beijing'}

    # 根据键（索引）来查值
    # 字典[key]
    print(dict['name'])
    # print(dect['high']) # 使用不存在的key会报错

    module.line()

    # 字典.get(key, default=None)
    print(dict.get('high')) # 使用不存在的key时返回None，或者指定默认值


    # 根据值来查键


dict_search()


module.line()


# 列表嵌套字典

def list_dict():
    print("列表嵌套字典")
    list =[
        {'name': 'Wlp', 'age': 25, 'city': 'Beijing'},
        {'name': 'Tom', 'age': 26, 'city': 'Shanghai'}
    ]

    for card in list:
        print(card) # 这里的card就是字典对象



module.line()


