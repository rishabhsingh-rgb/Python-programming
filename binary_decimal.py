binary=input("Enter the binary number: ")
binary=binary[::-1]
decimal=0
i=0
for num in binary:
    decimal+=(2**i)*int(num)
    i+=1
    
print("The decimal equivalent of given binary number is:",decimal)
