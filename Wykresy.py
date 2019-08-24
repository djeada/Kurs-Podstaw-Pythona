import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(-3,3,100)
y1 = numpy.sin(x)
y2 = numpy.exp(x)

plt.plot(x,y1,color='green',marker='o')
plt.plot(x,y2,color='blue',marker='+',linewidth=3,linestyle='None')
plt.xlabel('argumenty')
plt.ylabel('wartości')
plt.legend(['sin(x)','exp(x)'])
plt.ylim([-1,1])
plt.savefig('wykresik.png')
plt.show()
