import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I',
         'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','&','(',')','+','/','*']
letter=int(input("Enter the number of letter's in password:"))
num=int(input("Enter the number of numbers in password: "))
symbol=int(input("Enter the number of symbols in password: "))
password=[]
for i in range(1,letter+1):
    a=random.randint(0,51)
    password.append(letters[a])
for i in range(1,num+1):
    b=random.randint(0,9)
    password.append(numbers[b])
for i in range(1,symbol+1):
    c=random.randint(0,9)
    password.append(symbols[c])  
random.shuffle(password)
password2=""
for i in range(0,len(password)):
    password2=password2 + password[i]

print(f"Your password is: {password2}")