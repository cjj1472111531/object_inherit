# coding=gbk
# @file:04-�̳��е�init����.py
# @data:2021/7/8 9:52
# Editor:clown
#����Dog��
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.age=0

    def __str__(self):
       return f"����{self.name},����Ϊ{self.age}"

#  XTg �̳�Dog��
class XTq(Dog):
    #������д__iniy__���� �����ٵ��ø���__init__����
    #�β���� ����init�������βΣ���д�����βΣ���д��������β�
    def __init__(self,name,color):
        # Dog.__init__(self,name)
        # super().__init__(name) #name�������������Ϊ����������Ҫ����
        super(XTq, self).__init__(name)
        self.color=color

    def __str__(self):
        return f"������{self.name},������{self.age}" \
               f",��ɫ��{self.color}"


    pass


#��������Ȯ����
xtq=XTq('zzzz','��ɫ')
print(xtq)
