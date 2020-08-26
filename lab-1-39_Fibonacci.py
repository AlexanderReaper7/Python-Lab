from functools import lru_cache

import time as t


@lru_cache
def fib(n):
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)


n = int(input("input value for n: "))
beforeTime = t.time()

for i in range(n):
	print("{} :  {}".format(i, fib(i)))

totTime = t.time() - beforeTime
print("Total time elapsed {} seconds".format(totTime))
exit()
