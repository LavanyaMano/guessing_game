import random
import math
# import argv from sys
# guesses = argv


def main():
	ITEMS = (
		"Guessing Number:",
		"1: Play",
		"0: Exit",
		)

	while True:
		for item in ITEMS:
			print(item)

		menu_selection = input ("\n Please select an option from above?")
		
		if menu_selection == "0":
			break
		elif menu_selection == "1":
			game()
		else:
			display_invalid_option(menu_selection)

def display_invalid_option(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again \n". format (menu_selection))
	else:
		print("\n{} is not a number, please enter a number \n". format(menu_selection))

def game():
	print("We are gonna play of guessing number. \n")
	print("You win if the number is same as mine or you lose.\n")
	print("Guess a number between 0 and 10.")
	user_guess = int(input("> "))
	guesses = 2
	random_number = math.floor(random.random()*10)
	old_guess = []
	flag = False
	while guesses>0:	
		if (user_guess in old_guess):
			print("This number is guesses already.\n Guess a new number: ")
			user_guess = int(input("> "))
		else:
			if user_guess == random_number:
				print("You win")
				flag = True
				break
			elif user_guess > random_number:
				print("Your number is too high.")
				print("Guess Again.")
				user_guess = int(input("> "))
			else:
				print("Your number is too low.")
				print("Guess Again.")
				user_guess = int(input("> "))

			old_guess.append(user_guess)
			guesses= guesses-1

	if flag:
		main()
	else:
		print("You Lose")

	return None
	

if __name__ == '__main__':
	main()