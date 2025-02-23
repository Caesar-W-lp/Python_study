# 作者:李一安
# 2024年12月29日21时35分10秒


# 循环语句
# python中有两种循环语句：for和while，没有do-while。

# while循环的语法格式：

# 循环变量
# while 条件表达式:
    # 语句块
    # 循环变量的更新

def test_while():
    i = 1
    while i <= 10:

        # 这里的f是指格式化字符串，可以用{ }括起变量，然后用.format()方法替换成变量的值
        print(f"i = {i}")

        # python没有i++或i--的操作符，只能用+=1或-=1
        i += 1

test_while()
