import numpy as np
def f(x):
    y=np.exp(x)*np.sin(x)
    return y

xmin=0
xmax=np.pi/2
aI=2.9052 #Analytic value
kill=0 #Dummy for while-loop
while kill==0:
    n=int(input('Number of intervals?(Multiples of 3 only) : '))
    bounds=np.linspace(xmin,xmax,n+1) #Boundary values
    h=bounds[1]-bounds[0] #Step size
    nI=0

    for i in range(0,n-2,3): #n=0,3,6...n-3
        nI+=3/8*h*(f(bounds[i])+3*f(bounds[i+1])+3*f(bounds[i+2])+f(bounds[i+3]))

    e=abs((aI-nI)/aI*100) #%rel error
    print('Simpson''s 3/8 yields {} with {} intervals.'.format(nI,n))
    print('% relative error : {}%\n'.format(e))