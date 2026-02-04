import random
a=int(input("Lets play🎮\n Enter your choice:-\n Press 0 for ROCK🪨.\n Press 1 for PAPER📰.\n Press 2 for SCISSOR✂️.\n"))
b=random.randint(0,2)
print(f"Opposition's choice:\n{b}")
if a>2 or a<0:
    print("Please enter a valid move🤡.")
elif a==b:
    print("It's a draw🤝")
elif a==0 and b==2:
    print("You won😎")
elif a==2 and b==0:
    print("You lost😐")
elif b>a:
    print("You lost😐")
elif a>b:
    print("You won😎")