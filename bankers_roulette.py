import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

c=random.choice(names)
print(f"{c} is going to buy the meal today!")