student_marks={}
num_student=int(input("Enter the total number of students: "))
for i in range(num_student):
    name=input(f"Enter the name of the student {i+1}: ")
    marks=int(input(f"Enter the marks of {name}: "))
    student_marks[name]=marks

student_grades={}

for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]='A+'
    elif marks>80:
        student_grades[student]='A' 
    elif marks>70:
        student_grades[student]='B+' 
    elif marks>60:
        student_grades[student]='B' 
    elif marks>50:
        student_grades[student]='C' 
    elif marks>40:
        student_grades[student]='D'    
    else:
        student_grades[student]='F'     

print("\nThe grades of the students are displayed below:")
for i in student_grades:
    print(i,"->",student_grades[i])