mat=[]
n=int(input("Enter the number of rows/column in your square matrix: "))
for i in range(n):
    print(f"\nEnter the {n} elements of row{i+1}:")
    row=[]
    for j in range(n):
        value=int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)
    mat.append(row)

flag=1 
print("\nYour given matrix is:")
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=' ')
        if mat[i][j]!=mat[j][i]:
            flag=0 
    print()
        
if flag==0:
    print("Given matrix is Asymmetric matrix.")
else:
    print("Given matrix is Symmetric matrix.")    
        