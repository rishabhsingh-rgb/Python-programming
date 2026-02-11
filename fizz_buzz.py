a=input("Enter the maximum range of number: ")
for i in range(1,int(a)+1):
    if i%3==0 and i%5==0:
         print(f"{i} FIZZBUZZ")
    elif i%3==0:
        print(f"{i} FIZZ")
    elif i%5==0:
        print(f"{i} BUZZ")   