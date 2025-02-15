# 作者:李一安
# 2025年02月01日07时17分29秒
# 1713450722@qq.com


# work1
def work1():
    # 使用异或运算符实现列表中元素的去重
    # 异或满足交换律
    list1 = [1, 1, 2, 2, 3, 4, 4]

    result = 0
    for i in list1:
        result ^= i

    print(f'work1:{result}')

    # 计算过程为：
    # 1 ^ 0 = 1
    # 1 ^ 1 = 0
    # 0 ^ 2 = 2
    # 2 ^ 2 = 0
    # 0 ^ 3 = 3
    # 3 ^ 4 = 7
    # 7 ^ 4 = 3


# work6
# 有8个整数，其中有3个数出现了两次，2个数出现了一次，找出出现了一次的那2个数。
def work6():
    '''
    有8个整数，其中有3个数出现了两次，2个数出现了一次，找出出现了一次的那2个数。
    思路：
    分而治之的思想。
    先分为两堆，再逐堆解决。
    关键就是怎么分，以及怎样解决。

    :return:
    '''

    list1 = [1, 2, 3, 2, 1, 5, 3, 7]

    result = 0
    for i in list1:
        result ^= i

    split_flag = result & -result
    # result & -result 这个公式可以找到result二进制位中最低位为1的那个值，即为分割点
    # 注意：python都是有符号数
    # 过程为：
    # result = 00000111 ^ 00000101 = 00000010 = 2
    # result & -result = 00000010 & 11111110 = 00000010 = 2

    list2 = []
    list3 = []
    for i in list1:
        if i & split_flag:
            list2.append(i)
            # 留下二进制第二位为1的数
        else:
            list3.append(i)
            # 留下二进制第二位不为1的数

    ret1 = 0
    for i in list2:
        ret1 ^= i

    ret2 = 0
    for i in list3:
        ret2 ^= i

    print(f'work2:{ret1, ret2}')



if __name__ == '__main__':
    work1()
    work6()