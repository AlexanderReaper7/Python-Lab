class Grid:
	def __init__(self):
		self.squares = [[DEFAULT_CHAR for i in range(N)] for j in range(N)]


def print_grid(grid: Grid):
	output = "\n"
	for row in grid.squares:
		i = 0
		for sq in row:
			i += 1
			output = output + sq  # add this square´s character to output
			if i % N == 0:  # if at the end of row, add new-line character
				output = output + "\n"
			else:  # else add space
				output = output + " "
	print(output)


def get_input(current_player: str):
	while True:
		try:
			inputstr = input("input coord for player \"{}\" ".format(current_player))
			inputs = inputstr.split(" ")
			outputs = (int(inputs[0])-1, int(inputs[1])-1)
		except ValueError:
			print("{} is not valid input, try again.".format(inputstr))
		except IndexError:
			print("{} is not valid input, try again.".format(inputstr))
		else:
			return outputs # index 0 = X, 1 = Y


def claim_square(coords: (int, int), current_player: str):
	# Claim if empty and return true
	if grid.squares[coords[1]][coords[0]] == DEFAULT_CHAR:
		grid.squares[coords[1]][coords[0]] = current_player
	else:
		raise IndexError


# Credit to https://stackoverflow.com/a/1056352/9071448
def check_winner(coords: (int, int), current_player: str, move_count: int):
	# alias
	x = coords[0]
	y = coords[1]

	# check col
	for i in range(N):
		if grid.squares[y][i] != current_player:
			break
		if i == N-1:
			# report win
			return True

	# check row
	for i in range(N):
		if grid.squares[i][x] != current_player:
			break
		if i == N-1:
			# report win
			return True

	# check diag
	if x == y:
		# we're on a diagonal
		for i in range(N):
			if grid.squares[i][i] != current_player:
				break
			if i == N-1:
				# report win
				return True

	# check anti diag
	if x + y == N - 1:
		for i in range(N):
			if grid.squares[i][(N-1)-i] != current_player:
				break
			if i == N-1:
				# report win
				return True

	# check draw
	if move_count == (N*N - 1):
		# report draw
		return False

	return None


def print_instructions():
	instructions = INSTRUCTIONS.format(N=N, PLAYER1=PLAYER1, PLAYER2=PLAYER2, DEFAULT_CHAR=DEFAULT_CHAR, N2=N*N)
	print(instructions)


def main():
	print_grid(grid)
	current_player = PLAYER1
	move_count = 0
	while True:
		# user action
		coords = get_input(current_player)
		try:
			claim_square(coords, current_player)
		except IndexError:
			print("coords not valid, try again")
			continue
		# print new grid state
		print_grid(grid)
		# check for winner
		is_winner = check_winner(coords, current_player, move_count)
		if is_winner is not None:
			if is_winner:
				print(f"{current_player} has won on move {move_count + 1}!")
			else:
				print("It´s a tie!")
			break
		# next player
		if current_player is PLAYER1:
			current_player = PLAYER2
		else:
			current_player = PLAYER1
		move_count += 1
	input("press enter to exit")


# initialize
# partial credit to https://www.exploratorium.edu/brain_explorer/tictactoe.html for the instructions
INSTRUCTIONS = "1. The game is played on a grid that's {N} by {N} squares.\n" \
				"2. You are \'{PLAYER1}\', your friend is \'{PLAYER2}\'. Players take turns putting their marks in empty squares.\n" \
				"3. Empty squares are shown as \'{DEFAULT_CHAR}\'.\n" \
				"4. Mark a square by entering an empty square´s coordinates separated by a space in the format \"x y\".\n" \
				"5. The first player to get {N} of their marks in a row (vertically, horizontally or diagonally) is the winner.\n" \
				"6. When all {N2} squares are full, the game is over. If no player has {N} marks in a row, the game ends as a draw.\n"
N = 3
DEFAULT_CHAR = "*"
PLAYER1 = "X"
PLAYER2 = "O"
grid = Grid()  # [Y][X]
# run
print_instructions()
input("press enter to start game")
main()
# exit
exit()
