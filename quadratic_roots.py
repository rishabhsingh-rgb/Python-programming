print("Enter the coefficients of the equation(a,b and c): ") 
a=int(input("Enter a: ")) 
b=int(input("Enter b: ")) 
c=int(input("Enter c:")) 
print(f"Your equation is {a}x^2+{b}x+{c}=0.")
d=(b*b)-(4*a*c) 
if d>=0: 
    root1=(-b+d**0.5)/(2*a)
    root2=(-b-d**0.5)/(2*a) 
    print(f"The roots of the equation are: {round(root1,2)} and {round(root2,2)}.") 
elif d<0: 
    print("There were no real roots of this equation.") 