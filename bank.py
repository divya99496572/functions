class sbi:               
    branch='palamaner'
    ifsc='sbi00026'
    manager='charan'
    loc='chittoor'
    def __init__(self,name,acc,pan,bal,mob):
        self.name = name
        self.acc = acc
        self.pan = pan
        self.balance = bal
        self.mobile = mob

    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
    def update_mob(self,mob):
        self.mobile=mob

    @classmethod
    def change_mgr(cls,new):
       cls.manager = new

    @staticmethod
    def add(a,b):
        return a+b


varalu=sbi('varalakshmi',9245768,'DGTY0000D',1000,1234567890)
veena=sbi('veena sunkara',863754,'BGYH2000R',2500,2345678910)
        
