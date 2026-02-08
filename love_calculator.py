your_name=input("Enter your name: ")
partner_name=input("Enter your partner's name: ")
true=(your_name.lower().count('t') + partner_name.lower().count('t')) + (your_name.lower().count('r') + partner_name.lower().count('r')) + (your_name.lower().count('u') + partner_name.lower().count('u')) + (your_name.lower().count('e') + partner_name.lower().count('e'))
love=(your_name.lower().count('l') + partner_name.lower().count('l')) + (your_name.lower().count('o') + partner_name.lower().count('o')) + (your_name.lower().count('v') + partner_name.lower().count('v')) + (your_name.lower().count('e') + partner_name.lower().count('e'))
percent=int(str(true) + str(love))
if percent<10 or percent>90:
    print(f"Your love percentage is {percent}%, you go together like coke and mentos.")
elif percent>=40 and percent<=50:
    print(f"Your love percentage is {percent}%, you are alright together.")
else:
    print(f"Your love percentage is {percent}%.")        