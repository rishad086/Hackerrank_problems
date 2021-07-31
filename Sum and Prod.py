x=list(map(int,input().split()))
c=[]
for i in range(x[0]):
    x=list(map(int,input().split()))
    c.append(x)

import numpy as np
c=np.array(c)

print(np.prod(np.sum(c,axis=0),axis=None))