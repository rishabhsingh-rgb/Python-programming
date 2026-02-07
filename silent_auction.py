import os

def highest_bid(bidding_details):
    max_bid=0
    winner=""
   
    for bidder in bidding_details:
        if bidding_details[bidder]>max_bid:
            max_bid=bidding_details[bidder]
            winner=bidder
    for bidder in bidding_details:
        print(bidder,bidding_details[bidder])        
    print(f"The maximum bid is by {winner} of amount {max_bid}.")    
        
print('Welcome to this silent-auction.\n')
bidding_details={}
bid_end=False

while not bid_end:
    name=input("Enter the name of the bidder: ")
    bid_amount=float(input("Enter the bidding amount: "))
    bidding_details[name]=bid_amount
    more_bid=input("\nIf there are more bidder's type 'Yes' otherwise type 'No'.\n").lower()
    if more_bid=='no':
        os.system('cls')
        bid_end=True
        highest_bid(bidding_details)

    elif more_bid=='yes':
        os.system('cls')