# 作者:李一安
# 2024年12月30日20时48分36秒
# 1713450722@qq.com

# 模块
# 一个py文件就是一个模块，可以被其他模块导入使用。
# 导入模块的语法格式如下：
# import 模块名

# 多个模块(多个py文件)放在同一个文件夹里，这个w文件夹可以被称为包(package)。
# 导入包的语法格式如下：
# from 包名 import 模块名

# python解释器自带了很多模块，可以直接使用，但自定义的模块不能与系统自带的模块重名，否则会覆盖系统模块。


# 在模块中可以定义全局变量，也可以通过global关键字声明全局变量。
# 定义全局变量的语法格式如下：
# global 变量名
# 示例：
# 在模块中定义全局变量a，并赋值为10。
# global a
# a = 10
# 全局变量的定义和赋值必须在模块的最开始处，且分开进行。


def print_line():
    print('-' * 50)



