"""Module for utilizing A* on a 2D grid"""

import math
from A_Star.grid import Occupation

neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, path, node):
	path.append(node)
	# if the path has hit a dead end (endless loop), the path is complete.
	if came_from[node] == node:
		return path
	else:
		return reconstruct_path(came_from, path, came_from[node])


def eval_node(grid, scores, open_set, came_from, goal: (int, int), node: (int, int)):
	for (x, y) in neighbors:
		coordx = node[0]+x
		coordy = node[1]+y
		print(f"node {coordx},{coordy}")
		if coordx < 0 or coordx >= len(grid):
			print("X out of bounds")
			continue
		if coordy < 0 or coordy >= len(grid[0]):
			print("Y out of bounds")
			continue

		# Correct path if goal is found
		# Skip if blocked
		if grid[coordx][coordy] == Occupation.BLOCKED:
			print("Blocked")
			continue
		# Skip if start square
		if grid[coordx][coordy] == Occupation.START:
			print("Start")
			continue

		# Calculate costs
		# distance to goal
		dist = distance((coordx, coordy), goal)
		# path length
		path_len = scores[node] + 1

		# store cost in dictionary
		if (coordx, coordy) in scores:
			# if the stored path length if greater than the new, store new.
			if scores[(coordx, coordy)] > path_len:
				scores[(coordx, coordy)] = path_len
				came_from[(coordx, coordy)] = node
				open_set[(coordx, coordy)] = path_len + dist
		else:
			scores[(coordx, coordy)] = path_len
			came_from[(coordx, coordy)] = node
			open_set[(coordx, coordy)] = path_len + dist

		if grid[coordx][coordy] == Occupation.GOAL:
			print("Goal")
			return reconstruct_path(came_from, [], (coordx, coordy))

	return None


def a_star(grid, start: (int, int), goal: (int, int)):
	"""Function to calculate a path through a grid"""

	scores: {(int, int): (int, int)} = {start: 0}  # (x,y): path length
	came_from: {(int, int): (int, int)} = {start: start}  # (x,y): parent
	open_set: {(int, int): int} = {start: distance(start, goal)}  # (x,y): total

	while len(open_set) > 0:
		current = min(open_set.items(), key=lambda x: x[1])

		result = eval_node(grid, scores, open_set, came_from, goal, current[0])
		if result is not None:
			result.reverse()
			print(f"Found path: {result}")
			return result
		del(open_set[current[0]])

	return None
