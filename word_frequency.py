def frequency(s):
    words=s.lower().split()   
    freq={}

    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    for word in sorted(freq):
        print(word, ":", freq[word])

text=input("Enter a string: ")
frequency(text)
