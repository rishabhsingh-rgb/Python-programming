main_string = input("Enter the main string: ")
sub_string = input("Enter the substring: ")

count = 0
length = len(sub_string)

for i in range(len(main_string) - length + 1):
    if main_string[i:i+length] == sub_string:
        count += 1

print("Number of occurrences:", count)
