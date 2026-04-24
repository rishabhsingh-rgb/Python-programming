class rectangle:
    def __init__(self,lenght,breadth):
        self.l=lenght
        self.b=breadth
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)

r1=rectangle(4,6)
print(r1.area())
print(r1.perimeter())     
