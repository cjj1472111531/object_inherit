# coding=gbk
# @file:04-继承中的init方法.py
# @data:2021/7/8 9:52
# Editor:clown
#定义Dog类
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.age=0

    def __str__(self):
       return f"他叫{self.name},年龄为{self.age}"

#  XTg 继承Dog类
class XTq(Dog):
    #子类重写__iniy__方法 ，不再调用父类__init__方法
    #形参这块 子类init方法的形参，先写父类形参，再写子类独有形参
    def __init__(self,name,color):
        # Dog.__init__(self,name)
        # super().__init__(name) #name参数加入就是因为，父类中需要加入
        super(XTq, self).__init__(name)
        self.color=color

    def __str__(self):
        return f"名字是{self.name},年龄是{self.age}" \
               f",颜色是{self.color}"


    pass


#创建哮天犬对象
xtq=XTq('zzzz','白色')
print(xtq)
