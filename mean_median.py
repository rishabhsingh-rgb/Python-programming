list1=[]
sum1=0
n=int(input("Enter number of elements in your list: "))
for i in range(n):
    value=int(input(f"Enter the value {i+1}: "))
    list1.append(value)
    sum1+=value
print(list1)
sorted_list=sorted(list1)
print(f"The mean of the elements of list is: {round(sum1/n,2)}")
if n%2==0:
    median=(sorted_list[(n//2)-1]+sorted_list[(n//2)])/2
    print(f"The median of the list is: {median}")
elif n%2!=0:
    median=sorted_list[((n+1)//2)-1]
    print(f"The median of the list is: {median}") 