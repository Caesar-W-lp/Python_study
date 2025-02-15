# 作者:李一安
# 2024年12月29日19时30分32秒
# 1713450722@qq.com


# work1

a = 10
print(type(a), a)

b = 3.14
print(type(b), b)

c = 'Caesar'
print(type(c), c)

print('-' * 50)


# work2

def change():
    x = 32

    # 二进制
    print(bin(x))

    # 八进制
    print(oct(x))

    # 十六进制
    print(hex(x))


change()

print('-' * 50)


# work3

def for_count():
    total = 0

    for i in range(1, 100):
        if i % 2 != 0:
            total = total + i

    print(total)


for_count()


def while_count():
    total = 0
    i = 1
    while i <= 100:
        if i % 2 != 0:
            total = total + i
        i = i + 1

    print(total)


while_count()

print('-' * 50)


# work4

def multiplication_table():
    for row in range(1,10):
        for col in range(1, row+1):
            print(f"{col} * {row} = {row * col}\t", end="")

        print("")


multiplication_table()

print('-' * 50)


# work5

# 第一种方法
# 由于整型是无穷大，所以以下的64位是题目对统计的一个限制

def binarization1():
    x = int(input("请输入一个十进制数: "))
    if x >= 0:
        # 此种情况下的二进制数补码与原码相同
        num = bin(x).count("1")

    else:
        # 负数的二进制数补码是将原码取反再加1
        # 而bin()得到的是：正数为原码，负数为负号加原码
        # 负数的原码取反+1得补码，补码再取反+1得原码，根据这个法则，先让原码-1再取反即得补码
        # 在python中，数据的符号和数值是分开存储的，故而数据部分的存储就是按照无符号数的存储方式
        num = 64-bin(-x-1).count("1")
        # num = 64-bin(~x).count("1")

    print(f"二进制数的补码中1的个数为：{num}")

binarization1()


# 第二种方法

def binarization2():
    '''
    按位运算的方法
    :return:
    '''
    x = int(input("请输入一个十进制数: "))

    flag = 1 # 设置游标

    count = 0 # 记录1的个数

    while flag < 2**64:
        if x & flag:
            count += 1
        flag <<= 1 # 左移游标

    print(f"二进制数的补码中1的个数为：{count}")


binarization2()

