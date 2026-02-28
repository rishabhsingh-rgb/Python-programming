rows=int(input("Enter number of rows in upper-triangular part: "))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()        
for i in range(1,rows):
    for k in range(i):
        print(" ",end="")
    for j in range(2*rows-(2*i+1)):
        print("*",end="")
    print()    
