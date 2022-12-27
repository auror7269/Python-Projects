import caeser_art
print(caeser_art.logo)

def caeser(word,shift,direction):
	ans=""
	if direction=="decode":
		shift*=-1
	for i in word:
		
		if i in alphabet:
			pos=alphabet.index(i)
			new_pos=pos+shift
			new_letter=alphabet[new_pos]
			ans+=new_letter
		else:
			ans+=i
		
	print(f"The {direction}d text is : {ans}")	
response=True		
while response:

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	while shift>26:
		shift=shift%26
	caeser(text,shift,direction)
	res=input("Type yes if you wanna go again, Otherwise type  no: ")
	if res=="yes":
		continue
	else:
		response=False
		print("Goodbye !! Have a nice day :)")

