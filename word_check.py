data={
    "THEIR":"THEIR",
    "BUSINESS":"BISINESS",
    "WINDOWS":"WINDMILL",
    "WERE":"WEAR",
    "SAMPLE":"SAMPLE"
}
correct=0
almost=0
wrong=0

for key in data:
    correct_word=key
    given_word=data[key]

    if correct_word==given_word:
        correct+=1
    elif len(correct_word)==len(given_word):
        diff=0
        for i in range(len(correct_word)):
            if correct_word[i]!=given_word[i]:
                diff+=1

        if diff<=2:
            almost+=1
        else:
            wrong+=1
    else:
        wrong+=1

print(f"Correct words: {correct}\nAlmost correct: {almost}\nWrong words: {wrong}")
