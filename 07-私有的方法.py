# coding=gbk
# @file:07-私有的方法.py
# @data:2021/7/8 11:52
# Editor:clown
#私有权限：在属性名和方法名前面加上两个下划线__
# 方法权限：在什么地方可以使用和操作
#   私有方法：在属性名和方法名前面加上两个下划线__
#     1.不能在类外部通过对象直接访问和使用，只能在类内部访问和使用
#     ,不用在外部直接调用
#     2.不能被子类继承
#   公有方法：不是私有就是公有
#      目的是：保证数据的相对安全

class  Dog(object):
    def born(self):
        '''生小狗的方法，生一个小狗，休息30天'''
        print('生了一个小狗')
        self.__sleep()

    def __sleep(self):
        print('休息30天')

dog=Dog()
# dog._Dog__sleep() #直接进入私密方法
dog.born()
# dog.sleep()


