# coding=gbk
# @file:02-inherit_more.py
# @data:2021/7/7 22:40
# Editor:clown
'''
���̳У����һ����ֻ��һ�����࣬�����ֹ�ϵ��Ϊ���̳�
��̳У����һ�����ж�����࣬�����ּ̳й�ϵ��Ϊ��̳�
���̳У�c--->b--->a
'''

'''
��д�ĸ������ȥ����͸���������ͬ�ķ���
Ϊʲô��д������ķ��������������������������Ҫ��д
��д�ص㣺�������������ͬ�ķ���  ��������Լ��ķ���
'''

class animal(object): #����animal���object����˵  �����̳�
    # def  __init__(self,name):
    #     self.name=name

    #  ��animal��Ŷ��дplay��������ֵ���ˣ
    def paly(self):
        print(f"��������ˣ")
        # print(f"{self.name}��������ˣ")


#  ����Dog�̳�animal
class Dog(animal):
    #Dog---��Animal     Ҳ�ǵ��̳�
    #Animal----��Object ���ֹ�ϵ�������̳�
    #���̳��У�������Ե������м̳����е���
    def bark(self):
        print("��������......")
    pass

#����xtq��
class xtq(Dog):
    #Dog---��Animal     Ҳ�ǵ��̳�
    #xtq----��Dog ���ֹ�ϵ�������̳�
    def bark(self):
        print("bark��������д�ˣ��Ҳ�����")

    def paly(self):
        print("paly����Ҳ����д�ˣ��Ҿ�����")


    pass



#  ����dog�� ȥ���ø���ķ���
dog = Dog()
dog.paly()
print("$$$$$$$$$$$$$$$")
dog1=xtq()
dog1.paly()
dog1.bark()
