class animal:
    def sound(self):
        print("Animal makes sound")

class Dog(animal):
    def sound(self):
        print("Dog Barks")

class Cat(animal):
    def sound(self):
        print("Cat Meows")  

d1=Dog()
d1.sound()
c1=Cat()
c1.sound()  
