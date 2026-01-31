import random
names=input("Enter the name's of all friend's(seperated by comma)\n")
names_split=names.split(",")
print(names_split)
b=len(names_split)
a=random.randint(0,b-1)
print(f"{names_split[a]} will pay the bill.")