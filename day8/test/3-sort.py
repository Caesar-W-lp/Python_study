# 作者:李一安
# 2025年02月23日21时58分01秒


# sort是列表对象自带的接口
# sort会改变原来的列表
def sort_test():
    list_1 = [9, 5, 2, 7]
    list_1.sort()
    print(list_1)

sort_test()





# sorted会返回排序完成的列表，而原列表不改变
# sorted默认从小到大
# sorted作用于字典时，排序的对象是键值对的key
# sorted(可迭代对象, key = 比较规则)，这里的key就是一个回调函数，将可迭代对象传入这个函数，对这个可迭代对象中的所有一阶元素按照这个函数进行比较
def sorted_test():
    list_1 = [9, 5, 2, 7]
    list_2 = sorted(list_1)
    print(list_1)
    print(list_2)

sorted_test()





def change_lower(str_name: str):
    return str_name.lower()

my_list = "This is a test string from Andrew".split()
print(my_list)

# key可以传递一个比较规则的函数,比较规则发生了改变,key就是给它传递一个函数
# print(sorted(my_list, key=change_lower))
my_list.sort(key=change_lower)
print(my_list)

print('-' * 50)
student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

# lambda表达式，就是匿名函数，匿名函数好处，提高编写效率，提高阅读速度
print(sorted(student_tuples, key=lambda x: x[2]))





class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说更灵活方便，可以返回非字符串类型，但是不能与__str__同时写，否则__str__会覆盖__repr__
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student('john', 'A', 15)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print('-' * 50)
print(sorted(student_objects,key=lambda student:student.age))






from operator import itemgetter, attrgetter



print('使用operator系列')
# 根据比较对象的一阶元素下辖的二阶元素的下标来排序，适用于多阶容器
print(sorted(student_tuples, key=itemgetter(0)))

# 根据比较对象的一阶元素的属性来排序，适用于一阶元素为对象
print(sorted(student_objects,key=attrgetter('age')))



print('使用operator系列,多列排序')
# 若一阶元素下辖的二阶元素的第一下标相同，则比较第二下标
print(sorted(student_tuples, key=itemgetter(1,2)))
# 同种写法
print(sorted(student_tuples, key=lambda x: (x[1],x[2])))
# 若一阶元素下辖的二阶元素的第一下标相同，则比较第二下标，但第二下标按照逆序比较
print(sorted(student_tuples, key=lambda x: (x[1],-x[2]))) #第一列升序，第二列降序
# 若一阶元素的第一属性相同，则比较第二属性
print(sorted(student_objects, key=attrgetter('grade', 'age'),reverse=True))



print('查看排序稳定性')
# 稳定性就是指没有作为比较标准的元素之间的相对位置在比较前后不发生变化
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))







mydict = { 'Li'   : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du'   : ['C',2],
           'Ma'   : ['C',9],
           'Zhe'  : ['H',7] }

print(mydict.items())
# [('Li', ['M', 7]), ('Zhang', ['E', 2]), ('Wang', ['P', 3]), ('Du', ['C', 2]), ('Ma', ['C', 9]), ('Zhe', ['H', 7])]

print(sorted(mydict.items(),key=lambda x:x[1][1]))


# 字典的key就是这个每个value的下标
gameresult = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print('-'*50)
print(sorted(gameresult, key=lambda x:x['rating']))

print(sorted(gameresult , key=itemgetter("rating","name")))


