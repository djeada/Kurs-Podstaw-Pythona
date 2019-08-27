import numpy
import random
import math
import matplotlib.pyplot as plt
import scipy.interpolate

dane_x = numpy.array([0,0.2,0.5,0.7,1.1,1.8,2.0,2.1,2.5])
dane_y = [math.exp(x) + random.uniform(-1,1) for x in dane_x]
plt.plot(dane_x,dane_y,marker='+',linestyle='None',markersize=20)


x = numpy.linspace(0,2.5)

f1 = scipy.interpolate.interp1d(dane_x,dane_y)
y1 = f1(x)
plt.plot(x,y1,marker='None')

f2 = scipy.interpolate.interp1d(dane_x,dane_y,kind='cubic')
y2 = f2(x)
plt.plot(x,y2,marker='None')

y_eksponens = numpy.exp(x)
plt.plot(x,y_eksponens)

plt.show()
