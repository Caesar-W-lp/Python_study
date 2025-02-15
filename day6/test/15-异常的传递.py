# 作者:李一安
# 2025年02月09日15时38分51秒
# 1713450722@qq.com


# 异常的传递
# 1. 异常的传递是指在嵌套函数中，如果内层函数发生异常，会在发生异常的位置停下并向上层抛出异常，并被上层函数捕获。



def demo1():

    num1 = int(input("请输入一个数字："))
    print(num1)

    return num1

def demo2():
    num2 = demo1()
    print(num2)

    return num2


def function():
    try:
        print(demo2())
    except Exception as e:
        print("发生异常")
        print(f"异常信息：{e}")

    finally:
        print("程序结束")


if __name__ == '__main__':
    function()

