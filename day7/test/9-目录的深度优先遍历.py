# 作者:李一安
# 2025年02月12日22时02分58秒
# 1713450722@qq.com

import os

# 目录深度优先遍历
def scan_dir(current_path, width):

    # 获得当前目录下所有文件和目录
    file_list = os.listdir(current_path)

    # 遍历当前文件夹里的所有文件
    for file in file_list:
        # 输出文件名
        print(" " * width, file)

        # 判断文件是否为文件夹
        new_path = current_path + "/" + file  # 把当前路径和文件名拼接起来
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)



if __name__ == '__main__':
    scan_dir(".", 0)



