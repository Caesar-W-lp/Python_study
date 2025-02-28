# 作者:李一安
# 2025年01月05日12时11分26秒


# 全局变量与局部变量


# 局部变量：
# 在函数内部定义的变量，只能在函数内部使用，函数执行完毕后，变量会被销毁
# 由于局部变量之在所在函数内部起作用，故而不同函数的局部变量名称可以相同，不会互相影响


# 全局变量：
# 在函数外部定义的变量，所有函数都可以使用这个变量
# 在函数内部修改全局变量的值时，需要在变量名前加上global关键字，表示这个变量是一个全局变量，否则会被认为是局部变量
# 全局变量仅在当前的模块内有效，不同模块的全局变量名称可以相同，不会互相影响
# 若要使用另一个模块的全局变量，需要导入这个模块，然后使用模块名.变量名来访问
# 若要在函数中使用全局变量，则全局变量可以声明在函数调用前的任何位置，甚至可以在函数声明以后，但规格一般都放在最前面（import之后）
# 全局变量不建议大量使用，它的作用域太大，容易造成命名冲突，而且容易造成难以追踪的错误。


# 引用计数
# 引用计数是一种内存管理技术，它是一种通过跟踪每个对象的被引用次数来判断是否可以回收内存的技术。
# 当一个对象被创建时，它的引用计数被初始化为1。当一个对象被引用时，它的引用计数加1；当一个对象不再被引用时，它的引用计数减1。
# 当一个对象的引用计数变为0时，说明没有任何变量引用它，可以将其回收。
# Python使用引用计数来管理内存，当一个对象没有被引用时，Python会自动回收它。
# 即当没有任何变量指向堆内存中的对象时，Python才会自动回收这个对象。


# 示例：

num1 = 10
num2 = 20

def test():
    num1 = 1

    global num2
    num2 = 2

    print(num1, id(num1), num2, id(num2))


print(num1, id(num1), num2, id(num2))

test() # 函数执行时，内部的num会被视作局部变量，即覆盖了全局变量的使用

print(num1, id(num1), num2, id(num2))

# 根本原因就是：
# 解释器会查找函数内部是否有存在与全局变量重名的局部变量
# 若存在，则会将函数内的这个重名变量视作局部变量来使用，而屏蔽掉全局变量
# 这种情况下，全局变量和局部变量虽然同名，但却在栈内存拥有不同的变量地址，并且指向不同的堆内存中的对象。

# 若不存在，才会将其视作全局变量来使用

# 如果要在函数内同时使用重名的全局变量和局部变量，则需要在函数内使用global关键字来声明全局变量
# 这种情况下，函数内部若修改了全局变量的值，则会影响到全局变量的值，
# 根据引用计数的原理，全局变量会变化所指向的堆内存中的对象，若原来的对象不再被引用，则会被回收。

