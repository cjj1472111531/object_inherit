# coding=gbk
# @file:11-Ѽ�����͵Ķ�̬.py
# @data:2021/7/8 14:49
# Editor:clown
# Ѽ������  python�ǽ��������ԣ���̬���ԣ�
# c���� c++����������  �ϸ�̳й�ϵ����



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

class Yazi(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def www(self):
        print(f"Сè{self.name}��ߣ��")


#����һ����ͬ�ķ���
def play_with_dog(obj_dog):
    obj_dog.www()

dog=Dog('С��',18)
play_with_dog(dog)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=xtq('С��',18)
# dog1.www()
play_with_dog(dog1)

cat=Yazi('fuck',18)
play_with_dog(cat)

print(Dog.__mro__)