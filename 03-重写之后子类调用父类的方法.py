# coding=gbk
# @file:03-重写之后子类调用父类的方法.py
# @data:2021/7/7 22:55
# Editor:clown
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
        print("嗷嗷嗷叫....")

    def paly(self):
        print("paly方法也被重写了，我就是玩")

    def see_host(self):#看到主人之后 要汪汪叫
        #因为重写了
        print("看见主人了，",end='')
        self.bark()
        # 想要在子类中调用父类的同名方法
        #三种方法
        #法一：父类名.方法名.(self,其他参数)
        print("看见主人之后，",end='')
        # 选择父类方法名
        # 为啥要写self 因为这样就是调用这个当前类的self从而不会报错
        # 调用对象不要调用实参值，python解释器会自动加入self值
        # 而此时调用的是“类名”  所以需要手动加上self
        Dog.bark(self)

        #法二：使用类 super(当前A，self).方法名(参数)
        # 当前类就是在那个A类下面   会调用类A中父类的方法
        super(xtq,self).bark()

        #法三：是方法二的简写
        # super().方法名(参数)
        super().bark()


    pass



#  创建dog类 去调用父类的方法
# dog = Dog()
# dog.paly()
# print("$$$$$$$$$$$$$$$")
# dog1=xtq()
# dog1.paly()
# dog1.bark()


dog1=xtq()
dog1.see_host()