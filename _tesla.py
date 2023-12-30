class Employee:
    company='Tesla'
    ceo='Elon Musk'

    def insert_member(self,name,age,sal,Eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.Eid=Eid
Divya=Employee()
Abhi=Employee()
Krish=Employee()
Employee.insert_member(Divya,'Divya',20,35000,'tes01')
Employee.insert_member(Abhi,'Abhi',20,30000,'tes02')
Krish.insert_member('krish',21,32000,'tes03')
    