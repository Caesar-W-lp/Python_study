# 作者:李一安
# 2024年12月27日20时00分39秒


# 变量类型

a = 1
b = 1

print(id(a), id(b))
# 也就是说两者的地址是一样的
# 有点像C语言中堆内存中存储的数据一样，实际的数据存储在堆内存中，堆内存中的每一个数据都是唯一存在，不会重复出现，数据在堆内存中的地址存放在栈内存的变量中

a = 2

print(id(a))
# id()就是用于获取对象的唯一标识符，在python中，id()函数返回对象实际值在堆内存地址，而不是在栈内存中存放堆内存地址的变量的地址。

# python中所有的变量其实质都像上面所说的是一个引用（指针），其实就是一个指向真实数据的地址

# 而为什么又要研究python的数据类型呢？因为python里变量指向的实际数据可以根据运算规则分为数字型（整型、浮点型、布尔型）和非数字型

# bool型：True：实际数据为1的整型，但所有的非0整型（包括负数）都可以起到True的作用；False：真实数据为0的整型。

# 在python中，整型型变量是不会溢出的，即大小无上限（根本原因是会自动扩容）,因此没有long和long long；但浮点数是有上限的，精度为17位（整数部分数字个数+小数点+小数部分数字个数），和C语言中的double相同


# 在python中，所有变量都是对象，即不单纯是一个数值，而是一个含有内部结构的系统，它的返回值就是真实数值在堆内存中的地址，在堆内存中的真实数值才是一个单纯的值。


# 数据的唯一性：堆内存中的对象是唯一的，但并不是说堆内存中的每一个数据都是唯一存在的。
# 实际上，可以创建多个相同的对象，它们在堆内存中有不同的地址。
# 例如，两个不同的列表对象在堆内存中有不同的地址，但它们可以包含相同的元素。
#
# 变量实际上是对象的引用，它们指向堆内存中对象的实际位置。
# 在Python中，这些引用通常被称为“对象的引用”或“指针”，它们存储在局部变量表中，而局部变量表是每个函数调用的栈帧的一部分。
#
# 变量和引用：在Python中，变量实际上是对对象的引用。
# 当一个变量被赋值给另一个变量时，它们都指向堆内存中的同一个对象。这意味着它们共享同一个地址，而不是每个变量都有自己的地址。
