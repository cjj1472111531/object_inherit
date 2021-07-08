# coding=gbk
# @file:06-私有权限__.py
# @data:2021/7/8 10:49
# Editor:clown
#私有权限：在属性名和方法名前面加上两个下划线__
# 方法权限：在什么地方可以使用和操作
#   私有：在属性名和方法名前面加上两个下划线__
#     1.不能在类外部通过对象直接访问和使用，只能在类内部访问和使用
#     2.不能被子类继承
#   公有：不是私有就是公有
#      目的是：保证数据的相对安全

#案列需求：定义people类 定义ICBC_money,
# 钱不能随便修改，必须合法的终端才能操作
class People(object):
    def __init__(self):
        #python中的私有本质是 修改属性的名字
        #在创建对象过程的时候，自动修改属性名
        # 在属性名前面加上 '_类名前缀'
        self.__ICBC_money=0
    #定义公有的办法，提供接口，修改金额
    def get_money(self):
        return self.__ICBC_money

    def change_money(self,money):
        self.__ICBC_money+=money

#创建对线
xw=People()
#实例对象.__dict__ 可以查看对象具有的属性信息，
# 类型是字典，字典的key是属性名 字典value为属性值‘
print('赋值之前：',xw.__dict__)
xw._People__ICBC_money=1032  #修改私有值
xw.__ICBC_money=11000   #不是修改私有属性，是重新添加公有属性
print('赋值之后：',xw.__dict__)
print(xw.__ICBC_money)
print("=="*20)
xw.change_money(50)
print('修改之后的钱为',xw.__dict__)
moeny=xw.get_money()
print("金钱的数量%d"%moeny)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
xw.change_money(-500)
print('修改之后的钱为',xw.__dict__)
moeny=xw.get_money()
print("金钱的数量%d"%moeny)

