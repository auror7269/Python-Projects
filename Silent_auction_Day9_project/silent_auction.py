from replit import clear
from silent_auction_D9_art import logo


print(logo)
response="yes"
dict1={}
while response=="yes":
		name=input("Enter your name: ")
		bid=int(input("What is your bid? $"))
		dict1[name]=bid
		response=input("Type yes if there are other bidders after you, Otherwise type no: ")
		clear()

def highest_bid(dict):
	winner=""
	highest_bid=0
	for i in dict:
		temp=int(dict[i])
		if temp>highest_bid:
			highest_bid=dict[i]
			winner=i
		else:
			continue
	print(f"{winner} won the auction with a bid of ${highest_bid}")
highest_bid(dict1)			

		
