import numpy as np
a=(input().split())
a=map(int,a)
a=list(a)
matrix=[]

for i in range(a[0]):


    c = (input().split())
    c = map(int, c)
    c = list(c)

    matrix.append(c)

matrix=np.reshape(matrix,(a[0],a[1]))
print(np.transpose(matrix))
print(matrix.flatten())




