# coding=gbk
# @file:08-类方法.py
# @data:2021/7/8 13:40
# Editor:clown
'''
实例方法：类中默认定义的方法，就是实例方法  第一个参数self 表示实例对象
类方法：使用@classmethood装饰的方法，类方法 第一个参数cls，代表的时候类对象自己
什么情况定义实例方法，什么情况定义类方法
1.如果在方法使用实例属性，那么该方法必须定义为类方法
2.前提：不需要使用实例属性，需要使用类属性，可以将这个方法定义为类方法

'''

class Dog(object):
    class_name='狗类'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def  play(self):  #实例方法
        print(f"小狗{self.name}在快乐的玩耍")

    # def get_class_name(self):
    #     #实例方法，没有用到实例属性，所以可以定义为类方法
    #     return self.class_name

    @classmethod
    #类方法进行   cls类方法调用形参 在调用的时候不需要手动传递，自动传递
    def get_class_name(cls):
        return cls.class_name



dog=Dog('fuck',2)
dog.play()
print(dog.get_class_name())

z=dog.get_class_name()
print(z)

dog.__mor__()