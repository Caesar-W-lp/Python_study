# 作者:李一安
# 2025年02月26日10时52分32秒


# 正则表达式用于处理字符串

# .   匹配任意 1 个字符（除了\n）
# [ ] 匹配[ ]中列举的其中一个字符
# \d  匹配数字，即 0-9 decimal
# \D  匹配非数字，即不是数字
# \s  匹配空白，即 空格，tab 键 space
# \S  匹配非空白
# \w  匹配unicode字符，即 a-z、A-Z、0-9、_ (汉字) word ，命名规则字符集，大小写字母，数字，下划线
# \W  匹配非单词字符

# 在正则表达式中字母大小写匹配是敏感的


# 导入正则表达式的包
import re


def simple():
    """
    初识正则表达式
    :return:
    """
    # 使用match方法进行匹配
    # re.match(正则表达式, 要匹配的字符串)
    # match接口是默认从字符串的开始位置开始匹配，如果匹配成功，返回一个Match对象，就是匹配成功的结果，否则返回None
    # 其实就是用正则表达式去对照需要匹配的字符串，完全匹配成功则返回对照过的字符串
    result = re.match("wangdao", "wangdao.cn")
    if result:
        print(result.group()) # wangdao


def single():
    """
    匹配单个字符，注意，数字35是两个字符
    :return:
    """
    # 使用.匹配任何单个字符
    ret = re.match(".", "M")
    print(ret.group()) # M

    ret = re.match("t.o", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())
    print('-' * 50)


    # 大小写h都可以的情况
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())


    # 匹配0到9第二种写法
    ret = re.match("[0-9]Hello Python", "6Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "7Hello Python") # 这里不能为了美观写成[0-3 5-9]，里面所有的符号包括空格都会被视为参与匹配的字符
    print(ret.group())
    print('-' * 50)


    # 使用\d进行匹配，匹配单个数字
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())



# *     匹配前一个字符出现 0 次或者更多次，即可有可无。
# +     匹配前一个字符出现 1 次或者更多次，即至少有 1 次。
# ?     匹配前一个字符出现 1 次或者 0 次，即只会有 1 次或 0 次。若匹配到0次，则正则表达式中的扫描指针继续往后走，字符串中的扫描指针留在原位；且正则引擎一般都会统筹后面的字符串，[字符集]?是可选的，[字符集]是必须满足的，在字符串不够匹配的情况下，不论这两者的先后顺序，都会优先满足[字符集]
# {m}   匹配前一个字符出现 m 次，限定出现次数。若不够则返回 None，若更多则仅到 m 次，匹配过程中出现不在字符集中的字符返回 None
# {m,n} 匹配前一个字符出现从 m 到 n 次，限定出现次数。不够范围、超出范围、或在还没扫描至范围下限时就遇到不存在于字符集中的字符时，结果同上；但若在[m,n]范围内匹配过程中扫描到不在字符集中的字符，则停止并返回已经匹配的字符，否则就一直匹配至上限n次


