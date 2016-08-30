import random
import math
import pdb
from sys import argv


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
	script, guesses = argv
	print("We are gonna play of guessing number. \n")
	print("You win if the number is same as mine or you lose.\n")
	print("Guess a number between 0 and 10.")
	user_guess = 0
	#guesses = 2
	random_number = math.floor(random.random()*10)
	old_guess = []
	flag = False
	guesses = int(guesses)
	while guesses >0:	
		user_guess = int(input("> "))
		if (user_guess in old_guess):
			print("This number is guessed already.\n Guess a new number: ")
			continue
		else:
			if user_guess == random_number:
				print("You win")
				flag = True
				break
			elif user_guess > random_number:
				print("Your number is too high.")
				print("Guess Again.")
			else:
				print("Your number is too low.")
				print("Guess Again.")
			old_guess.append(user_guess)
			#pdb.set_trace()
			guesses= guesses-1

	if flag:
		pass
	else:
		print("You Lose")

	return None
	

if __name__ == '__main__':
	main()