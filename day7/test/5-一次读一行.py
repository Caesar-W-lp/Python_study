# 作者:李一安
# 2025年02月10日20时21分10秒
# 1713450722@qq.com

def use_readline():

    file = open("file_5.txt", "r", encoding="utf-8")

    while True:
        file_line = file.readline() # 一次读一行，包含末尾的换行符

        if not file_line:
            print("\n文件已读完")
            break

        else:
            print(file_line, end="")

    file.close()



if __name__ == '__main__':
    use_readline()
