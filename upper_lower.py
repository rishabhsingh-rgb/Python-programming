string=input("Enter the string: ")
upper_case=" "
lower_case=" "
for ch in string:
    if 'a'<= ch<='z':
        upper_case+=chr(ord(ch)-32)
    else:
        upper_case+=ch
for ch in string:
    if 'A'<= ch<='B':
        lower_case=chr(ord(ch)+32)
    else:
        lower_case+=ch
print(f"Upper-case string is:{upper_case}")
print(f"Lower-case string is:{lower_case}")