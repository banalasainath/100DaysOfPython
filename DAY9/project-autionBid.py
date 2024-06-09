#we are building a project to collect the bids secretely

import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def clear_console():
    os.system('cls')

def highest_bid(Bids):
    max_bid_name=""
    max_bid_amount=0
    for key in Bids:
        if Bids[key]>max_bid_amount:
            max_bid_name=key
            max_bid_amount=Bids[key]
    print(f"The highest bid was {max_bid_amount} and it was bid by {max_bid_name}") 
    return       

Bids = {}
print(logo)
while(True):
    name = input("Enter your name : ")
    Bids[name]=int(input("Enter your Bidding Amount : "))
    check = input("Is there any other persons to bid the amount? yes or no : ").lower()
    clear_console()
    if(check=="no"):
        highest_bid(Bids)
        break