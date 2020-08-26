import matplotlib.pyplot as pl
import numpy

while True:
	try:
		minX = int(input("min x: "))
		maxX = int(input("max x: "))
	except ValueError:
		print("input is not a valid integer, try again.")
	else:
		break

x = numpy.linspace(minX, maxX, 100)

pl.plot(x, numpy.sin(x))
pl.show()
