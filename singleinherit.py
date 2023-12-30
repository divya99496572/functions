class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
    def display(self):
        print(self.c)
class derived(Base):
    #pass
    def __init__(self,c,d,e):  #constructor chaining
        Base.__init__(self,c)
        #super().__init__(c)
        self.e=e
        self.d=d
    def display(self):
        super().display()
        print(self.e,self.d)

obj=derived(2,4,5)