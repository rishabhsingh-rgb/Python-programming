mat1=[]
n=int(input("Enter the number of rows in first-matrix: "))
m=int(input("Enter the number of column in first-matrix: "))
for i in range(n):
    print(f"\nEnter the {m} elements of row{i+1}:")
    row=[]
    for j in range(m):
        value=int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    mat1.append(row)

mat2=[]
p=int(input("\nEnter the number of rows in second-matrix: "))
q=int(input("Enter the number of column in second-matrix: "))
for i in range(p):
    print(f"\nEnter the {q} elements of row{i+1}:")
    row=[]
    for j in range(q):
        value=int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    mat2.append(row) 
print("\nFirst matrix:")       
for i in range(n):
    for j in range(m):
        print(mat1[i][j],end=' ')
    print()  

print("\nSecond matrix:")
for i in range(p):
    for j in range(q):
        print(mat2[i][j],end=' ')
    print()         
result=[]
if m!=p:
    print("\nMatrix multiplication not possible.")
    exit()
else:
    for i in range(n):
        row2=[]
        for j in range(q):
            sum=0
            for k in range(p):
                sum+=mat1[i][k]*mat2[k][j]
            row2.append(sum)
        result.append(row2)
print("\nThe resultant matrix after multiplication is:")        
for i in range(n):
    for j in range(q):
        print(result[i][j],end=' ')
    print()     