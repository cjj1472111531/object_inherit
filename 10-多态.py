# coding=gbk
# @file:10-多态.py
# @data:2021/7/8 14:15
# Editor:clown
'''
多态：在需要使用父类对象的地方，也可以使用子类对象
1.子类继承父类
2.子类重写父类中同名方法
3.通过一个公共的方法，参数为父类对象，在同样的方法中调用子类和父类同名的方法
'''
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
#定义一个共同的方法
def play_with_dog(obj_dog):
    obj_dog.www()

dog=Dog('小白',18)
play_with_dog(dog)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=xtq('小黑',18)
# dog1.www()
play_with_dog(dog1)


# dog.haha()
# class Dog(object):
#     def www(self):
#         print("开心的笑，哈哈哈哈")
#
# class xtq(Dog):
#     def www(self):
#         print("我突然不笑了")
#         Dog.www(self)
#         pass
#
#     # def haha(self):
#     #     print("我突然不笑了")
#     #     Dog.www(self)
#     #     pass
#
# dog=xtq()
# dog.www()
# # dog.haha()




