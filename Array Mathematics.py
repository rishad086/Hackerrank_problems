import numpy as np
a=list(map(int,input().split()))
c=[]
d=[]
for i in range(a[0]):
    b = list(map(int, input().split()))
    c.append(b)
for i in range(a[0]):
    b = list(map(int, input().split()))
    d.append(b)



c=np.array(c)
d=np.array(d)
print(c+d)

print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.floor_divide(c,d))
print(np.mod(c,d))
print(np.power(c,d))