# coding=gbk
# @file:01-inherit_basic.py
# @data:2021/7/7 22:23
# Editor:clown
#  定义是一个动物类
class animal(object):
    # def  __init__(self,name):
    #     self.name=name

    #  在animal了哦书写play。输出快乐的玩耍
    def paly(self):
        print(f"在愉快的玩耍")
        # print(f"{self.name}在愉快的玩耍")


#  定义Dog继承animal
class Dog(animal):
    pass


#  创建dog类 去调用父类的方法
dog = Dog()
dog.paly()
