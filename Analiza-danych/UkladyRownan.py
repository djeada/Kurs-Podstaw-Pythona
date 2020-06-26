import numpy

A = numpy.array([[1,3],[3,-6]])
B = numpy.array([11,3])
Z = numpy.linalg.solve(A,B)
print(Z)

A = numpy.array([[1,-7,3],[2,5,-1],[1,1,1]])
B = numpy.array([2,-8,5])
Z = numpy.linalg.solve(A,B)
print(Z)
