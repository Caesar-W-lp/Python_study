# 作者:李一安
# 2025年02月04日22时24分19秒
# 1713450722@qq.com

# 对象中的属性也可以是另一个对象

class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0  # 类中有的属性可能不用传参，但一定要在类中给它设置初始值

    def __str__(self):
        return f"[{self.model}]目前弹量为[{self.bullet_count}]"

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            print("fire!!!")
            self.bullet_count -= 1
        else:
            print(f"[{self.model}]子弹不足...")


class Soldier:
    def __init__(self, name, gun : Gun = None):
        self.name = name
        self.gun = gun

    # 开火
    def fire(self):
        # 判断是否有枪
        if self.gun is None:
            print(f"[{self.name}]手里没枪...")
        else:
            self.gun.shoot()


def func():
    ak47 = Gun("ak47")
    san_duo = Soldier("许三多")
    san_duo.fire()
    san_duo.gun = ak47
    san_duo.fire()
    san_duo.gun.add_bullet(50)
    san_duo.fire()



if __name__ == '__main__':
    func()

    # is 和 is not 运算符用于判断连个对象的引用对象是否为同一个，类似于id(a) == id(b)