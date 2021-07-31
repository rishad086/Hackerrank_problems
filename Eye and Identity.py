import  numpy
numpy.set_printoptions(legacy="1.13")
i=list(map(int,input().split()))
print (numpy.eye(i[0], i[1], k = 0))