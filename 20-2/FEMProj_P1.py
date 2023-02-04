import matplotlib.pyplot as plt
import numpy as np
E=30E6
A=2
def u(x):
    u=0.283/(E*A)*x**2-1.698E-5
    return u
analytic_x=np.linspace(0,60,10000)
analytic_y=[]
for i in range(10000):
    analytic_y.append(u(analytic_x[i]))
fe_2e_x=np.linspace(0,60,3)
fe_2e_y=[-16.9800E-06,-12.7350E-06,-25.4700E-36]
fe_4e_x=np.linspace(0,60,5)
fe_4e_y=[-16.9800E-06,-15.9187E-06,-12.7350E-06,-7.42875E-06,-29.7150E-36]

plt.plot(analytic_x,analytic_y,'b',label='Analytic Displacement')
plt.plot(fe_2e_x,fe_2e_y,'r',label='2 Elements FE Displacement')
plt.plot(fe_4e_x,fe_4e_y,'y',label='4 Elements FE Displacement')
plt.legend();plt.xlabel('Location X');plt.ylabel('Bar Displacement')
plt.show()