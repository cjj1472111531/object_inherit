# coding=gbk
# @file:05-多继承.py
# @data:2021/7/8 10:15
# Editor:clown
# 1.定义Dog类，定义bark类 和get方法
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
    pass

xtq=XTq()
xtq.bark()
xtq.play()
##以上无冲突
xtq.eat()
#两个父类都存在同样的方法，默认调用第一个父类的eat
xtq.eat()
