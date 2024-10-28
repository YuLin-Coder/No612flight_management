class Phone(object):
    type = '电话'
 #显示电话号码、拨打电话、接听电话
    def __init__(self,number):

        self.number = number


    def getnumber(self):
        print('本机号码为：')
        print(self.number)

    def dail(self):
        print('正在拨打电话...')
 
    def answer(self):
        print('正在接听电话...')
 
 
class Telephone(Phone):#固定电话
    type = '固定电话'

    def dail(self):
        print('在固定地点拨打电话...')
 
    def answer(self):
        print('在固定地点接听电话...')
 
class Mobilephone(Phone):#移动电话
    type = '移动电话'

 
    def dail(self):
        print('在任意地方拨打电话...')
 
    def answer(self):
        print('在任意地方接听电话...')
    
    def sendmessage(self):
        print('正在发送消息...')


telephone = Telephone(10086)
telephone.getnumber()
telephone.dail()
telephone.answer()
print(telephone.type)
mobilephone = Mobilephone(18326555771)
mobilephone.getnumber()
mobilephone.dail()
mobilephone.answer()
mobilephone.sendmessage()
print(mobilephone.type)