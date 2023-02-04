xlist=[]
ylist=[]
n=int(input('Data numbers : '))
for i in range(n):
    x=float(input('X{} : '.format(i)))
    y=float(input('Y{} : '.format(i)))
    xlist.append(x)
    ylist.append(y)

def L(k,n,x): #순번k=0,1,2....,데이터수, 인수x
    L=1
    for i in range(n):
        if i!=k:
            L*=(x-xlist[i])/(xlist[k]-xlist[i])
    return L

def P(x):
    P=0
    for k in range(n):
       P+=L(k,n,x)*ylist[k]
    return P

target=float(input('At x = '))
print(P(target))