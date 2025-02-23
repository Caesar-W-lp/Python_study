# 作者:李一安
# 2025年02月15日12时48分34秒


# eval()函数的作用是将字符串当作有效的表达式来执行，并返回结果。


def read_config(config_file):
    '''
    读取配置文件
    :param config_file:
    :return:
    '''
    text = open(config_file, 'r+', encoding='utf-8')
    text_content = text.read()

    print(type(text_content))# 无论文件的内容是什么格式，读取操作产生的都是字符串

    print(text_content)

    change_text_content = eval(text_content)

    print(type(change_text_content))

    print(change_text_content)

    text.close()


if __name__ == '__main__':
    read_config('file_12')