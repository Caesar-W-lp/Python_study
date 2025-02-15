# 作者:李一安
# 2025年02月11日14时57分00秒
# 1713450722@qq.com

# python中内置了文件管理操作的相关函数，封装在os包中
import os


# 以字节流形式复制图片文件

def copy_picture_file():
    # 生成文件对象
    file1 = open("file_7.jpg", "rb")
    file2 = open("file_7_1.jpg", "wb")

    # 读取文件内容
    file_bites = file1.read()

    # 写入新文件
    file2.write(file_bites)

    # 关闭文件
    file1.close()
    file2.close()


# 以字节流形式加密图片文件
def crypt_picture_file():
    # 生成文件对象
    file = open("file_7_1.jpg", "rb+")

    # 定位到文件开头偏移
    file.seek(3, os.SEEK_SET)

    # 读取文件内容
    file_bites = file.read(1) # 获取1个字节的内容
    print(f'原始字节：{file_bites}')

    # 加密操作
    # 字节取反
    inverted_b = bytes([~file_bites[0] & 0xff]) # 按位取反并限制在0-255范围内
    print('取反后：', inverted_b)

    # 重定位到原来的位置
    file.seek(3, os.SEEK_SET)

    #将加密的字节写回原文件
    file.write(inverted_b)


    # 关闭文件
    file.close()




if __name__ == '__main__':
    # copy_picture_file()
    crypt_picture_file()
