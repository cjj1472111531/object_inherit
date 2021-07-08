# coding=gbk
# @file:11-鸭子类型的多态.py
# @data:2021/7/8 14:49
# Editor:clown
# 鸭子类型  python是解释性语言（动态语言）
# c语言 c++编译型语言  严格继承关系才能



class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def www(self):
        print(f"{self.name}在开心的笑，哈哈哈哈")

class xtq(Dog):
    def www(self):#重写
        print(f"{self.name}不笑了")
        # Dog.www(self)
        pass

class Yazi(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def www(self):
        print(f"小猫{self.name}被撸了")


#定义一个共同的方法
def play_with_dog(obj_dog):
    obj_dog.www()

dog=Dog('小白',18)
play_with_dog(dog)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=xtq('小黑',18)
# dog1.www()
play_with_dog(dog1)

cat=Yazi('fuck',18)
play_with_dog(cat)

print(Dog.__mro__)