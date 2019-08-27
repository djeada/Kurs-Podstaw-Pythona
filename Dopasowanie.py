import numpy
import matplotlib.pyplot as plt
import scipy.interpolate as inter
import random

dane_x = numpy.array([0, 0.2, 0.5, 0.7, 1.1, 1.8, 2.2, 2.5])
dane_y = numpy.array([numpy.exp(x) + random.uniform(-1,1) for x in dane_x])


x = numpy.linspace(0,2.5)

f1 = inter.interp1d(dane_x,dane_y)
y1 = f1(x)

plt.subplot(2,2,1)
plt.plot(dane_x,dane_y,linestyle='None', marker='+',markersize=20)
plt.plot(x,y1)
plt.title('Liniowo')

f2 = inter.interp1d(dane_x,dane_y,kind='cubic')
y2 = f2(x)

plt.subplot(2,2,2)
plt.plot(dane_x,dane_y,linestyle='None', marker='+',markersize=20)
plt.plot(x,y2)
plt.title('Wielomianowo')

y_eksponens = numpy.exp(x)

plt.subplot(2,2,3)
plt.plot(dane_x,dane_y,linestyle='None', marker='+',markersize=20)
plt.plot(x,y_eksponens)
plt.title('Eksponencjalnie')

plt.show()

