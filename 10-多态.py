# coding=gbk
# @file:10-��̬.py
# @data:2021/7/8 14:15
# Editor:clown
'''
��̬������Ҫʹ�ø������ĵط���Ҳ����ʹ���������
1.����̳и���
2.������д������ͬ������
3.ͨ��һ�������ķ���������Ϊ���������ͬ���ķ����е�������͸���ͬ���ķ���
'''
class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def www(self):
        print(f"{self.name}�ڿ��ĵ�Ц����������")

class xtq(Dog):
    def www(self):#��д
        print(f"{self.name}��Ц��")
        # Dog.www(self)
        pass
#����һ����ͬ�ķ���
def play_with_dog(obj_dog):
    obj_dog.www()

dog=Dog('С��',18)
play_with_dog(dog)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=xtq('С��',18)
# dog1.www()
play_with_dog(dog1)


# dog.haha()
# class Dog(object):
#     def www(self):
#         print("���ĵ�Ц����������")
#
# class xtq(Dog):
#     def www(self):
#         print("��ͻȻ��Ц��")
#         Dog.www(self)
#         pass
#
#     # def haha(self):
#     #     print("��ͻȻ��Ц��")
#     #     Dog.www(self)
#     #     pass
#
# dog=xtq()
# dog.www()
# # dog.haha()




