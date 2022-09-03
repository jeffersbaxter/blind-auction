from os import system, name
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

bids = {}
bidding_is_ongoing = True
while bidding_is_ongoing:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid
    still_bidding = input("Does anyone else want to place a bid? 'y' or 'n' \n")
    if still_bidding == 'n':
        bidding_is_ongoing = False
    clear()

highest_bid = {
    "name": "",
    "bid": 0
}
for bidder in bids:
    if bids[bidder] > highest_bid["bid"]:
        highest_bid["name"] = bidder
        highest_bid["bid"] = bids[bidder]

print(f"{highest_bid['name']} had the highest bid with ${highest_bid['bid']}!")