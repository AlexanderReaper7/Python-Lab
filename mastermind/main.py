from mastermind.master_mind_GUI import *
from random import randrange


def generate_secret_code_smart() -> [int]:  # TODO
	gen = [randrange(5) for _ in range(4)]
	if any(gen.count(val) > 1 for val in gen):
		for val in gen:
			if gen.count(val) > 1:
				val
	return gen


def generate_secret_code() -> [int]:
	"""Brute force generate a list containing non duplicated integers.
	There is a possibility of this function never returning. :)"""
	while True:
		gen = [randrange(5) for _ in range(4)]
		print(f"secret code is {gen}")
		if not any(gen.count(val) > 1 for val in gen):
			break
	return gen


def correct_answer(guess: [int], secret: [int]) -> (int, int):
	num_both = 0  # TODO: rename num_both
	num_color = 0  # TODO: rename num_color
	i = 0
	for val in guess:
		if val == secret[i]:
			num_both += 1
		elif secret.count(val) > 0:
			num_color += 1
		i += 1
	return num_both, num_color


def main():
	secret = generate_secret_code()
	window = create_GUI()
	guess_index = 0
	while True:
		# make guess
		guess = make_guess(guess_index, window)
		# correct answer?
		if guess == secret:
			gameover_screen(guess_index+1, "Winner")
			break
		# how many right colors & positions?
		(places, colors) = correct_answer(guess, secret)
		peg_feedback(guess_index, places, colors, window)
		# is the last guess?
		if guess_index >= GAME_SIZE - 1:
			gameover_screen(guess_index+1, "Loser")
			break
		guess_index += 1
	window.close()


main()
