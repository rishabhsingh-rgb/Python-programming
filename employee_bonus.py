class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def bonus(self):
        self.salary=self.salary+ 0.2*self.salary

class developer(employee):
    def bonus(self):
        self.salary=self.salary+0.1*self.salary

m1=manager("Rakesh",50000)
print(m1.salary)
m1.bonus()
print(m1.salary)
d1=developer("Rahul",40000)
print(d1.salary)
d1.bonus()
print(d1.salary) 
