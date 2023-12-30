class car:
    name="cars"

    def __init__(self,name,mileage,price,color):
        self.name=name
        self.mileage=mileage
        self.price=price
        self.color=color

class supra(car):
    pass
class BMW(car):
    pass
c1=supra('supra mk4',10,50000,'black')
c2=BMW('BMW m3',20,2500000,'blue')