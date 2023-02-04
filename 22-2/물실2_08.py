import pandas as pd
import matplotlib.pyplot as plt
import DataProcessing as DP
import numpy as np

Data=pd.read_csv("C:\\Users\LHB-MSLab\Documents\카카오톡 받은 파일\실험데이터\exp-b\\power.txt",skiprows=[0], sep='\t')

Data.columns=['Time','Power']



DP.MyPlotTemplate()
Fig=plt.figure()
ax=Fig.add_subplot(111)
# ax.plot(Data['Time'],Data['Power'],c='k',linewidth=1)
ax.plot(Data['Time'],Data['Power'],c='k',linewidth=0.5)
# ax.plot(Data2['Time'],Data2['U'])
ax.grid()
ax.set_xlabel('Time (sec)')
ax.set_ylabel(r'Power $(mW)$')
ax.set_xlim(Data['Time'].iloc[0],Data['Time'].iloc[-1])
ax.annotate(f"Max={Data['Power'].max()}",(Data['Time'].iloc[Data['Power'].argmax()],Data['Power'].max()))
ax.annotate(f"Min={Data['Power'].min()}",(Data['Time'].iloc[Data['Power'].argmin()],Data['Power'].min()))


Fig.tight_layout()
plt.show()