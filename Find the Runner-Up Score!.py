x=int(input())
y=input().split(" ")
m=[]
for i in y:
    if int(i) not in m:
        m.append(int(i))
m.sort()
if len(m)>2:
    print(m[len(m)-2])
elif len(m)==2:
    print(m[0])
else:
    print(m[0])

