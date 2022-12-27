from replit import clear
import random as rd 
import hangman_words
import hangman_art


lives=6
chosen_word= rd.choice(hangman_words.word_list)
display=[]

print(hangman_art.logo)
for blank in range(len(chosen_word)):
         display.append("_ ")
        
print(display) 
end_of_game=False       
while not end_of_game: 
        user_input=input('Guess the word: ').lower()
        clear()
        if user_input in display:
            print(f"You have already guessed {user_input}")
            continue
        for position in range(len(chosen_word)):
            i=chosen_word[position]
            if user_input==i:
                display[position]=user_input
        print(display)    
        if user_input not in chosen_word:
            print(f"You guessed {user_input}, that is not in the word. You lose a life.")
            lives-=1
            if lives==0:
               end_of_game=True
               print(f"You lose!!! Better Luck next time {chosen_word}")
        
        if "_ " not in display:
            end_of_game=True
            print("You win")  
        
        print(hangman_art.stages[lives])      
        
   


