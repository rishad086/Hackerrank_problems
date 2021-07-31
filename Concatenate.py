import numpy as np
a=(input().split())
a=map(int,a)
a=list(a)
matrix1=[]
matrix2=[]
for i in range(a[0]):


    c = (input().split())
    c = map(int, c)
    c = list(c)

    matrix1.append(c)

for i in range(a[1]):


    c = (input().split())
    c = map(int, c)
    c = list(c)
    matrix2.append(c)

print(np.concatenate((matrix1, matrix2), axis=0))




