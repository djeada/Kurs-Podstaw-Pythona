import numpy
import matplotlib.pyplot as pyplot
import sympy
import scipy.misc

x = sympy.Symbol('x')
print(sympy.diff(3*x**2+1,x))

def function(x):
    return 3*x**2 + 1

print(scipy.misc.derivative(function,2.0))

z = numpy.linspace(-5,5)

pyplot.plot(z,function(z))
pyplot.plot(z,scipy.misc.derivative(function,z))
pyplot.show()

