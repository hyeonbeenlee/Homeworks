import matplotlib.pyplot as plt
import numpy as np
def v(x):
    v=(12500/3*x**4-200000/3*x**3+1000000/3*x**2-1600000/3*x)/(200*10**5)
    return v

analytic_x=np.linspace(0,8,10000)
analytic_y=[]
for i in range(10000):
    analytic_y.append(v(analytic_x[i]))

fe_x=np.linspace(0,8,11)
fe_y=[-110.000e-33,-4.77862e-03,-6.91194e-03,-5.63195e-03,-2.21865e-03,-460.000e-33,-2.21865e-03,-5.63195e-03,-6.91194e-03,-4.77862e-03,-110.000e-33]

plt.plot(analytic_x,analytic_y,label='Analytic Displacement')
plt.plot(fe_x,fe_y,label='FE Displacement of 10 Beam Elements')
plt.xlabel('Location');plt.ylabel('Deflection')
plt.legend(loc='upper left')
plt.xlim(0,8);plt.ylim(-0.015,0.005)
plt.show()
