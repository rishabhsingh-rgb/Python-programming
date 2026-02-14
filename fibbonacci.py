terms=int(input("Enter the number of terms of fibonacci series: ")) 
a=0 
b=1 
for i in range(terms): 
    print(a, end=" ") 
    temp=a 
    a=b  
    b=temp+b