def more_alp():
    """
    匹配多个字符
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    print('-' * 50)

    # 实例：匹配变量名
    # +的使用
    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        ret = re.match(r'[a-zA-Z_]+[\w]*', name) # 这里的+和*都是在正则表达式中起作用的符号，不会被算作用于匹配的字符
        if ret:
            print(f'{ret.group()} 是正确的')
        else:
            print(f'{name} 不符合命名规范')

    print('-' * 50)

    # 实例：匹配0-99之间的数字
    # ?的使用
    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

    print('-' * 50)

    # 实例：匹配6-20位的字符串，包含大小写字母、数字、下划线
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s*34455ff66")
    print(ret.group())




# 匹配开头结尾
# ^ 匹配字符串开头
# $ 匹配字符串结尾

def start_end():
    """
    匹配结尾
    :return:
    """
    # 符合163的邮箱找出来
    # $ 作用就是匹配完成后还会进一步考察字符串在匹配完成的位置后续是否还有内容，若没有则返回匹配成功的对象，若还有则返回None，从而做到限定结尾的作用
    # 确保匹配的字符串必须以正则表达式的内容结束
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r'[\w]{4,20}@163\.com$', email)  # 匹配的字符串中出现了正则的符号，要使用\进行转义
        if ret:
            print(f'{ret.group()}是正确的邮箱{email}') # 若不加$，则"xiaoWang@163.comheihei" 也会匹配成功，因为匹配指针在匹配完其中的m就结束了返回匹配成功的对象，不再管后续是否还有字符串
        else:
            print(f'{email}邮箱地址不正确')

    print('-' * 50)

    # 匹配0到99
    ret = re.match(r"[1-9]?\d$", "09")
    if ret:
        print(ret.group())
    else:
        print('不是0-99之间')







# 匹配分组
# |           匹配左右任意一个表达式
# (ab)        将括号中字符作为一个分组
# \num        引用分组 num 匹配到的字符串
# (?P<name>)  分组起别名
# (?P=name)   引用别名为 name 分组匹配到的字符串


def split_group():
    """
    匹配分组
    :return:
    """
    # 匹配0到100
    ret = re.match(r"[1-9]?\d$|100", "77")
    if ret:
        print(ret.group())
    else:
        print('不是0-100之间')


    # 匹配1到99,匹配分组，依次匹配，
    # 写到 | 前面的会先匹配
    ret = re.match(r"[1-9]$|[1-9][0-9]", "11")
    if ret:
        print(ret.group())
    else:
        print('不是1-99之间')

    print('-' * 50)


    # ()的使用
    # 限制 | 的作用域，其实就是使某一部分成为一个单独的子分组
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
    print(ret.group())
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
    print(ret.group())

    print('-' * 50)

    # [^-]中，^-的意思就是除了-外所有的字符，[]是建立字符集
    # ()的作用是创建捕获组（capture group）。捕获组的主要功能是：将正则表达式的一部分括起来，以便后续可以单独提取这部分匹配的内容。在正则匹配结果中可以通过 group() 方法获取捕获组的值。
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")# 代表没有遇到小横杠 - 就一直进行匹配，直到遇见
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

    print('-' * 50)


    # 能够完成对正确的字符串的匹配
    ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>")
    print(ret.group())

    # 这里的 \1 就是指代第一个分组
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    print(ret.group())

    print('-' * 50)

    # 多个引用分组就不建议使用，因为会导致混乱，建议使用别名
    # 多个引用分组的替代方法就是给分组起别名，然后在后续引用别名
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)

    print('-' * 50)

    for label in labels:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)





# re模块的高级用法

# 此函数用于sub的第二个参数，将匹配到的数字加100
# 传入的是匹配结果对象，还需要用group()方法获取匹配到的字符串
def add(x):
    result = x.group() # 获得的是匹配到的字符串
    print(result)
    return str(int(result) + 100)


# search findall sub split

def other_func():
    """
    search findall sub split
    :return:
    """
    # search 遍历字符串，匹配第一个匹配项，返回 Match 对象，如果没有匹配项，则返回 None
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())

    print('-' * 50)

    # findall 遍历字符串，匹配所有匹配项，返回一个字符串列表，如果没有匹配项，则返回空列表
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)

    print('-' * 50)


    # sub(正则表达式, 用于替换的子字符串, 要替换的字符串，替换次数)
    # 其实就是先遍历字符串，找到所有匹配的目标字符串，然后替换，返回替换后的字符串。
    # 第二个参数也可以是一个函数，函数的第一个参数是 Match 对象，再用函数的返回值进行替换。
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)

    print('-' * 50)

    # sub只替换前两个
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    # sub()的第四个参数是count，表示替换的次数，默认是全部替换
    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)



# pattern 就是正则表达式，text 就是要匹配的字符串
# 这里的 finditer 就是返回一个迭代器，可以遍历所有匹配项，每次迭代返回一个 Match 对象
def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    # 其实就是先用一次findall，再将匹配到的分节，每次仅取出一节
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


def use_finditer():
    """
    使用finditer
    :return:
    """
    # 示例用法
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)


def number_generator(start=0):
    while start <= 5:  # 无限循环，持续生成数字
        yield start  # 程序在这里暂停，start值被return回来
        start += 1



def use_generator():
    """
    使用生成器，理解next
    :return:
    """
    # # 示例使用
    gen = number_generator()  # 创建生成器实例，从0开始
    print(gen)

    # next 的作用是执行迭代器，并获取迭代器在当前位置的值，然后将迭代器指向下一个位置。
    print(next(gen))  # 输出 0
    print(next(gen))  # 输出 1
    print(next(gen))  # 输出 2

    # for循环后面可以是迭代器，也可以是生成器，for循环会自动调用next方法获取当前值
    for i in gen:
        print(i)


def use_findall():
    """

    :return:
    """
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时', r':', ret_s)
    ret_s = re.sub(r'分', r'', ret_s)
    print(ret_s)

    # findall 内部的设计机制存在问题，在使用时，如果有分组，则需要在分组前面加?:，否则只会作用于分组
    # 将常用的正则表达式封装起来方便使用
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)

    # search 没问题
    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret1 = pattern1.search(ret_s)
    print(ret1.group())



# 总练习
def use_sub():
    long_text = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """

    # print(long_text)

    # 数据清洗，将html标签、空格、换行符、制表符等替换为空
    ret=re.sub(r'<[^>]*>|&nbsp;|\n|\s','',long_text)
    print(ret)

def use_split():
    # 返回值是一个列表，包含分割后的字符串
    # 第二个参数可以指定分隔符，默认是空格
    # 第三个参数可以指定分割次数，默认是0，表示分割所有
    ret = re.split(r":| ","info:xiaoZhang 33 shandong")
    print(ret)

if __name__ == '__main__':
    # simple()
    # single()
    # more_alp()
    # start_end()
    # split_group()
    # other_func()
    # use_finditer()
    # use_generator()
    # use_findall()
    # use_sub()
     use_split()


# 额外：
# 转义字符中的\的作用是将后面的字符完全视为普通字符，而不是有特殊作用的符号