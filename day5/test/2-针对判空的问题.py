# 作者:李一安
# 2025年02月02日14时55分07秒



def func1():
    if []:
        print("非空列表")
    else:
        print("空列表")

    print("-"*50)

    if ():
        print("非空元组")
    else:
        print("空元组")

    print("-" * 50)

    if {}:
        print("非空字典")
    else:
        print("空字典")

    print("-" * 50)

    if "":
        print("非空字符串")
    else:
        print("空字符串")

    print("-" * 50)


    empty_set = set()
    if empty_set:
        print("非空集合")
    else:
        print("空集合")


if __name__ == '__main__':

    # 空的容器作为一个对象，此对象的返回值是布尔值False，就是数值0，而不是None。
    # 但是空容器这个对象并不是布尔值对象False，即[] ！= False。
    func1()