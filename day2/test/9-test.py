# 作者:李一安
# 2024年12月28日12时36分04秒


# 读取标准输入

a = input('请输入：')
print(a)
print(type(a))

# 通过标准输入得到的所有数据全是字符串类型，后续若要作为其他类型数据来使用需要类型转换

num1 = int(a)
print(type(num1),num1)

num2 = float(a)
print(type(num2),num2 )


print('-'*100)

# 由于字符串与数字之间不能直接计算，故而需要先将字符串转换为数字再进行计算，计算结果再返回为字符串

b = input('请输入字母，自动转化为大写字母:')

print(type(b),b)

num_b = ord(b)

num_b = num_b - 32

b = chr(num_b)

print(type(b),b)


print('-'*100)


# 可以将以上转换字母大小写的代码封装为一个函数

def change1():
    b = input('请输入字母，自动转化为大写字母:')

    print(type(b), b)

    num_b = ord(b)

    num_b = num_b - 32

    b = chr(num_b)

    print(type(b), b)


change1()


print('-'*100)


# 以下是将输入的数字转化为数字型再进行运算，而非转化为ASCII码值再进行计算
def change2():
    a = input('输入一个数：')

    num = int(a)

    print(num)

change2()

# 浮点型是可以转整型的，但浮点数字符串是无法通过类型转化函数来转化为整型的，只能先转为浮点型，再以浮点型的身份做后续操作
# 但是整型字符串是可以直接转为浮点型的