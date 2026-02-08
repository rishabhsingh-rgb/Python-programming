question_bank=[
    {"text":"What will be the output of: print(10//3)?",
     "answer":"B"
    },
    {
      "text":"Which keyword is used to define a function in Python?",
      "answer":"D"  
    },
    {
     "text":"Which of the following is immutable?",
      "answer":"A"   
    },
    {
       "text":"What is the output of: print('Hello'[1])?",
      "answer":"D"    
    },
    {
        "text":"Which operator is used for exponentiation?",
      "answer":"C"   
    }

]     

options=[
    ['A. 3.3','B. 3','C. 4','D. error'],
    ['A. fun','B. function','C. define','D. def'],
    ['A. Tuple','B. List','C. Set','D. Dictionary'],
    ['A. error','B. o','C. h','D. e'],
    ['A. ^','B. //','C. **','D. %']
]


score=0
def check_answer(user_choice,correct_option):
    if user_choice==correct_option:
        return True
    else:
        return False

print("*************************************\n")
print("Welcome to my Python-Quiz game.")
for question_num in range(len(question_bank)):
    print("\n*************************************\n")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)


    guess=input("Enter your choice (A/B/C/D): ").upper()   
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct answer.")
        score+=1
    else:
        print("Wrong answer.")
        print(f"The correct answer is {question_bank[question_num]["answer"]}.")

    print(f"Your current score is {score}/{question_num+1}.") 
print(f"\nYou have given {score} correct answers.")
print(f"Your score is {score/len(question_bank)*100}.")           
