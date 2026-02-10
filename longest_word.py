sentence = input("Enter a sentence: ")
words = sentence.split()  
longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("Longest word in the given sentence is:", longest_word)
print("Length of the longest word is:", max_length)