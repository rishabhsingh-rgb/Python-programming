print("Here is the menu:\n" + "\n" +"Small pizza: 150 RS\n" + "Medium pizza: 200 RS\n" + "Large pizza: 500 RS\n" + "Pepperoni for small pizza: 20 RS\n" + "Pepperoni for medium or large pizza: 30 RS\n" + "Extra cheese for any size pizza: 25 RS")
print("Plz select the size of pizza you want:")
size=input("Small, Medium or Large: ")
cheese=input("Do you want extra cheese? Yes or No: ")
if size=="Small" or size=="small":
    bill=150
    pepperoni=input("Do you want pepperoni? Yes or No: ")
    if pepperoni=="Yes" or pepperoni=="yes":
        bill+=20
    if cheese=="Yes" or cheese=="yes":
        bill+=25
if size=="Medium" or size=="medium":
    bill=200
    pepperoni=input("Do you want pepperoni? Yes or No: ")
    if pepperoni=="Yes" or pepperoni=="yes":
        bill+=30
    if cheese=="Yes" or cheese=="yes":
        bill+=25
if size=="Large" or size=="large":
    bill=500
    pepperoni=input("Do you want pepperoni? Yes or No: ")
    if pepperoni=="Yes" or pepperoni=="yes":
        bill+=30
    if cheese=="Yes" or cheese=="yes":
        bill+=25                
print("Your bill is of RS:",str(bill)+"\n")
print("Thanku for visiting our store.")