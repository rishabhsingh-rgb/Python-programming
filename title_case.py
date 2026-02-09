sentence = input("Enter a sentence: ")

words = sentence.split()

new_sentence = []

for word in words:
    new_word = word[0].upper() + word[1:]
    new_sentence.append(new_word)

result = ""
for i in new_sentence:
    result=result+ ' '+i

print("Capitalized sentence:", result)