import matplotlib.pyplot as pl
import numpy

minX = int(input("min x: "))
maxX = int(input("max x: "))

x = numpy.linspace(minX, maxX, 100)

pl.plot(x, numpy.sin(x))
pl.show()
