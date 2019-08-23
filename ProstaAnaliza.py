import numpy
from matplotlib import pyplot

data_file = numpy.loadtxt('data_file.txt',delimiter=',')
time = data_file[:,0]
print(time[:10])


sensors = data_file[:,1:5]
avg = numpy.mean(sensors,axis=1)

my_data = numpy.vstack((time,sensors.T,avg))
my_data = my_data.T
numpy.savetxt('export.csv',my_data,delimiter=',')

pyplot.plot(time/60,sensors[:,1],'ro')
pyplot.plot(time/60,avg,'b.')
pyplot.show()

