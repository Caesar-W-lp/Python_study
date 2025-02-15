# 作者:李一安
# 2025年02月09日16时05分49秒
# 1713450722@qq.com


def input_password1():
    # 输入密码
    password = input("请输入密码：")

    # 判断密码长度
    if len(password) >= 8:
        return password

    # raise 的作用就是自定义一个异常，并抛出一个异常
    # 自定义异常用于处理自己不想要的结果，即使这个结果在语法上是正确的，但是与自己的逻辑需求不符
    # 自定义异常比if else语句更加灵活和方便
    # 括号()里就是自定义的异常信息

    # 产生异常
    # 这里用异常类Exception实例化了一个异常对象ex
    ex = Exception("密码长度必须大于等于8位")

    # 抛出异常
    # 异常必须要抛出才能被捕获，否则此异常将被Python解释器忽略
    # try-except语句就是用来捕获异常的
    raise ex


def input_password2():
    # 输入密码
    password = input("请输入密码：")

    # assert 用于判断一个表达式，如果表达式为False，则抛出一个AssertionError异常
    # 整合了判断、生成异常、抛出异常这一系列操作，使代码更加简洁
    assert len(password) >= 8, "密码长度必须大于等于8位"


if __name__ == '__main__':

    print(input_password1())

#    try:
#        print(input_password1())
#
#    except Exception as e:
#            print(e)

    try:
        print(input_password2())

    except Exception as e:
            print(e)