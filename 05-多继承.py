# coding=gbk
# @file:05-��̳�.py
# @data:2021/7/8 10:15
# Editor:clown
# 1.����Dog�࣬����bark�� ��get����
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
    pass

xtq=XTq()
xtq.bark()
xtq.play()
##�����޳�ͻ
xtq.eat()
#�������඼����ͬ���ķ�����Ĭ�ϵ��õ�һ�������eat
xtq.eat()
