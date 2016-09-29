import random
import sys

def main():
    menu = Menu()
    game = Game()
    result = menu.display_menu_selection()
    if result:
        game.play_set()
        answer = game.play()

        if answer:
            print ("You won the game.")
        else:
            print("Better luck next time.")


class Menu():
    def __init__(self):
        self.ITEMS = (
            "Guessing Number:",
            "1: Play",
            "0: Exit",
            )
    def display_menu_list(self):
        for item in self.ITEMS:
            print(item)

    def display_menu_selection(self):
        self.display_menu_list()
        menu_selection = input ("\n Please select an option from above?")
        
        if menu_selection == "0":
            sys.exit(0)
        elif menu_selection == "1":
            return True
        else:
            self.display_invalid_option(menu_selection)
        return False

    def display_invalid_option(menu_selection):
        if menu_selection.isdigit():
            print("\n{} is an invalid option, please try again \n". format (menu_selection))
        else:
            print("\n{} is not a number, please enter a number \n". format(menu_selection))



class Game():
    def __init__(self):
        self.user_guess = 0
        self.start_number=0
        self.end_number=10
        self.random_number = 0
        self.previous_guesses = []
        self.guesses = 3

    def play_set(self):
        print("We are playing guessing number game. \n")
        print("You win if the number is same as mine or you lose.\n")
        print("Default number range is from 0 to 10")
        print("Do you want to set new range?")
        user_input = input("Y/N>   ")
        user_input.lower()
        try:
            if user_input == "y":
                self.start_number = int(input("Enter starting number: >   "))
                self.end_number = int(input("Enter ending number: >   "))
        except:
            print("Default number range is set for the game.")


        print("Default number of guesses = 3.")
        print("Do you want to set new guesses count?")
        user_input = input("Y/N>   ")
        user_input.lower()
        try:
            if user_input == "y":
                self.guesses = int(input("Enter guesses count: >   "))
        except:
            print("Default number is set for the game.")

        self.random_number = random.randint(self.start_number,self.end_number)
        return (self.random_number,self.guesses)

    def play(self):
        old_guess =[]
        while self.guesses >0:   
            user_guess = int(input("Guess a number: > "))
            if (user_guess in old_guess):
                print("This number is guessed already.\n Guess a new number: ")
                continue
            else:
                if user_guess ==self.random_number:
                    print("You win")
                    return True
                elif user_guess >self.random_number:
                    print("Your number is too high.")
                    print("Guess Again.")
                else:
                    print("Your number is too low.")
                    print("Guess Again.")
                old_guess.append(user_guess)
                self.guesses= self.guesses-1

        return False

if __name__ == '__main__':
    main()
