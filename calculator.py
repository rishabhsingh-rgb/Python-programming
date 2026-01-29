import os

def add(first,second):
    sum=first+second
    return sum 

def sub(first,second):
    diff=first-second
    return diff

def mul(first,second):
    product=first*second
    return product

def div(first,second):
    division=first/second
    return division

operations_dict={

    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

a=float(input('● Enter first number: '))

print(f"➕\n➖\n✖️ (*)\n➗(/)")

continue_=True  
while continue_:
    choice=input('● Enter your choice: ')
    b=float(input('● Enter second number: '))
    calculator_op=operations_dict[choice]
    output=calculator_op(a,b)
    print(f'{a} {choice} {b} = {output}')

    what_next=input(f"● Enter '𝒀' to continue with {output}.\n● Enter '𝓝' to start a new calculation.\n● Enter '✘' to exit.\n ").lower()
    if what_next=='y':
        a=output
    elif what_next=='n':
        os.system('cls')
        a=float(input("● Enter first number: "))    
    elif what_next=='x':
        continue_=False
        print('Calculation ended.')    