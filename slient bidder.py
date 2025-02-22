def find_higest_bidder(bidding_dict):
    higest = 0
    winner=""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[name]
        if bid_amount > higest:
            higest = bid_amount
            winner = bidder
    print(f"higest bidder is {winner} with a amount of {higest}")

silent_bid = {}

restart = True
while restart:
    name = str(input("What is your Name?: "))
    bid: int = int(input("What is your bid?: $"))
    rerun = input("Do you want to add a new bid Yes or No?:").lower()
    silent_bid[name] = bid
    if rerun == "no":
        restart = False
        find_higest_bidder(silent_bid)
    elif rerun == "yes":
        print("\n"*100)
