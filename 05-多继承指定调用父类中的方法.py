# coding=gbk
# @file:05-��̳�ָ�����ø����еķ���.py
# @data:2021/7/8 10:23
# Editor:clown
class Dog(object):
    def bark(self):
        print("�������С�����")
    def eat(self):
        print("�й�ͷ��������")
# 2.����God�࣬ ����play���eat����
class God(object):
    def play(self):
        print("�����з�һ�ᡣ����")
    def eat(self):
        print("��ʲô��������")

# 3.����XTQ�࣬�̳�Dog���God��
class XTq(God,Dog):
    def eat(self):
        print("��д֮��eat����")
        #���ø����еķ���
        # ����һ������.����(self,����)  ��һҪ��һ��
        # Dog.eat(self)
        # God.eat(self)
        #������super(��A��self).������(����)
        # ��A�ĸ��ࣨ�̳�˳��������һ����ģ��ķ���
        # ����֮ǰ�鿴�̳е�˳����
        super(XTq, self).eat()
    pass

xtq=XTq()
xtq.bark()
xtq.play()
##�����޳�ͻ
# xtq.eat()
#�������඼����ͬ���ķ�����Ĭ�ϵ��õ�һ�������eat
#ͬ�����Լ�Ҳ��ͬ���ķ��� �ǻ�Ĭ�����Լ�����ͬ���ķ���
xtq.eat()

##����.__mro__���Բ鿴��ǰ��ļ̳�˳������Ҳ�з�������˳�� ����Ԫ��
print(XTq.__mro__)


