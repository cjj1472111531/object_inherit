# coding=gbk
# @file:08-�෽��.py
# @data:2021/7/8 13:40
# Editor:clown
'''
ʵ������������Ĭ�϶���ķ���������ʵ������  ��һ������self ��ʾʵ������
�෽����ʹ��@classmethoodװ�εķ������෽�� ��һ������cls�������ʱ��������Լ�
ʲô�������ʵ��������ʲô��������෽��
1.����ڷ���ʹ��ʵ�����ԣ���ô�÷������붨��Ϊ�෽��
2.ǰ�᣺����Ҫʹ��ʵ�����ԣ���Ҫʹ�������ԣ����Խ������������Ϊ�෽��

'''

class Dog(object):
    class_name='����'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def  play(self):  #ʵ������
        print(f"С��{self.name}�ڿ��ֵ���ˣ")

    # def get_class_name(self):
    #     #ʵ��������û���õ�ʵ�����ԣ����Կ��Զ���Ϊ�෽��
    #     return self.class_name

    @classmethod
    #�෽������   cls�෽�������β� �ڵ��õ�ʱ����Ҫ�ֶ����ݣ��Զ�����
    def get_class_name(cls):
        return cls.class_name



dog=Dog('fuck',2)
dog.play()
print(dog.get_class_name())

z=dog.get_class_name()
print(z)

dog.__mor__()