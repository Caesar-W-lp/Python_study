# 作者:李一安
# 2025年02月13日17时22分22秒


import os
import sys
from time import gmtime, strftime


def get_file_size(file_path):
    # 获取文件的信息
    file_infor = os.stat(file_path)

    # 分别获取文件大小，用户ID，文件权限，文件最后修改时间
    print(f'size：[{file_infor.st_size}],'
          f'uid：[{file_infor.st_uid}],'
          f'mode：[{file_infor.st_mode}],'
          f'mtime：[{file_infor.st_mtime}]')



    # 把秒数转为字符串时间
    # 格式化时间
    # gmtime()函数将时间戳转换为格林威治时间
    gm_time = gmtime(file_infor.st_mtime) # 返回一个对象，包含了年月日时分秒
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


if __name__ == '__main__':
    get_file_size("model.py")