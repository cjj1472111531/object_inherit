# coding=gbk
# @file:03-��д֮��������ø���ķ���.py
# @data:2021/7/7 22:55
# Editor:clown
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
        print("��໽�....")

    def paly(self):
        print("paly����Ҳ����д�ˣ��Ҿ�����")

    def see_host(self):#��������֮�� Ҫ������
        #��Ϊ��д��
        print("���������ˣ�",end='')
        self.bark()
        # ��Ҫ�������е��ø����ͬ������
        #���ַ���
        #��һ��������.������.(self,��������)
        print("��������֮��",end='')
        # ѡ���෽����
        # ΪɶҪдself ��Ϊ�������ǵ��������ǰ���self�Ӷ����ᱨ��
        # ���ö���Ҫ����ʵ��ֵ��python���������Զ�����selfֵ
        # ����ʱ���õ��ǡ�������  ������Ҫ�ֶ�����self
        Dog.bark(self)

        #������ʹ���� super(��ǰA��self).������(����)
        # ��ǰ��������Ǹ�A������   �������A�и���ķ���
        super(xtq,self).bark()

        #�������Ƿ������ļ�д
        # super().������(����)
        super().bark()


    pass



#  ����dog�� ȥ���ø���ķ���
# dog = Dog()
# dog.paly()
# print("$$$$$$$$$$$$$$$")
# dog1=xtq()
# dog1.paly()
# dog1.bark()


dog1=xtq()
dog1.see_host()