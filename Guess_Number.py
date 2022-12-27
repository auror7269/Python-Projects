import random as rd 
from replit import clear
num=rd.randint(0,100)
chances=10
def game(num,chances):
	clear()
	while chances>0:

		us=int(input('Guess the number between 0 and 100\n'))
		chances-=1
		if us==num:
			print(f'That is correct.The number was {num} \n')
			break
		elif us>num:
			print(f'Too High.')
			print(f'Number of chances remaining {chances}')
			continue
		elif us<num:
			print('Too Low')
			print(f'Number of chances remaining {chances}')
			continue
user=int(input('''Which level do you want to play on?
	    For Easy press 0
	    For Hard press 1  '''))
if	user==0:
	chances=10
	print('You get 10 chances to guess the number')
elif user==1:
	chances=5
	print('You get 5 chances to guess the number')			
game(num,chances)




