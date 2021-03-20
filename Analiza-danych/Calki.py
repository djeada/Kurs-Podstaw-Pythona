import sympy
import scipy.integrate
import numpy
import matplotlib.pyplot as pyplot

x = sympy.Symbol("x")
print(sympy.integrate(pow(x, 2) - 3 * pow(x, 3) + x - 25, x))


def funkcja(x):
    return pow(x, 2) - 3 * pow(x, 3) + x - 25


wynik = scipy.integrate.quad(funkcja, 0, 1)
print(wynik[0])

z = numpy.linspace(-1, 3)
pyplot.plot(z, funkcja(z))
pyplot.show()
