from os import system, name

def clear():
     if name == 'nt':
        _ = system('cls')
     else:
        _ = system('clear')
def add_bidder():
    print("\nWelcome to the secret auction program!")
    name = input("Enter your name: ")
    bid = int(input("Enter your bid : $"))
    auction_members[name] = bid

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

auction_members = {}

print(logo)
add_bidder()
more_bidders = input("Are there any more bidders? Type 'yes' or 'no' : ").lower()
while more_bidders == "yes":
    clear()
    add_bidder()
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no' : ").lower()

max_bid = -1
winner_name = ""
for name in auction_members:
    if auction_members[name] > max_bid:
        max_bid = auction_members[name]
        winner_name = name

print(f"The winner is {winner_name} with a bid of ${max_bid}!")