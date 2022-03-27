import math
x=int(input())
y=int(input())
u=(math.sqrt(x**2+y**2))/2
y=y/2
angle=round(math.degrees(math.acos(y/u)))
print(angle)
print(str(angle)+chr(248))

