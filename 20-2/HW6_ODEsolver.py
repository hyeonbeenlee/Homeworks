import numpy as np
import matplotlib.pyplot as plt

def F(t):
    F=160*np.cos(2*t)
    return F

m=100
k=64
c=0.5
tlen=20
h1=0.1
h2=0.01

#mx''+cx'+kx=F(t)
def ddx(dx,x,t): #2계미분
    ddx=(F(t)-k*x-c*dx)/m
    return ddx

def dx(ddx,x,t): #1계미분
    dx=(F(t)-m*ddx-k*x)/c
    return dx

#Step 1로, Euler method
t=0 #initial time
x=0 #initial x
v=0 #initial x'
euler_h1v=[0]
euler_h1x=[0]
for i in range(0,int(tlen/h1+1),1):
    t=h1*i
    v=v+ddx(v,x,t)*h1
    x=x+dx(ddx(v,x,t),x,t)*h1
    euler_h1v.append(v)
    euler_h1x.append(x)
print("Euler's method with step size {}\nVelocities : {}\nPositions : {}\n".format(h1,euler_h1v,euler_h1x))

#Step 2로, Euler method
t=0 #initial time
x=0 #initial x
v=0 #initial x'
euler_h2v=[0]
euler_h2x=[0]
for i in range(0,int(tlen/h2+1),1):
    t=h2*i
    v=v+ddx(v,x,t)*h2
    x=x+dx(ddx(v,x,t),x,t)*h2
    euler_h2v.append(v)
    euler_h2x.append(x)
print("Euler's method with step size {}\nVelocities : {}\nPositions : {}\n".format(h2,euler_h2v,euler_h2x))

#Step 1로, Heun's method
t=0 #initial time
x=0 #initial x
v=0 #initial x'
heun_h1v=[0]
heun_h1x=[0]
for i in range(0,int(tlen/h1+1),1):
    t=h1*i
    k12=ddx(v,x,t) #초기 2계기울기
    k11=dx(k12,x,t) #초기 1계기울기

    #Predictor
    vtemp=v+k12*h1 #예측 1계 함수값
    xtemp=x+k11*h1 #예측 0계 함수값
    k22=ddx(vtemp,xtemp,t) #예측 2계기울기
    k21=dx(k22,xtemp,t) #예측 1계기울기

    #Corrector
    v=v+(k12+k22)/2*h1
    x=x+(k11+k21)/2*h1

    heun_h1v.append(v)
    heun_h1x.append(x)
print("Heun's method with step size {}\nVelocities : {}\nPositions : {}\n".format(h1,heun_h1v,heun_h1x))

#Step 2로, Heun's method
t=0 #initial time
x=0 #initial x
v=0 #initial x'
heun_h2v=[0]
heun_h2x=[0]
for i in range(0,int(tlen/h2+1),1):
    t=h2*i
    k12=ddx(v,x,t) #초기 2계기울기
    k11=dx(k12,x,t) #초기 1계기울기

    #Predictor
    vtemp=v+k12*h2 #예측 1계 함수값
    xtemp=x+k11*h2 #예측 0계 함수값
    k22=ddx(vtemp,xtemp,t) #예측 2계기울기
    k21=dx(k22,xtemp,t) #예측 1계기울기

    #Corrector
    v=v+(k12+k22)/2*h2
    x=x+(k11+k21)/2*h2

    heun_h2v.append(v)
    heun_h2x.append(x)
print("Heun's method with step size {}\nVelocities : {}\nPositions : {}\n".format(h2,heun_h2v,heun_h2x))

x1=np.arange(0,20+2*h1,h1)
x2=np.arange(0,20+2*h2,h2)
fig=plt.figure()
f1=fig.add_subplot(211)
f2=fig.add_subplot(212)
f1.set_title('Velocity')
f1.plot(x1,euler_h1v,label='Euler 0.1')
f1.plot(x1,heun_h1v,label='Heun 0.1')
f1.plot(x2,euler_h2v,label='Euler 0.01')
f1.plot(x2,heun_h2v,label='Heun 0.01')
f1.legend(loc='lower left')
f1.grid()

f2.set_title('Position')
f2.plot(x1,euler_h1x,label='Euler 0.1')
f2.plot(x1,heun_h1x,label='Heun 0.1')
f2.plot(x2,euler_h2x,label='Euler 0.01')
f2.plot(x2,heun_h2x,label='Heun 0.01')
f2.legend(loc='lower left')
f2.grid()

plt.show()