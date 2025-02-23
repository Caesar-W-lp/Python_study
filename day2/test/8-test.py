# 作者:李一安
# 2024年12月28日12时13分06秒


# 字符串研究

str1 = 'a'

print(type(str1))

str2 = 'abc'

print(type(str2))

# 在python语言中，是不具有字符类型的，只有字符串，无论是单个字符还是多个字符，无论是用单引号还是双引号括起来的，都是字符串

str3 = "'abc'"
print(type(str3),str3)

str4 = '"abc"'
print(type(str4),str4)

# 设计字符串既可以用单引号也可以用双引号括起来的原因是考虑到字符串内会出现单引号和双引号的情况

str5 = "\"abc\""
print(type(str5),str5)

str6 = '\'abc\''
print(type(str6),str6)

#若出现单引号和双引号内有相同引号的字符串时，作为字符串部分的引号需要使用转义字符

print(ord('0'))

# ord()这个函数用于返回单个字符的字符串的ASCII码值

print(chr(48))

# chr()这个函数用于返回ASCII码所对应的单个字符的字符串

# print('a'+1)

# 不同于在C语言中，字符串数据类型并不能与整型进行加减运算，即使是说单个字符是具有ASCII码值的，因为python中的运算的实质就是对象间的运算

print('-'*50)

# 可以进行乘法运算，结果就是字符重复了多少次