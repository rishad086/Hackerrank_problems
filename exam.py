list=[]
#print(list)
for i in range(0,6):
    list1 = []
    for j in range(0,7):

        x=int(input())
        list1.append(x)
    list.append(list1)
print(list)

for j in list:
    for i in range(0,7):
        if j[i]==1:
            print("*",end=' ')
        else:
            print("-",end=' ')
    print('\n')




