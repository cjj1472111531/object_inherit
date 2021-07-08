# coding=gbk
# @file:05-多继承指定调用父类中的方法.py
# @data:2021/7/8 10:23
# Editor:clown
class Dog(object):
    def bark(self):
        print("汪汪汪叫。。。")
    def eat(self):
        print("啃骨头。。。。")
# 2.定义God类， 定义play类和eat方法
class God(object):
    def play(self):
        print("在云中飞一会。。。")
    def eat(self):
        print("吃什么鬼。。。。")

# 3.定义XTQ类，继承Dog类和God类
class XTq(God,Dog):
    def eat(self):
        print("重写之后eat方法")
        #调用父类中的方法
        # 方法一：类名.方法(self,参数)  法一要好一点
        # Dog.eat(self)
        # God.eat(self)
        #法二：super(类A，self).方法名(参数)
        # 类A的父类（继承顺序链的下一个类的）的方法
        # 可以之前查看继承的顺序链
        super(XTq, self).eat()
    pass

xtq=XTq()
xtq.bark()
xtq.play()
##以上无冲突
# xtq.eat()
#两个父类都存在同样的方法，默认调用第一个父类的eat
#同样我自己也有同样的方法 那会默认用自己类下同样的方法
xtq.eat()

##类名.__mro__可以查看当前类的继承顺序链，也叫方法调用顺序 返回元组
print(XTq.__mro__)


