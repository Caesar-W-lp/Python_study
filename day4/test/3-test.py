# 作者:李一安
# 2025年01月14日17时10分20秒


import module

# 字符串
# 将其视作一个对象来学习它的接口
# 不同于可变数据类型，字符串是不可变的，对字符串的操作可能会返回一个新的字符串，即会创建一个新的字符串对象，返回一个新的堆空间地址。
# 字符串是一个有序容器，那么它就有索引
# 所以字符串拥有不可变数据类型和容器的双重性质

def test_string():
    # 字符串的创建
    str1 = "hello world"
    print(str1)

    module.line()

    # 字符串的遍历
    for char in str1:
        print(char)

    module.line()

    # 字符串的索引
    print(str1[0])

    module.line()

    # 字符串长度
    print(len(str1))

    module.line()


    # 获得字符第一次出现的索引
    print(str1.index("l"))



test_string()


module.line()


# 常用字符串接口

# 查找子字符串
def string_find():
    str1 = "abcdbcd"
    ret = str1.find("bcd", 1, 4) # 从索引[1,4]闭区间内查找bcd首次出现位置的首索引
    print(ret, type(ret))

string_find()


module.line()


# 替换子字符串
def string_replace():
    str1 = "abcabcdefg"
    ret1 = str1.replace("abc", "123", 1) # 替换前1次出现的abc为123
    print(ret1)

    ret2 = str1.replace("abc", "123", 2) # 替换前2次出现的abc为123
    print(ret2)


string_replace()


module.line()


# 大小写变换
def string_upper():
    str1 = "abcabcdefg"
    ret1 = str1.upper()
    print(ret1)


string_upper()


module.line()


# 翻转大小写
def string_change_alpha():
    str1 = "abcABCdefg"
    ret1 = str1.swapcase()
    print(ret1)


string_change_alpha()


module.line()


#字符串的拆分

def string_split():
    str1 = "a b c d e f g 李 一 安"
    ret1 = str1.split() # 默认按照空格分割
    print(ret1)

    module.line()

    # 可指定分隔符
    str2 = "a,b,c,d,e"
    ret2 = str2.split(",")
    print(ret2)

    module.line()

    # 可指定最大分割次数
    str3 = "a,b,c,d,e,f,g,h"
    ret3 = str3.split(",", 2)
    print(ret3)

    module.line()

    # 默认分割符为空白字符的专用接口
    # \r是光标回到本行初始位置，并覆盖原有字符
    # \n是光标回到下一行行首，并在下一行插入新字符
    # \r\n是光标回到下一行行首，并在下一行插入新字符,是一个换行符组合，也就是说这两个转义字符是一体的
    # \n\r并不是换行符组合，是两个独立的换行符
    str4 = "ab\r\nb\n\rc\nd\ne"
    print(str4)

    module.line()

    ret4 = str4.splitlines()
    print(ret4)

    module.line()

    str5 = "ab\r\nb\nc\nd\ne"
    ret5 = str5.splitlines(True)
    print(ret5)


string_split()


module.line()


# 字符串的连接

def string_join():
    str1 = ["a", "b", "c", "d", "e"]
    ret1 = ",".join(str1)
    print(ret1)

    module.line()

    str2 = ["a", "b", "c", "d", "e"]
    ret2 = "".join(str2)
    print(ret2)

string_join()


module.line()


# 字符串切片
# 切片语法：str[start:end:step]
# start: 切片开始的索引，默认为0
# end: 切片结束的索引，默认为字符串长度，最后一个字符的索引+1
# 对[star, end)索引区间（也就是[start, end-1]）内的字符串进行切片
# start和end可以为负数，表示从字符串末尾开始计数的索引，-1表示倒数第一个字符，-2表示倒数第二个字符，以此类推
# step: 切片步长，默认为1
# step可以为负数，表示反向切片



def string_slice():
    str1 = "0123456789"
    ret1 = str1[0:5]
    print(ret1)

    module.line()

    ret2 = str1[:]
    print(ret2)

    module.line()

    ret3 = str1[::2] # 切片索引02468
    print(ret3)

    module.line()

    ret4 = str1[1::2] # 切片索引13579
    print(ret4)


string_slice()


module.line()



