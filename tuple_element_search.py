t=("apple", "banana", "mango", "apple", "orange", "banana", "apple")
key=input("Enter element to search: ")
first=-1
last=-1
i=0
while i<len(t):
    if t[i]==key:
        if first==-1:
            first=i
        last=i
    i=i+1
if first==-1:
    print("Element not found in tuple")
else:
    print("First occurrence at index:", first)
    print("Last occurrence at index:", last)
