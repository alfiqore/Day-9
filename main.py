from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bidder = []


def add_bidder(names, amount):
    new_bidder = {}
    new_bidder["names"] = names
    new_bidder["amount"] = amount
    bidder.append(new_bidder)


def count(bidder):
    max_name = bidder[0]["names"]
    max_amount = bidder[0]["amount"]
    for i in range(1, len(bidder)):
        if bidder[i]["amount"] > max_amount:
            max_name = bidder[i]["names"]
            max_amount = bidder[i]["amount"]
    print(f"Maximum bid is ${max_amount} by {max_name}")


play = 1
names = input("What is Your Name : \n")
amount = int(input("How much You want to bid? \n$"))
add_bidder(names, amount)

while play > 0:
    decision = (input("Is there someone else who want to bid? Y/N \n")).lower()
    if decision == 'y':
        clear()
        print(logo)
        names = input("name : \n")
        amount = int(input("How much? \n$"))
        add_bidder(names, amount)
    else:
        count(bidder)
        break
