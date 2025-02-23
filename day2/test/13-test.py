# 作者:李一安
# 2024年12月29日15时44分47秒


# 逻辑运算符（and、or、not，与C语言不同的是，not与前两个运算符的优先级是一样的，在C语言中否的优先级很高）

def logic():
    '''
    使用逻辑运算符
    :return:
    '''

    # and运算符的结果为假则返回False，为真则返回后一个值(原因就是短路运算，无论什么情况且的短路会算到最后一个值)
    print(0 and 1)
    print(1 and 0)
    print(1 and 2)
    print(2 and 1)

    print('-'*100)

    # or运算符的结果为假则返回False，为真则返回前一个值(原因就是短路运算，若第一个值为真，或的短路只会算到前一个值)
    print(0 or 0)
    print(1 or 2)
    print(2 or 1)

logic()