# 作者:李一安
# 2025年02月14日22时23分46秒



import sys

def write_hello(file_path):
    file = open(file_path, 'w', encoding='utf-8')
    file.write('Hello, world!\n')
    file.close()


if __name__ == '__main__':
    print(type(sys.argv))
    print(sys.argv)

    write_hello(sys.argv[1])
    # 在终端传入：python .\11-传参.py file_11.txt
