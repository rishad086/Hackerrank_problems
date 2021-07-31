import numpy
a=input().split()
a=map(int,a)

a=list(a)
a=numpy.array(a)
a=numpy.reshape(a,(3,3))
print(a)
