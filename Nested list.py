x = [];
y = int(input())
for i in range(y):
    name = input()
    score = float(input())

    x.append([name, score])


p = []

for name, score in x:
    p.append(score)
    p.sort()


c = p[1]

i=0
while i<5:
    if p[i]<c and c<=p[i+1]:
        c=p[i+1]
        break


d = []

for name, score in x:
    if c == score:
        d.append(name)

d.sort()

for i in d:
    print(i)
