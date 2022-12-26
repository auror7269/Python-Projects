import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices=[rock,paper,scissors]
user_choice=input('What do you choose type 0 for rock, 1 for paper, 2 for scissors\n')
if user_choice=="0":
  print(rock)
elif user_choice=="1":
  print(paper)
elif user_choice=="2":
  print(scissors)

cp_choices=random.choice(choices)
if user_choice=='0' and cp_choices==paper:
  print(f'Compuer chose: {paper}')
  print('You lose')
elif user_choice=='1' and cp_choices==scissors:
  print(f'Compuer chose: {scissors}')
  print('You lose')  
elif user_choice=='2' and cp_choices==rock:
  print(f'Compuer chose: {rock}')
  print('You lose') 
elif user_choice=='0' and cp_choices==rock:
  print(f'Compuer chose: {rock}')
  print('It\'s a tie')  
elif user_choice=='1' and cp_choices==paper:
  print(f'Compuer chose: {paper}')
  print('It\'s a tie') 
elif user_choice=='2' and cp_choices==scissors:
  print(f'Compuer chose: {scissors}')
  print('It\'s a tie') 
else:
  print(f"Compuer chose: {cp_choices}") 
  print('You won')   