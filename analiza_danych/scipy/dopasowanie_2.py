import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sy
import pylab as plb
import numpy as np
import csv
from lmfit import Model
from math import pi

np.seterr(divide="ignore", invalid="ignore")

x = []
y = []

with open("Proba.csv") as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter=";")
    for wiersz in czytnikCSV:
        x.append(int(wiersz[1]))
        y.append(float(wiersz[0]))


def gauss(x, A, mu, sigma):
    x = np.array(x)
    return A * np.exp(-1 * (x[:] - mu) * (x[:] - mu) / sigma / sigma)


def sincSquare(x, A, mu, sigma):
    return A * np.sinc(pi * x * sigma) ** 2 + mu


p0 = [0.68, 0, 1 / 17]
coeffs, matcov = curve_fit(sincSquare, x, y, p0, maxfev=50000)

print(coeffs)
print(matcov)

xaj = np.linspace(-5, 60, num=500)
yaj = sincSquare(xaj, coeffs[0], coeffs[1], coeffs[2])

plt.plot(x, y, "x", xaj, yaj, "r-")
plt.xlabel("odleglosc [cm]")
plt.ylabel("kontrast między jasnymi i ciemnymi prążkami")
plt.show()
