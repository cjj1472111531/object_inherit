# coding=gbk
# @file:02-inherit_more.py
# @data:2021/7/7 22:40
# Editor:clown
'''
单继承：如果一个类只有一个父类，那这种关系称为单继承
多继承：如果一个类有多个父类，把这种继承关系称为多继承
多层继承：c--->b--->a
'''

'''
重写的概念：子类去定义和父类名字相同的方法
为什么重写：父类的方法，不能满足子类对象需求，需要重写
重写特点：子类调用子类相同的方法  父类调用自己的方法
'''

class animal(object): #对于animal类和object类来说  ，单继承
    # def  __init__(self,name):
    #     self.name=name

    #  在animal了哦书写play。输出快乐的玩耍
    def paly(self):
        print(f"在愉快的玩耍")
        # print(f"{self.name}在愉快的玩耍")


#  定义Dog继承animal
class Dog(animal):
    #Dog---》Animal     也是单继承
    #Animal----》Object 这种关系叫做多层继承
    #多层继承中，子类可以调用所有继承链中的类
    def bark(self):
        print("汪汪汪叫......")
    pass

#定义xtq类
class xtq(Dog):
    #Dog---》Animal     也是单继承
    #xtq----》Dog 这种关系叫做多层继承
    def bark(self):
        print("bark方法被重写了，我不叫了")

    def paly(self):
        print("paly方法也被重写了，我就是玩")


    pass



#  创建dog类 去调用父类的方法
dog = Dog()
dog.paly()
print("$$$$$$$$$$$$$$$")
dog1=xtq()
dog1.paly()
dog1.bark()
