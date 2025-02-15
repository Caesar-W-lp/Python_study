# 作者:李一安
# 2025年02月10日21时04分53秒
# 1713450722@qq.com


# seek()方法用于重置位置指针
# seek(offset, whence)
# 参数offset：表示偏移量，即相对于whence的位置
# 参数whence：表示偏移量的参考位置，0文件开头(SEEK_SET)，1当前位置(SEEK_CUR)，2文件末尾(SEEK_END)（最后一个字节再后一位）
# 文本模式下，seek相对于开头进行偏移时，相对偏移量只能为非负数；相对于当前和结尾进行偏移时，相对偏移量只能为0
# 文本模式下只能向后偏移，不能向前偏移；二进制模式下，seek可以向前或向后偏移。

def seek_test1():

    file = open("file_6.txt", "r+", encoding="utf-8")

    text = file.read(5) #读操作结束以后，位置指针位于第6个字节
    #read()方法默认读取全部内容，但也可在()内指定读取字节数，一个字母或数字1字节，一个汉字3字节
    print(text)

    print("-"*50)

    print("相对于开头进行偏移")
    file.seek(1, 0) # 重置位置指针，使其位于第二个字节
    text = file.read(5) # 此操作结束后，位置指针位于第7个字节
    print(text)

    print("-"*50)

    print("相对于结尾进行偏移")
    # 文本模式下，seek相对于结尾进行偏移时，相对位移量（第一个参数）只能为0
    file.seek(0, 2)  # 重置位置指针，使其位于最后一个字节再后一位
    text = file.read() # 返回空字符串
    print(text)

    file.close()




def seek_test2():

    # 二进制模式
    # 二进制模式下，打开文件时不需要使用编码参数，但需要使用b前缀，如rb+
    # 二进制模式下产生的是字节流对象，所以一般用于图片、视频、音频等字节流形式数据的处理
    file = open("file_6.txt", "rb+") # 位置指针位于文件开头
    bites = file.read()
    print(bites)

    print("-"*50)

    # 字节流模式下的seek()方法

    #相对于开头位置进行偏移
    print("相对于开头位置进行偏移")
    file.seek(3, 0) # 从开头偏移了3个字节，位置指针位于第4个字节起始处
    bites = file.read(6) # 读取6个字节，位置指针位于第10个字节起始处
    print(bites)

    print("-" * 50)

    # 相对于当前位置进行偏移
    # 二进制模式下，seek相对于当前位置进行偏移时，相对位移量可以为正数、负数、0
    print("相对于当前位置进行偏移")
    file.seek(-3, 1) # 相对于当前位置向前偏移3个字节，位置指针位于第7个字节起始处
    bites = file.read(6) # 读取6个字节，位置指针位于第13个字节起始处
    print(bites)

    print("-" * 50)

    # 相对于结尾位置进行偏移
    # 二进制模式下，seek相对于结尾位置进行偏移时，相对位移量可以为负数、0
    print("相对于结尾位置进行偏移")
    file.seek(-12, 2)  # 相对于当前位置向前偏移3个字节，位置指针位于第7个字节起始处
    bites = file.read()  # 全部读取，位置指针位于文件末尾
    print(bites)


    file.close()


if __name__ == '__main__':
    # seek_test1()

    seek_test2()



# 注意：
# seek的计算是按照字节来的
# python中一个汉子占3个字节
# 所以要在字符串为汉字的情况下做位置指针的偏移，偏移量需要是3的倍数

