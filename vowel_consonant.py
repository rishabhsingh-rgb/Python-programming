
string = input("Enter a string: ").lower()
vowels = 0
consonants = 0
spaces = 0
for ch in string:
    # Check for space
    if ch == ' ':
        spaces += 1
    elif ('a' <= ch <= 'z'):
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)