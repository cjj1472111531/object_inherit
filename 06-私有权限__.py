# coding=gbk
# @file:06-˽��Ȩ��__.py
# @data:2021/7/8 10:49
# Editor:clown
#˽��Ȩ�ޣ����������ͷ�����ǰ����������»���__
# ����Ȩ�ޣ���ʲô�ط�����ʹ�úͲ���
#   ˽�У����������ͷ�����ǰ����������»���__
#     1.���������ⲿͨ������ֱ�ӷ��ʺ�ʹ�ã�ֻ�������ڲ����ʺ�ʹ��
#     2.���ܱ�����̳�
#   ���У�����˽�о��ǹ���
#      Ŀ���ǣ���֤���ݵ���԰�ȫ

#�������󣺶���people�� ����ICBC_money,
# Ǯ��������޸ģ�����Ϸ����ն˲��ܲ���
class People(object):
    def __init__(self):
        #python�е�˽�б����� �޸����Ե�����
        #�ڴ���������̵�ʱ���Զ��޸�������
        # ��������ǰ����� '_����ǰ׺'
        self.__ICBC_money=0
    #���幫�еİ취���ṩ�ӿڣ��޸Ľ��
    def get_money(self):
        return self.__ICBC_money

    def change_money(self,money):
        self.__ICBC_money+=money

#��������
xw=People()
#ʵ������.__dict__ ���Բ鿴������е�������Ϣ��
# �������ֵ䣬�ֵ��key�������� �ֵ�valueΪ����ֵ��
print('��ֵ֮ǰ��',xw.__dict__)
xw._People__ICBC_money=1032  #�޸�˽��ֵ
xw.__ICBC_money=11000   #�����޸�˽�����ԣ���������ӹ�������
print('��ֵ֮��',xw.__dict__)
print(xw.__ICBC_money)
print("=="*20)
xw.change_money(50)
print('�޸�֮���ǮΪ',xw.__dict__)
moeny=xw.get_money()
print("��Ǯ������%d"%moeny)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
xw.change_money(-500)
print('�޸�֮���ǮΪ',xw.__dict__)
moeny=xw.get_money()
print("��Ǯ������%d"%moeny)

