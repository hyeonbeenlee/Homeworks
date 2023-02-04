import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Functions as Func


## 실험1
# Experiment=np.array([198.4,2942,1966,295.6,99.7])
# Theory=np.array([200,3000,2000,300,100])
# Experiment,Theory=np.sort(Experiment),np.sort(Theory)
# Error=np.abs(Theory-Experiment)
#
# # print(Theory)
# # print(Experiment)
# # print(Error)
# # print(Error/Theory*100)
#
#
# Func.MyPlotTemplate()
#
# Fig1=plt.figure(figsize=(10,10))
# f1=Fig1.add_subplot(211)
# f2=Fig1.add_subplot(212)
#
#
#
#
#
#
# f1.set_xticks(range(0,3001,100))
# f1.plot(Theory,np.log10(Theory),'-o',color='b',label='Theoretical value',zorder=2)
# f1.plot(Theory,np.log10(Experiment),'-o',color='m',label='Marked value',zorder=1)
# f1.set_xlim(0,3100)
# # f1.set_ylim(0,3100)
# f1.set_ylabel('Resistance Value'+r"$(\log_{10}\ Scale)$")
# ax1=f1.twinx()
# ax1.set_ylabel('Absolute Error'+r"$(\Omega)$")
# ax1.set_ylim(0,70)
# ax1.bar(Theory,Error,color='r',width=50,label='Abs. Error',zorder=0)
# ax1.legend(loc=4)
#
#
#
#
# f1.grid()
# f2.grid()
# f1.legend()
#
# plt.tight_layout()
# plt.show()



#### 실험2
V=[1,2,3,4,5]
R_th1=np.full(5,99.7)
R_th2=np.full(5,198.4)
I_exp1=np.array([10.18,19.41,29.20,38.44,47.70])/1000 #100 Ohm (A)
I_exp2=np.array([4.99,10.14,14.93,19.70,24.91])/1000 #200 Ohm (A)

R_exp1=np.round(V/I_exp1,2)
R_exp2=np.round(V/I_exp2,2)

Func.MyPlotTemplate()
fig1=plt.figure(figsize=(10,5))
f1=fig1.add_subplot(121)
f2=fig1.add_subplot(122)

f1.plot(V,R_th1,'-o',color='k',label='Real resistance')
f1.plot(V,R_exp1,'-o',color='r',label="Using Ohm's law")
f1.set_ylim(90,110)
f1.set_xticks(range(1,6))
f1.set_xlabel('Voltage (V)')
f1.set_ylabel('Resistance '+r"$(\Omega)$")
f1.set_title(r"100 $(\Omega)$ Case")

f2.plot(V,R_th2,'-o',color='k',label='Real resistance')
f2.plot(V,R_exp2,'-o',color='r',label="Using Ohm's law")
f2.set_ylim(190,210)
f2.set_xticks(range(1,6))
f2.set_xlabel('Voltage (V)')
f2.set_ylabel('Resistance '+r"$(\Omega)$")
f2.set_title(r"200 $(\Omega)$ Case")


f1.grid()
f2.grid()
f1.legend()
f2.legend()
fig1.tight_layout()
# plt.show()

print(np.mean(R_exp1))
print(np.mean(R_exp2))