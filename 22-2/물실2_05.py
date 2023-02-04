import numpy as np
<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

class MulSil2():
    RefRCtemp = np.array([0.001, 0.00330, 0.00330, 0.01089, 0.01, 0.033])
    RefRC = np.zeros(len(RefRCtemp) * 2)
    RefRC[0::2] = RefRCtemp  # 0부터 2번씩띄우는 인덱스들
    RefRC[1::2] = RefRCtemp

    ExpRC = "0.0013 0.0012 0.0038 0.0038 0.0036 0.0039 0.0113	0.0114 0.0112	0.0112 0.0344	0.0342"
    ExpRC = ExpRC.replace("\t", " ")
    ExpRC = np.array(ExpRC.split(' '), dtype=np.float32)
    RCerr = np.abs(ExpRC - RefRC) / RefRC * 100
    RCerr = RCerr.reshape((-1, 2))

    def setEpsilon(self,epsilon):
        self.Epsilon=epsilon

    def setRC(self,R,C):
        self.R=R
        self.C=C*1e-6

    def setPlotTime(self,time):
        self.plotTime=time

    def setExpLine(self,expval):
        self.expVal=expval
    def setExpLine2(self,expval):
        self.expVal2=expval


    def PrintErr(self):
        for i in range(len(Err)):
            print(f"{self.Err[i, 0]:.2f} {self.Err[i, 1]:.2f}")

    def MyPlotTemplate(self):
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.size'] = 12
        plt.rcParams['mathtext.fontset'] = 'stix'





    def PlotRCtransient(self):
        def Q(self, t):
            return self.Epsilon * self.C * (1 - np.exp(-t / (self.R * self.C)))

        def Qoff(self,t):
            return self.Epsilon*self.C*(np.exp(-t/(self.R*self.C)))


        t=np.linspace(0,self.plotTime,1000)
        Qs=Q(self,t)
        Qs2=Qoff(self,t)

        Fig=plt.figure(figsize=(17,8))
        ax=Fig.add_subplot(1,2,1)
        ax.plot(t,Qs,color='b',label=r"$Q(t)=\varepsilon C(1-e^{-t/RC})$")
        ax.set_xlim(0,self.plotTime)
        ax.hlines(self.Epsilon*self.C*(1-np.exp(-1)),0,self.R*self.C,color='k',label=r'$\varepsilon C(1-e^{-1})$')
        ax.vlines(self.R*self.C,0,self.Epsilon*self.C*(1-np.exp(-1)),color='r',label=r"$RC_{theory}$")
        ax.vlines(self.expVal,0,self.Epsilon*self.C*(1-np.exp(-1)),color='g',label='Experiment')
        ax.annotate(f"Experiment RC={self.expVal}",(self.expVal,self.Epsilon*self.C*(1-np.exp(-1))))
        ax.set_title('Charge Process')
        ax.set_xlabel('Time (sec)')
        ax.set_ylabel("Electric Charge (Q)")
        ax.set_ylim(0,Qs[-1])
        ax.legend()
        ax.grid()

        ax=Fig.add_subplot(1,2,2)
        ax.plot(t, Qs2, color='b', label=r"$Q(t)=\varepsilon C(e^{-t/RC})$")
        ax.set_xlim(0,self.plotTime)
        ax.set_xlabel('Time (sec)')
        ax.set_ylabel("Electric Charge (Q)")
        ax.hlines(self.Epsilon * self.C * (np.exp(-1)), 0, self.R * self.C, color='k',
                  label=r'$\varepsilon C(e^{-1})$')
        ax.vlines(self.R * self.C, 0, self.Epsilon * self.C * (np.exp(-1)), color='r', label=r"$RC_{theory}$")
        ax.vlines(self.expVal2, 0, self.Epsilon * self.C * (np.exp(-1)), color='g', label='Experiment')
        ax.annotate(f"Experiment RC={self.expVal2}",(self.expVal2,self.Epsilon * self.C * (np.exp(-1))))
        ax.set_ylim(Qs2[-1], Qs2[0])
        ax.legend()
        ax.grid()
        ax.set_title('Discharge Process')


        Fig.suptitle(f"R={self.R} $\Omega$, C={self.C*1e6:.0f}$\mu F$",fontsize=16)
        Fig.tight_layout()
        plt.show()






if __name__ == "__main__":
    MS = MulSil2()
    MS.MyPlotTemplate()
    MS.setEpsilon(5)
    MS.setRC(100,330)
    MS.setExpLine(0.0344) #실험충전시간
    MS.setExpLine2(0.0342) #실험방전시간
    MS.setPlotTime(0.035)
    MS.PlotRCtransient()
=======
import Functions as Func
import matplotlib.pyplot as plt

