# 作者:李一安
# 2025年01月05日20时43分52秒
# 1713450722@qq.com

# 全局变量的使用

# import的作用其实就是把另一个模块里的代码导入到当前模块中，这样就可以直接使用模块里的函数、类等。
# 故而若被导入的模块中有全局变量且不加以限制，则这些全局变量也会被导入到当前模块中。
# 并且被导入的模块中的行为（打印输出）若不加以限制，也会在当前模块中执行。
# 为了加以限制，引入了if __name__ == '__main__':的使用


# 对于if __name__ == '__main__':
# python中每个模块在运行时会有一个隐含的变量__name__用于记录当前模块的运行状态，
# 当该模块作为主模块运行时，__name__的值为'__main__'，
# 当该模块被通过导入到其他模块来运行时，__name__的值为自己这个模块的模块名。

# 因此，对于if __name__ == '__main__':后的语句只有当本模块作为主模块来运行时才会执行，
# 而当本模块被导入到其他模块中时，if __name__ == '__main__':后的语句不会被执行。


def print_line(char, times):
    print(char * times)


def main():
    a = '*'
    times = 50


if __name__ == '__main__':
    main()
