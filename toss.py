call=input("What is your call: HEADS or TAILS ?").lower()
import random
a=random.randint(1,2)
if a==1 and call=="heads":
    print(" Here comes the HEADS,You won the toss.")
elif a==1 and call=="tails":
    print(" Here comes the HEADS,You lost the toss.")    
elif a==2 and call=="tails":
    print("Here comes the TAILS,You won the toss.")
elif a==2 and call=="heads":
    print("Here comes the TAILS,You lost the toss.") 