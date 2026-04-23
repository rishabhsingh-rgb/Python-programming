class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"Name:- {self.name}\nRoll no:- {self.roll_no}\nMarks:- {self.marks}") 

    def calculate_grade(self):
        if self.marks>90 and self.marks<=100:
            return "A+"
        elif self.marks>80:
            return "A"
        elif self.marks>70:
            return "B+"
        elif self.marks>60:
            return "B"
        elif self.marks>50:
            return "C"
        elif self.marks>40:
            return "D"
        else:
            return "Failed!!!"       

s1=Student("Raju",23,70)
s1.display()
print(s1.name)
print(s1.roll_no)
print(s1.marks)
print(s1.calculate_grade())
