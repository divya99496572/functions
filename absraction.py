from abc import ABC,abstarctmethod
class car(ABC): 
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        self.speed=0
class supra(car):
    pass
class BMW(car):
    pass