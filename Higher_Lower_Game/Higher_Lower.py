from Higher_Lower_art import logo,vs

from data import data
import random as rd
from replit import clear

def check_answer(guess,a_follower,b_follower):
	ans='a'
	if a_follower>b_follower:
		ans='a'
	elif b_follower>a_follower:
		ans='b'
	if guess==ans:
		return True
	else:
		return False			
def format_data(account):
	account_name=account["name"]
	account_desc=account["description"]
	account_country=account["country"]
	return f"{account_name}, a {account_desc}, from {account_country}\n"


print(logo)
score=0
game_continue=True	
accountB=rd.choice(data)
while game_continue:
	accountA=accountB
	accountB=rd.choice(data)
	while accountA==accountB:
	 	accountB=rd.choice(data)

	print(f"Compare A: {format_data(accountA)}")
	print(vs)
	print(f"Against B: {format_data(accountB)}")	

	guess=input("Who has more followers?Type 'A' or 'B': ").lower()

	a_follower=accountA["follower_count"]
	b_follower=accountB["follower_count"]

	correct=check_answer(guess,a_follower,b_follower)
	clear()
	print(logo)
	if correct:
		score+=1
		print(f"You're right! Current score: {score}")
	else:
		game_continue=False
		print(f"Sorry.that's wrong. Final Score: {score}")	







