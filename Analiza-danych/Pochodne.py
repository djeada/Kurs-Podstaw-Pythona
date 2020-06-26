import numpy
import matplotlib.pyplot as pyplot
import sympy
import scipy.misc

x = sympy.Symbol('x')
print(sympy.diff(5*pow(x,2)-x+16,x))

def funkcja(x):
    return 5*pow(x,2)-x+16

print(scipy.misc.derivative(funkcja,1))

z = numpy.linspace(-5,5)

pyplot.plot(z,funkcja(z))
pyplot.plot(z,scipy.misc.derivative(funkcja,z))
pyplot.show()
