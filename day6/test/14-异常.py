# 作者:李一安
# 2025年02月08日20时50分41秒
# 1713450722@qq.com

# 异常
# try的代码块中是试行代码，如果试行代码产生任何异常，就会停在发生异常的那一步并转而进入except代码块，
# try代码块中异常后续的正常代码并不会继续执行；
# 若一切正常则不会执行except代码块


def function1():
    num = 0

    try:
        num = int(input("输入一个数字："))
        print(num)

    except:
        print("请输入正确的数字")

    print(num)


# 异常种类
# 对异常的分类识别有点像C语言中的switch case

def function2():
    num = 0

    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)

    except ValueError:
        print("请输入正确的整数")

    except ZeroDivisionError:
        print("除0异常")

    print(num)


# 对未知异常的捕获
def function3():
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)

    # 用Exception内置类将所产生的异常封装为一个实例对象
    # e就是异常日志
    except Exception as e:
        print(e)
        # 输出异常发生的位置
        print("异常发生的行数：", e.__traceback__.tb_lineno)
        # 输出异常发生的所在文件
        print("异常发生的文件：", e.__traceback__.tb_frame.f_globals["__file__"])


    # else 代码块在try代码块没有发生异常时执行
    else:
        print("正常执行")
        return 0


    # finally 代码块无论是否发生异常都会执行
    # 即使在try代码块中使用了return语句，finally代码块也会被执行
    finally:
        print("程序结束")


if __name__ == '__main__':
    # function1()
    # function2()
    function3()
