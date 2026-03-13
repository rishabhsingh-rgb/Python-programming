def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(f"Values before:-\na={a}\nb={b}")
a,b=swap(a,b)
print(f"Values after:-\na={a}\nb={b}")
