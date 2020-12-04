# def destructive_recursive_max(input: [int]):
# 	lst = input.copy()
# 	if len(lst) == 1:
# 		return lst[0]
# 	if lst[0] >= lst[len(lst)-1]:
# 		del lst[len(lst)-1]
# 	else:
# 		del lst[0]
# 	return destructive_recursive_max(lst)
#

def recursive_max(lst: [int]):
	if len(lst) == 1:
		return lst[0]
	if lst[0] >= lst[len(lst)-1]:
		return recursive_max(lst[0:len(lst)-1])
	else:
		return recursive_max(lst[1:len(lst)])


def main():
	numbers = [1, 13, 2, 65, 11, 13, 0, -1, -65, -65]
	print(numbers)
	print(recursive_max(numbers))
	print(numbers)


main()
