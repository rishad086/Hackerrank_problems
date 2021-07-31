import numpy as np
np.set_printoptions(legacy="1.13")

a=list(map(float,input().split()))
x=np.array(a)
print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))