def calc_r(x,y):
    return(x**2+y**2)/(2*y)

def calc_B(I):
    N=320 #횟수
    R=0.0625 #m
    mu0=4e-7*np.pi
    return (4/5)**(3/2)*(mu0*N*I)/R

def calc_EM(V,r,B):
    return 2*V/(r**2*B**2)

def calc_Err(ExpEM):
    Ref=1.76e11
    return np.abs((Ref-ExpEM)/Ref*100)
    # return np.abs(Ref-ExpEM)
    
def printeach(itterable,**kwargs):
    if 'title' in kwargs.keys():title=kwargs['title']
    if 'ptype' in kwargs.keys():ptype=kwargs['ptype']
    it_len=len(itterable)
    print(title)
    for i in range(it_len):
        print(f"{itterable[i]:{ptype}}")
    print()

def calc_All(HighVoltage):
    x=np.array([0.10,0.09,0.08,0.07,0.06])
    y=np.full(5,0.01)
    V=np.full(5,HighVoltage)
    if HighVoltage==2000:
        I=np.array([0.07,0.08,0.1,0.13,0.18])
    elif HighVoltage==4000:
        I=np.array([0.09,0.12,0.14,0.19,0.26])
    elif HighVoltage==6000:
        I=np.array([0.12,0.15,0.18,0.23,0.32])
    B=calc_B(I)
    r=calc_r(x,y)
    ExpEM=calc_EM(V,r,B)
    ExpErr=calc_Err(ExpEM)
    return B,r,ExpEM,ExpErr

HVs=[2000,4000,6000]

Xaxis=range(5)
XaxisLabels=[f'X={10-x}' for x in Xaxis]
Colors=['r','g','b']
Ref=1.76e11

Func.MyPlotTemplate()
Fig=plt.figure(figsize=(12,6))
ax=Fig.add_subplot(121)
ax2=Fig.add_subplot(122)

Errors=[]
Measures=[]
for idx,HighVoltage in enumerate(HVs):
    # HighVoltage=6000
    B,r,ExpEM,ExpErr=calc_All(HighVoltage)
    ax.scatter(Xaxis,ExpEM,s=1e2,color=Colors[idx],label=f"{HVs[idx]/1000} kV")
    ax2.plot(Xaxis,ExpErr,'-o',color=Colors[idx],label=f"{HVs[idx]/1000} kV")
    print(f"Ua={HighVoltage} \nMean Error {np.mean(ExpErr):.2f} %")
    print(f"Min Error {np.min(ExpErr):.2f} %\n({XaxisLabels[np.argmin(ExpErr)]})")
    print(f"Max Error {np.max(ExpErr):.2f} %\n({XaxisLabels[np.argmax(ExpErr)]})")
    print(f"Std {np.std(ExpErr):.3e}")
    print(f"Std of Values {np.std(ExpEM):.3e}")
    print()
    Errors.append(ExpErr)
    Measures.append(ExpEM)

print(f"Entire std of error={np.std(np.squeeze(np.array(Errors))):.3e}")
print(f"Entire std of values={np.std(np.squeeze(np.array(Measures))):.3e}")
print(f"Entire mean of values={np.mean(np.squeeze(np.array(Measures))):.3e}")
    
    
    
ax.set_xticks(Xaxis),ax.set_xticklabels(XaxisLabels)
ax.set_xlim(-0.5,4.5),ax.set_xlabel("Y=1 Fixed",fontsize=20)
ax.set_ylim(Ref-1e11,Ref+1e11),ax.set_ylabel("Value (C/kg)")
Ytick=np.linspace(1,2.75,5,endpoint=True)*1e11
Ytick=np.sort(np.append(Ytick,Ref))
ax.set_yticks(Ytick)
ax.set_title("Experimental Values")
ax.hlines(Ref,-0.5,4.5,label=r'1.76$\times10^{11}$',linewidth=5,color='k')
ax.legend(title='$U_a$ and Reference'),ax.grid()

ax2.set_xticks(Xaxis),ax2.set_xticklabels(XaxisLabels)
ax2.set_xlabel("Y=1 Fixed",fontsize=20)
ax2.set_ylabel("Absolute Relative Error (%)"), ax2.set_ylim(0,100)
ax2.legend(title='$U_a$'),ax2.grid()
ax2.set_title("Error")


Fig.tight_layout()
plt.show()

# printeach(B,title='자기장',ptype='.6f')
# printeach(r,title='r',ptype='.3f')
# printeach(ExpEM,title='e/m Experiment',ptype='.4e')
# printeach(ExpErr,title='e/m Error',ptype='.2f')
>>>>>>> b266102733032321ef6d222c4915035dbf15b775
