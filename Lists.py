x=int(input())
list=[]
for i in range(0,x):
    y=input().split()


    if y[0]=='insert':

        list.insert(int(y[1]),int(y[2]))


    elif(y[0]=='remove'):

        list.remove(int(y[1]))

    elif(y[0]=='append'):

        list.append(int(y[1]))

    elif(y[0]=='sort'):
        list.sort()

    elif(y[0]=='pop'):
        list.pop()


    elif(y[0]=='print'):
        print(list)
    else:
        list.reverse()







