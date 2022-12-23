import random
from replit import clear



logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
should_continue=True
res=input("Do you want to play Blackjack? Types yes or no: ")

def deal_card():
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def Game(user_cards,computer_cards):
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	print(logo)
	utotal=sum(user_cards)
	ctotal=sum(computer_cards)


	print(f'Your cards: {user_cards}, current score={utotal}\n')
	print(f'Computer\'s first cards: {computer_cards[0]}')

	if ctotal=='21' and utotal=='21':
		print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
		return "Dealer has BlackJack. You lose"
	elif ctotal=='21':
		print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
		return "Dealer has BlackJack. You lose"
	elif utotal=='21':
		print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
		return "You got BlackJack. Dealer loses"
	

	more_cards=input('Type \'y\' to get another card, type \'n\' to pass:')
	while more_cards=='y':
		temp=deal_card()
		user_cards.append(temp)
		utotal+=temp
		if utotal>21 and 11 in user_cards:
			user_cards.remove(11)
			user_cards.append(1)
			utotal=sum(user_cards)
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			break
		elif utotal>21:
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			print('It\'s bust Dealer wins')
			break
		else:
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			more_cards=input('Type \'y\' to get another card, type \'n\' to pass:')
			continue 
	while more_cards=='n' :
		temp1=deal_card()
		computer_cards.append(temp1)
		ctotal+=temp1
		if ctotal>21:
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			print("It's a Bust. You win")
			break
		if ctotal>17:
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			break	
		elif ctotal==21:
			print(f' Your cards: {user_cards} and total: {utotal}. Dealer\'s cards: {computer_cards} and total: {ctotal}\n')
			print('Dealer got BlackJack, You lose')
			break
		else:
			continue		
def assign_cards():
	user_cards = []
	computer_cards = []
	is_game_over = False

	for _ in range(2):
	   user_cards.append(deal_card())
	   computer_cards.append(deal_card())	
	Game(user_cards,computer_cards)   
assign_cards()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  assign_cards() 	
		

