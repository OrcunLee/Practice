from replit import clear

bids = {}
bidding_finished = False

highest_bid = 0
winner = ""

while not bidding_finished :
    name = input("What is your name? : ")
    bid = int(input("What's your bid? : $"))
    bids[name] = bid
    bid_continue = input("Are there any other bidders? type 'yes' or 'no' ")
    if bid_continue == "no" :
        bidding_finished = True
    elif bid_continue == 'yes' :
        clear()

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid: 
        highest_bid = bid_amount
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")