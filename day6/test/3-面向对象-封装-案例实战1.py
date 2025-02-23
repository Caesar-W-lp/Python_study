#作者:李一安
# 2025年02月04日19时46分18秒


# 家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地为%.2f平方米" % (self.name, self.area)


# 户型类
class House:
    def __init__(self, houses_type, area):
        self.house_type = houses_type
        self.area = area
        self.free_area = area #剩余可用面积
        self.item_list = [] #家具列表


    def __str__(self):
        return ("户型：%s 总面积：%.2f 剩余可用面积：%.2f 家具列表：%s"
              % (self.house_type, self.area, self.free_area, self.item_list))


    # 一个对象中的方法的形参可以是另一个对象，从而做到用其他对象来影响当前的对象
    # 但本对象中的方法最终目的都是影响本对象的属性
    def add_item(self, item: HouseItem): # 可通过:给形参加注解
        if item.area > self.free_area:
            print("空间不够")

        else:
            # 更新剩余面积
            self.free_area -= item.area
            # 更新家具列表
            self.item_list.append(item.name)


def function():
    # 构建家具
    bed = HouseItem("床", 4)
    print(bed)

    chest = HouseItem("柜子", 2)
    print(chest)

    table = HouseItem("桌子", 1.5)
    print(table)

    # 构建房屋
    home = House("二室一厅", 50)

    # 搬家具进房屋
    home.add_item(bed)
    home.add_item(chest)
    home.add_item(table)

    print(home)




if __name__ == '__main__':
    function()