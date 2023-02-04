import matplotlib.pyplot as plt
import numpy as np
def dd(y,dy):
    ddy=2-4*y-5*dy
    return ddy

def d(y,ddy):
    dy=(2-4*y-ddy)/5
    return dy
tlen=10
h=float(input('Step size : '))
y=0
dy=0
ylog=[y]
dylog=[dy]

for i in range(int(tlen/h)):
    t=h*i
    dyp=0 #Predicts
    yp=0
    k11=dd(y,dy)
    k12=d(y,k11)
    dyp=dy+k11*h/2
    yp=y+k12*h/2
    k21=dd(yp,dyp)
    k22=d(yp,k21)
    dy=dy+k21*h
    y=y+k22*h
    ylog.append(y)
    dylog.append(dy)

x=np.arange(0,tlen+h,h)
fig=plt.figure()
f1=fig.add_subplot(211)
f2=fig.add_subplot(212)
f1.plot(x,ylog)
f1.set_title('y')
f2.plot(x,dylog)
f2.set_title('y\'')
plt.show()