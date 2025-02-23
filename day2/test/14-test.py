# 作者:李一安
# 2024年12月29日16时01分02秒


# 位运算符
# python中全都是有符号数

def func():
    '''
    位运算符(参与位运算的是补码，得到的结果也是补码)
    :return:
    '''

    # 按位与
    print(5 & 7)
    '''
    0000 0101
    0000 0111
    
    0000 0101 5
    '''

    print('-' * 100)

    # 按位或
    print(5 | 7)
    '''
    0000 0101
    0000 0111

    0000 0111 7
    '''

    print('-' * 100)

    # 按位非
    print(~5)
    '''
    0000 0101
    
    1111 1010
    
    1000 0110 -6
    '''

    print('-' * 100)

    # 按位异或(同为0，异为1)
    print(5 ^ 7)
    '''
    0000 0101
    0000 0111
    
    0000 0010

    '''

    # 按位异或的特点
    # 和0按位异或为本身
    print(5 ^ 0)
    # 和自己按位异或为0
    print(5 ^ 5)

    print('-' * 100)

    # 移位运算符只能用于整数类型
    # 左移位运算(由于python中的整型大小无上限，故而左移位运算符并不会发生溢出，而是永久性乘2)
    print(1 << 2)
    print(-1 << 2)

    print('-' * 100)

    # 右移位运算符(右移位运算符则是抹去低位，正数高位补0，负数低位补1，减1再除2)
    print(3 >> 1)
    print(-3 >> 1)


func()
