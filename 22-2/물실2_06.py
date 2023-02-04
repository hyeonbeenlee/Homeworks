import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Akima1DInterpolator as akispl
from Functions import MyPlotTemplate
from sklearn.metrics import mean_squared_error as mse
sklearn.metrics.

# A
# L=X_B[-1], B=B_List[-1]
X_A=np.arange(0.5,3.1,0.5) #Ampere
F_A=np.array([0.64,1.12,1.59,2.04,2.50,2.96]) #gram
F_A*=9.81/1000 #Newton

#B
# I=3A, B=B_List[-1]
X_B=np.array([12,22,32,42,32*2,42*2])/1000 #Meter
F_B=np.array([0.41,0.80,1.16,1.54,2.23,2.96]) #gram
F_B*=9.81/1000

#C
X_C=np.arange(1,7,1) #None
F_C=np.array([0.64,1.19,1.65,2.20,2.68,2.96]) #gram
F_C*=9.81/1000
I=3 #Ampere
L=X_B[-1]
B_List=F_C/(I*L)

MyPlotTemplate()
Fig1=plt.figure(figsize=(10,6))
ax=Fig1.add_subplot(111)
rect=ax.bar(X_C,B_List,color='g')
ax.bar_label(rect)
ax.grid()
ax.set_xlabel('Number of magnets'), ax.set_ylabel(r'$\Vert \vec{B} \Vert_2$ $(N/{Am}=Tesla)$')
Fig1.tight_layout()


#A
L=X_B[-1]
B=B_List[-1]
X_A_analytic=np.linspace(0.5,3,1000,endpoint=True)
F_A_analytic=X_A_analytic*L*B
Interpol=akispl(X_A,F_A)

Fig2=plt.figure(figsize=(10,6))
ax=Fig2.add_subplot(111)
ax.plot(X_A,F_A,'o',color='r',label='Experiment (Discrete)')
ax.plot(X_A_analytic,Interpol(X_A_analytic),color='cyan',label='Experiment (Interpolated)')
ax.plot(X_A_analytic,F_A_analytic,color='k', label='Analytic')
RMSEvalue=np.sqrt(mse(Interpol(X_A_analytic), F_A_analytic))
ax.set_title(f"RMSE: {RMSEvalue:.4e}\nRelative RMSE: {RMSEvalue/np.mean(Interpol(X_A_analytic))*100:.3f}%")
ax.set_xlabel('I (A)'), ax.set_ylabel(r"$\Vert \vec{F_B} \Vert_2$ $(N)$")
ax.set_xticks(X_A)
ax.grid()
ax.legend()
Fig2.tight_layout()

#B
I=X_A[-1]
B=B_List[-1]
X_B_analytic=np.linspace(X_B[0],X_B[-1],1000,endpoint=True)
F_B_analytic=I*B*X_B_analytic
Interpol=akispl(X_B,F_B)

Fig3=plt.figure(figsize=(10,6))
ax=Fig3.add_subplot(111)
ax.plot(X_B,F_B,'o',color='r',label='Experiment (Discrete)')
ax.plot(X_B_analytic,Interpol(X_B_analytic),color='green',label='Experiment (Interpolated)')
ax.plot(X_B_analytic,F_B_analytic,color='k', label='Analytic')
RMSEvalue=np.sqrt(mse(Interpol(X_B_analytic), F_B_analytic))
ax.set_title(f"RMSE: {RMSEvalue:.4e}\nRelative RMSE: {RMSEvalue/np.mean(Interpol(X_B_analytic))*100:.3f}%")
ax.set_xlabel('L (m)'), ax.set_ylabel(r"$\Vert \vec{F_B} \Vert_2$ $(N)$")
ax.set_xticks(X_B)
ax.grid()
ax.legend()
Fig3.tight_layout()

#C
I=X_A[-1]
L=X_B[-1]
X_C_analytic=np.linspace(X_C[0],X_C[-1],1000,endpoint=True)
Interpol=akispl(X_C,F_C)
F_C_analytic=Interpol(X_C_analytic)

Ideal_X_C=np.linspace(X_C[0],X_C[-1],1000,endpoint=True)
Ideal_F_C=np.linspace(F_C[0],F_C[-1],1000,endpoint=True)

Fig4=plt.figure(figsize=(10,6))
ax=Fig4.add_subplot(111)
ax.plot(X_C,F_C,'o',color='r',label='Experiment (Discrete)')
ax.plot(X_C_analytic,Interpol(X_C_analytic),color='magenta',label='Experiment (Interpolated)')
ax.plot(Ideal_X_C,Ideal_F_C,color='k',label='Linear Increase')
RMSEvalue=np.sqrt(mse(Interpol(X_C_analytic), Ideal_F_C))
ax.set_title(f"RMSE: {RMSEvalue:.4e}\nRelative RMSE: {RMSEvalue/np.mean(Interpol(X_C_analytic))*100:.3f}%")
ax.set_xlabel('Number of magnets'), ax.set_ylabel(r"$\Vert \vec{F_B} \Vert_2$ $(N)$")
ax.set_xticks(X_C)
ax.grid()
ax.legend()
Fig4.tight_layout()

Fig5=plt.figure(figsize=(10,6))
ax=Fig5.add_subplot(111)
X=np.linspace(0,np.pi*2,1000,endpoint=True)
Y=np.sin(X)
ax.plot(X,Y,color='green',label='Sine')
ax.vlines(np.pi/2,0,1)
ax.annotate(r"$x=90\degree$",(np.pi/2,0))
ax.set_xlabel(r"$x$ $(rad)$"), ax.set_ylabel(r"$y$")
ax.grid()
ax.set_xlim(X[0],X[-1])
ax.legend()
Fig5.tight_layout()

plt.show()






