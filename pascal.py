from functools import lru_cache


@lru_cache
def pascal(k, i):
	if i == 0 or k == i: return 1
	if k == i - 1 or i == 1: return k
	return pascal(k-1, i-1) + pascal(k-1, i)

def pascal_triangle(n):
	output = []
	for i in range(n):
		temp = []
		for j in range(i+1):
			temp.append(pascal(i,j))
		output.append(temp)
	return output

def print_pascal_triangle(n):
	values = pascal_triangle(n)
	for i in range(n):
		for j in range(i+1):
			print(values[i][j], end=" ")
		print()

N = int(input("input value for n: "))
#print(pascal_triangle(N))
print_pascal_triangle(N)
exit()