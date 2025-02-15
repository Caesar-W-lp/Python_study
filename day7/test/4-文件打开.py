# 作者:李一安
# 2025年02月10日15时41分24秒
# 1713450722@qq.com

# 位置指针 与 访问模式

# 读模式：
# 若目标文件存在，从头开始读，指针在开头。
# 若目标文件不存在，抛出异常。
# read()操作在哪儿结束，位置指针就停在哪儿

def read_file():

    # open(文件名, 访问模式, 编码方式)
    file = open('file_4.txt', mode='r', encoding='utf-8')
    text = file.read() # 返回一个字符串对象
    print(text)

    file.close() # 关闭文件
    # 文件的任何操作和关闭是配套操作，必须有关闭操作，否则会造成资源泄露。



# 写模式：w，
# 如果文件不存在，新建目标文件并从头写入，
# 如果文件存在就清空文件，指针重置于开头。

def write_file():
    # file_4.txt 文件存在，清空文件，重置位置指针
    file = open('file_4.txt', mode='w', encoding='utf-8')
    file.write('maybe')

    # file_4_1.txt 文件不存在，会自动创建
    file = open('file_4_1.txt', mode='w', encoding='utf-8')
    file.write('hello')


    file.close()


# 读写模式
# 若文件存在，则仅重置指针于开头，当需要写入时，则从指针处写，原有内容会被覆盖
# 若文件不存在，则抛出异常

def read_write_file():
    file = open('file_4.txt', mode='r+', encoding='utf-8') # 重置指针于开头

    text = file.read() # 读至结束，指针停在最后一个字符后
    print(text)

    file.write('lyan\n') # 写操作会将指针致末，在本例中这一步指针位置并不变，依然在最后一个字符后

    text = file.read() # 从最后一个字符后开始读，但后面并没有东西，返回空字符串
    print(text)

    file.close()


# 追加模式
# 若文件已存在，则将指针放置于文本末尾。
# 若不存在，则新建目标文件
# a模式只能写，a+模式既能读又能写。
def add_file():
    file = open('file_4.txt', mode='a', encoding='utf-8')

    file.write('hello')




if __name__ == '__main__':
    # read_file()
    # write_file()
    # read_write_file()
    add_file()


# 总结：
# 对于r及其附加模式r+
# 只要目标文件存在，则位置指针都在开头
# 如果目标文件不存在，都会报错

# 对于w，无论文件是否存在，都是干干净净且位置指针在开头

# 对于a和a+
# 只要目标文件存在，则位置指针都在文本末尾
# 如果目标文件不在，则新建文件

# 对于read()，无论位置指针在哪，都是从位置指针处开始读至文本末尾，无论后续有无文本，无则返回空字符串
# 对于write()，无论位置指针在哪，都是从位置指针处开始写，无论此时是否已有文本，有则覆盖