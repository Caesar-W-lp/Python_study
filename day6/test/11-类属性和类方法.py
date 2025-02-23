# 作者:李一安
# 2025年02月07日18时44分08秒




class Tool:
    # 类属性
    count = 0  # 类属性，所有实例共享，类似于类中的全局变量
    # 类属性是随着类的定义而创建的。在实例化之前，类属性就已经分配了内存。

    # 这个方法是定义对象属性
    # 实例属性只有在创建实例后才会分配内存
    def __init__(self, name):
        self.name = name
        Tool.count += 1


    @classmethod
    # 类方法专用于使用类属性，当只使用类属性时，就用类方法
    def class_method(cls): #cls这个参数就是指当前类，而非实例对象
        print(Tool.count)


    # 实例方法
    def function(self):
        print(self.name)


    # 类方法


def function1():
    tool1 = Tool("斧头")
    print(tool1.name)

    tool2 = Tool("锤子")
    print(tool2.name)

    print(Tool.count) # count是专属于一个类的属性，虽然可以用实例访问，但是用类来访问更标准
    print(tool1.count) # 不规范写法
    print(tool2.count) # 不规范写法
    # 所有的在类外以： 类.属性 的方式来添加属性的方式都是错误的

    Tool.class_method()



if __name__ == '__main__':
    function1()
