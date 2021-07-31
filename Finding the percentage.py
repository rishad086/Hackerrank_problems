x=int(input())
y={}

for i in range(x):

    name,*rest=input().split()




    marks=list(map(float,rest))



    y[name]=marks
q=input()


for i,j in y.items():
  if i==q:

   avg=sum(j)/3
print('%.2f'%avg)





