# coding=gbk
# @file:09-��̬����.py
# @data:2021/7/8 14:05
# Editor:clown
'''
�� @staticmethodװ�εķ�������Ϊ��̬�������Բ���û������Ҫ�󣬿��п���
ʲôʱ���徲̬����
ǰ�᣺����Ҫʵ�����ԣ�Ҳ����Ҫ�����ԣ���ʱ���Խ������������Ϊ��̬����
'''

class Dog(object):
    class_name='����'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def play(self):  #ʵ������
        print(f"С��{self.name}�ڿ��ֵ���ˣ")

    # def get_class_name(self):
    #     #ʵ��������û���õ�ʵ�����ԣ����Կ��Զ���Ϊ�෽��
    #     return self.class_name
    @staticmethod
    def show_info():
        #��̬��������в������ͱ��봫��ʵ��ֵ
        print("����һ��dog��")

    @classmethod
    #�෽������   cls�෽�������β� �ڵ��õ�ʱ����Ҫ�ֶ����ݣ��Զ�����
    def get_class_name(cls):
        return cls.class_name



dog=Dog('fuck',2)
dog.play()
# print(dog.get_class_name())
z=dog.get_class_name()
print(z)

#����.������()
dog.show_info()
#����.������()
Dog.show_info()

