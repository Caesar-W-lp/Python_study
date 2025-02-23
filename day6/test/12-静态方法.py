# 作者:李一安
# 2025年02月08日16时46分21秒



# 当要在类中封装一个方法
# 此方法既不访问实例属性和调用实例方法，也不访问类属性和调用类方法
# 则此方法可以写为静态方法

class Tool:

    @staticmethod
    def help():
        print("这是一个工具类")


if __name__ == '__main__':
    Tool.help()
    # 通过 类名.静态方法名 来调用静态方法，并不需要实例化