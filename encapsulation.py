class simple:
    __a=10
    b=40
    def __init__(self,c,d):
        self.__c=c
        self.d=d
    def __update_c(self,new):
        self.c=new
    def  display(self):
        print(self.__a,self.__c)
class child(simple):
    pass
