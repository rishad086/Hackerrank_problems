x=list(map(int,input().split()))
c=[]
for i in range(x[0]):
    x = list(map(int, input().split()))
    c.append(x)

import numpy as np
x=np.array(c)
print(np.max(np.min(x,axis=1),axis=0))
