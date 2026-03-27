num=int(input("Enter a number: "))
factors=[]
org_num=num
i=2
while i<=num:
    if num%i==0:
        num=num/i
        factors.append(i)
    else:
        i+=1

print(f"Prime factors of {org_num}:-{factors}")   
