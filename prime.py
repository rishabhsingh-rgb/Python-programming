import math
import sys
def continue_():
    choice=input("Do you want to check more numbers,type 'yes' otherwise type 'no': ").lower()
    if choice=='yes':
        prime()
    else:
        sys.exit()

def prime():
    number=int(input("Enter the number: "))
    flag=1
    if number==1:
        flag=0
    else:
        for i in range(2,math.ceil(number/2)):
        
            if number%i==0:
                flag=0
    if flag==1:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")   
    continue_()    

prime()

