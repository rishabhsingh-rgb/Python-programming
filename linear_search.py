n=int(input("Enter the number of element in your list: "))
list=[]
print(f"Enter {n} elements:")
for i in range(n):
    value=int(input(f"Enter element {i+1}:"))
    list.append(value)

element=int(input("Enter the element to search: "))
flag=1
count=0
for i in range(n):
    if list[i]==element:
        flag=0
        count+=1
    else:
        continue
if flag==0:
    print(f"{element} found and appears {count} times in list.") 
else:
    print(f"{element} not found in list.")  