# coding=gbk
# @file:01-inherit_basic.py
# @data:2021/7/7 22:23
# Editor:clown
#  ������һ��������
class animal(object):
    # def  __init__(self,name):
    #     self.name=name

    #  ��animal��Ŷ��дplay��������ֵ���ˣ
    def paly(self):
        print(f"��������ˣ")
        # print(f"{self.name}��������ˣ")


#  ����Dog�̳�animal
class Dog(animal):
    pass


#  ����dog�� ȥ���ø���ķ���
dog = Dog()
dog.paly()
