import random

choices = {
	1: "ROCK",
	2: "PAPER",
	3: "SCISSOR",
}


def main():
	global choice
	print("Welcome to the Game \"ROCK-PAPER-SCISSORS\"!")
	name = input("Enter your name, please: ")

	while True:
		print(f"{name}, what is your choice?")
		print("ROCK(1), PAPER(2), SCISSORS(3), or end game (q or quit)")
		while True:  # get user selection
			try:
				choice = input("Input: ")
				if choice == "q" or choice == "quit":
					print("Goodbye, thank you for playing!")
					exit(0)
				choice = int(choice)
				if choice < 1 or choice > 3:
					raise ValueError
			except ValueError:
				print("Wrong input! Please try again!")
				continue
			else:
				break

		computer_choice = random.randrange(1, 4)
		result = determine_winner(choice, computer_choice)
		if result is not None:
			if result:
				print(f"{name} is the winner of the game!")
			else:
				print("Computer is the winner of the game!")
		else:
			print("None is the winner of the game!")
		print(f"Computer has {choices.get(computer_choice)}\n")


# Returns true if the player wins, false if computer and none if draw
def determine_winner(player: int, computer: int):
	if player == computer:
		return None
	elif player == 1:
		if computer == 2:
			return False
		else:
			return True
	elif player == 2:
		if computer == 3:
			return False
		else:
			return True
	elif player == 3:
		if computer == 1:
			return False
		else:
			return True


main()
