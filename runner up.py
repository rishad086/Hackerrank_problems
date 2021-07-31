def LinearSearch(list,u):
    c=-1
    for i in list:
        c=c+1
        if i==u:
            return True,c
    return False,None




list=[]
x=int(input("enter the number of values u want"))
print("enter the values")
i=0
while i<x:
    y=int(input())
    list.append(y)
    i=i+1

print("enter the value u want")
u=int(input())
t,r=LinearSearch(list,u)
print(list[r+1:])

if t==True:
    print("Found","index value=",r)
    e,v= LinearSearch(list[r+1:],u)
    if e==True:
        print("Found Again", "index value=", v+r)

else:
    print("Not Found")

