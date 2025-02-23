# 作者:李一安
# 2024年12月30日20时17分10秒


import my_module

# 函数

# 函数需要先声明再使用

def my_func():
    print("Hello, world!")

print("执行前")

my_func()

print("执行后")

# 以上的函数是不带返回值的，其返回值默认为None，在python中，None表示空对象，区别与C语言中的NULL，C语言中NULL表示空指针，而None表示空对象。

ret = my_func()
print(ret)  # None



my_module.print_line()


# 带参函数与带返回值的函数
# 注意形参和实参
# 形参就算函数内的局部变量，仅在函数内有效

def add_num(x, y):
    s = x + y
    return s

print(add_num(10, 20))