a=input().split()
n=int(a[0])
m=int(a[1])
c=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
o=0
for i in c:
    if i in a:
        o=o+1

for i in c:
    if i in b:
        o=o-1



print(o)

