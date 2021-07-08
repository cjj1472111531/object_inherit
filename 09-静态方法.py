# coding=gbk
# @file:09-静态方法.py
# @data:2021/7/8 14:05
# Editor:clown
'''
用 @staticmethod装饰的方法，称为静态方法，对参数没有特殊要求，可有可无
什么时候定义静态方法
前提：不需要实例属性，也不需要类属性，此时可以将这个方法定义为静态方法
'''

class Dog(object):
    class_name='狗类'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def play(self):  #实例方法
        print(f"小狗{self.name}在快乐的玩耍")

    # def get_class_name(self):
    #     #实例方法，没有用到实例属性，所以可以定义为类方法
    #     return self.class_name
    @staticmethod
    def show_info():
        #静态方法如果有参数，就必须传递实参值
        print("这是一个dog类")

    @classmethod
    #类方法进行   cls类方法调用形参 在调用的时候不需要手动传递，自动传递
    def get_class_name(cls):
        return cls.class_name



dog=Dog('fuck',2)
dog.play()
# print(dog.get_class_name())
z=dog.get_class_name()
print(z)

#对象.方法名()
dog.show_info()
#类名.方法名()
Dog.show_info()

