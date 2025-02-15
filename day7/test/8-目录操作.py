# 作者:李一安
# 2025年02月11日18时23分52秒
# 1713450722@qq.com

# python中内置了文件管理操作的相关函数，封装在os包中
# 目录即文件夹
import os

def use_rename():
    # 重命名文件
    # os.rename('file_test.txt', 'file_8.txt')

    # 也可以使用绝对路径
    # 但极有可能发生转义字符错误
    # os.rename('F:\\jetbrains\\pycharm\\2024wangdao\\day7\\test\\file_8.txt', 'file_8_1.txt')

    # 也可以使用相对路径
    # .是代表当前目录，.\\一般都是配套使用
    os.rename('.\\file_8_1.txt', '.\\file_8.txt')



def use_dir_func():
    # 获取当前目录下的文件列表（包括隐藏文件）
    file_list = os.listdir('.') # 返回一个列表
    print(file_list)

    #创建目录
    os.mkdir('test_dir1')
    os.mkdir('test_dir2')

    # 删除空目录，目录必须为空，否则会报错
    os.rmdir('test_dir2')

    # 获得当前目录的绝对路径
    print(os.getcwd())

    # 改变操作目录
    # 父进程的工作目录不会改变，子进程的工作目录会改变
    os.chdir("8_test")
    file = open('test.txt', 'w', encoding='utf-8')
    file.write('改变操作目录')
    file.close()

    # 判断当前所在是否是目录
    os.path.isdir('8_test') # 是目录返回True，否则返回False


if __name__ == '__main__':
    # use_rename()
    use_dir_func()