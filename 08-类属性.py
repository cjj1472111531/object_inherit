# coding=gbk
# @file:08-类属性.py
# @data:2021/7/8 12:10
# Editor:clown
'''
对象（实例对象）：通过class定义的类创建，
即通过类实例化来的  又称为实例，实例对象

类(类对象)通过class定义的，又称为类对象，是python解释器在创建类的时候自动创建
作用 ：1.通过类对象，去定义实例对象
      2.类对象可以保存属性信息，作为类属性

类属性定义：在类内部，方法外部定义的变量就是类属性
类属性，字内存中只有一份

如何确定一个属性是该定义为 实例属性 还是  类属性
在假设这个属性为实例属性，查看这个属性值对于不同的实例对象，
属性值是否都一样，而且需要同时改变，
如果是 则可以定义为类属性
如果不是 则可以定义实例属性
'''

class Dog(object):
    class_name='狗类'

    def __init__(self,name,age):
        #定义的都是实例属性
        self.name=name
        self.age=age

dog=Dog('laal',18)
print(dog.__dict__)
print("^"*30)
#类名.__dict__ 查看类对象具有的属性
print(Dog.__dict__)
#查看类名.__mro__ 查看类对象具有的属性
# print("^"*30)
# print(Dog.__mro__)

#访问类属性
#类名.类属性
print(Dog.class_name)

#修改类属性
# 类名.类属性 =属性值
Dog.class_name='Fuck'
print(Dog.class_name)
print("&&&&&&&&&&")
# 补充 ：如果不存在和实例属性相同的类属性，则可以使用实例对象访问类属性的值
# 如果存在重名，则使用实例属性访问的一定是实例属性，不是类属性
print(dog.class_name)

