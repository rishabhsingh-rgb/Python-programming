import sys
milk=1000
sugar=200
coffee=300
milk_foam=500
money=0
profit=0

def coffee_():
    global milk
    global sugar
    global coffee
    global money
    global profit
   
    if milk-100>=0:
        milk-=100
    else:
        print("Sorry,milk is insufficient for this item.\n")    
        return
    if sugar-15>=0:
        sugar-=15
    else:
        milk+=100
        print("Sorry,sugar is insufficient for this item.\n")  
        return
    if coffee-20>=0:
        coffee-=20
    else:
        milk+=100
        sugar+=15
        print("Sorry,coffee is insufficient for this item.\n")  
        return
    print("Please insert coins")
    five=int(input("How many 5Rs coin: "))
    ten=int(input("How many 10Rs coin: "))
    twenty=int(input("How many 20Rs coin: "))
    total=(5*five+ten*10+20*twenty)
    if total>80:
        print(f"Here is your change {total-80}Rs.")
    elif total<80:
        milk+=100
        sugar+=15
        coffee+=20
        print("Insufficient amount!! Order failed.\n")
        return    
    money+=80
    profit+=20
    print("Here is your coffee.\n")    
        
def latte_():
    global milk
    global sugar
    global coffee
    global money
    global profit
   
    if milk-150>=0:
        milk-=150
    else:
        print("Sorry,milk is insufficient for this item.\n")    
        return
    if sugar-20>=0:
        sugar-=20
    else:
        milk+=150
        print("Sorry,sugar is insufficient for this item.\n")  
        return
    if coffee-30>=0:
        coffee-=30
    else:
        milk+=150
        sugar+=20
        print("Sorry,coffee is insufficient for this item.\n")  
        return
    print("Please insert coins")
    five=int(input("How many 5Rs coin: "))
    ten=int(input("How many 10Rs coin: "))
    twenty=int(input("How many 20Rs coin: "))
    total=(5*five+ten*10+20*twenty)
    if total>150:
        print(f"Here is your change {total-150}Rs.")
    elif total<150:
        milk+=150
        sugar+=20
        coffee+=30
        print("Insufficient amount!! Order failed.\n")
        return    
    money+=150
    profit+=30
    print("Here is your latte.\n")   

def cappuccino_():
    global milk
    global sugar
    global coffee
    global milk_foam
    global money
    global profit
   
    if milk-60>=0:
        milk-=60
    else:
        print("Sorry,milk is insufficient for this item.\n")    
        return
    if milk_foam-60>=0:
        milk_foam-=60
    else:
        milk+=60
        print("Sorry,milk-foam is insufficient for this item.\n") 
        return   
    if sugar-20>=0:
        sugar-=20
    else:
        milk+=60
        milk_foam+=60
        print("Sorry,sugar is insufficient for this item.\n")  
        return
    if coffee-30>=0:
        coffee-=30
    else:
        milk+=60
        sugar+=20
        milk_foam+=60
        print("Sorry,coffee is insufficient for this item.\n")  
        return
    print("Please insert coins")
    five=int(input("How many 5Rs coin: "))
    ten=int(input("How many 10Rs coin: "))
    twenty=int(input("How many 20Rs coin: "))
    total=(5*five+ten*10+20*twenty)
    if total>120:
        print(f"Here is your change {total-120}Rs.")
    elif total<120:
        milk+=60
        milk_foam+=60
        sugar+=20
        coffee+=30
        print("Insufficient amount!! Order failed.\n")
        return    
    money+=120
    profit+=30
    print("Here is your cappuccino.\n")      

def report():
    print(f"\nMilk:- {milk}ml\nMilk-Foam:- {milk_foam}ml\nCoffee:- {coffee}gm\nSugar:- {sugar}gm")           
    print(f"Money collected:- {money}Rs\nProfit:- {profit}Rs\n")

def add():
    global milk
    global coffee
    global milk_foam
    global sugar
    milk1=int(input("\nHow much milk to add(in ml):- "))
    coffee1=int(input("How much coffee to add(in gm):- "))
    sugar1=int(input("How much sugar to add(im gm):- "))
    milk_foam1=int(input("How much milk-foam to add(in ml):- "))
    milk+=milk1
    coffee+=coffee1
    milk_foam+=milk_foam1
    sugar+=sugar1
    print("\nIngredients added successfully.\n")

while True:
    print("Coffee:- 80Rs\nLatte:- 150Rs\nCappuccino:- 120Rs\n")
    choice=input("What would you like to have?").lower()
    if choice=="coffee":
        coffee_()
    elif choice=="latte":
        latte_()
    elif choice=="cappuccino":
        cappuccino_()
    elif choice=="report":
        report()
    elif choice=="add":
        add()    
    elif choice=="off":
        print("Machine turned off!!\n")
        sys.exit(0)
    else:
        print("Sorry this option is not available!!\n")    
