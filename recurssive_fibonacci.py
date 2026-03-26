a=0
b=1
def fib(n):
    if n==1:
        return a
    elif n==2:
        return b
    else:
        return fib(n-2)+fib(n-1)
    
term=int(input("Enter number of terms: "))
print("Fibonacci series:-")
for i in range(1,term+1):
    print(fib(i),end=" ")  
