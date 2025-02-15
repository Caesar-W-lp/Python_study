# 作者:李一安
# 2025年02月07日18时34分33秒
# 1713450722@qq.com


# 多态：不同的继承子类对象对同一条指令的反应是不一样的


class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing...")


class FlayDog(Dog):
    def play(self):
        print(f"{self.name} is flaying...")


class Person:
    def __init__(self, name):
        self.name = name

    def play(self, dog: Dog or FlayDog):
        print(f"{self.name} is playing with {dog.name}")
        dog.play()






def function():
    dog = Dog("Buddy")
    dog.play()  # Buddy is playing...

    flay_dog = FlayDog("Flay")
    flay_dog.play()  # Flay is flaying...

    person = Person("Jack")
    person.play(dog)  # Jack is playing with Buddy
    person.play(flay_dog)  # Jack is playing with Flay


if __name__ == '__main__':
    function()