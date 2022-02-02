import numpy
import scipy.optimize


def nielinowy(w):
    x = w[0]
    y = w[1]
    z = w[2]
    R = [0, 0, 0]
    R[0] = 3 * pow(y, 2) - pow(x, 2) + x - 7 - pow(z, 3)
    R[1] = 5 * pow(x, 2) + y - 21
    R[2] = 7 * pow(z, 2) + z - 5 + pow(x, 2) - pow(y, 4)
    return R


print(scipy.optimize.fsolve(nielinowy, numpy.array([0, 0, 0])))
