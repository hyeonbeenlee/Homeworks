import numpy as np
import matplotlib.pyplot as plt
from Functions import MyPlotTemplate

X=np.linspace(-np.pi*2,np.pi*2,1000,endpoint=True)
Y1=np.sin(X)
Y2=np.cos(X)
Y3=-np.cos(X)

MyPlotTemplate()
plt.plot(X,Y1,color='k',label=r"$\Delta v_R$")
plt.plot(X,Y2,color='r',label=r"$\Delta v_L$")
plt.plot(X,Y3,color='b',label=r"$\Delta v_C$")
plt.title(r"$\omega=1$, $\phi=0$")
plt.hlines(0,-np.pi*2,np.pi*2,color='k',linewidth=3)
plt.vlines(0,-1,1,color='k',linewidth=3)
plt.xticks(np.arange(-np.pi*2,np.pi*2+0.01,np.pi/2))
plt.legend(loc=1)
plt.grid()
plt.show()