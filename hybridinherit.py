class add1:
    @staticmethod
    def add(a,b,c):
        return a+b+c
class add2:
    @staticmethod
    def add(a,b):
        return a+b
class add(add1,add2):
    pass
    
class sub1:
    @staticmethod
    def sub(a,b):
        return a-b
class cal(add,sub1):
    pass
obj=cal()
