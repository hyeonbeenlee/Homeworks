import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Functions as Func
from scipy.interpolate import CubicSpline
from sklearn.metrics import mean_squared_error as MSE
import matplotlib.offsetbox as offsetbox


def AttractionForce(d, V):
    Epsilon_0 = 8.85e-12
    r = 15.2 / 100 / 2  # m
    A = np.pi * r ** 2  # m^2
    return Epsilon_0 * A * V ** 2 / (2 * d ** 2)


Data = np.zeros((4, 6))
Data[:, 0] = [0.305, 0.140, 0.065, 0.040] # 1열
Data[:, 1] = [1.215, 0.580, 0.305, 0.180] # 2열
Data[:, 2] = [2.705, 1.270, 0.695, 0.415] # 3열
Data[:, 3] = [4.780, 2.230, 1.235, 0.745]
Data[:, 4] = [7.365, 3.400, 1.905, 1.145]
Data[:, 5] = [10.580, 4.900, 2.680, 1.670]
Data_OG=Data # gram
Data = Data / 1000 * 9.81  # N
Volts = np.array([2, 4, 6, 8, 10, 12]) * 1000  # V
Volts_Analytic = np.linspace(2, 12, 1000, endpoint=True) * 1000  # V
Dists = np.array([1, 1.5, 2, 2.5]) / 100  # m
Dists_Analytic = np.linspace(1, 2.5, 1000, endpoint=True) / 100  # m
DF = pd.DataFrame(Data, columns=Volts, index=Dists)

Func.MyPlotTemplate()
Fig1 = plt.figure(figsize=(12, 8))
Fig2 = plt.figure(figsize=(12,8))
Fig3=plt.figure(figsize=(10,10))
f1 = Fig1.add_subplot(121)
f2 = Fig1.add_subplot(122)
f3=Fig2.add_subplot(121)
f4=Fig2.add_subplot(122)
f5=Fig3.add_subplot(121)
f6=Fig3.add_subplot(122)
f1_MSE = []
f2_MSE = []

for i, dist in enumerate(Dists):
    CS = CubicSpline(Volts, Data[i, :])
    f1.plot(Volts_Analytic / 1000, CS(Volts_Analytic))
    f1.scatter(Volts / 1000, Data[i, :], label=f"Case{i + 1:02d}: {dist * 100}cm")
    f1.plot(Volts_Analytic / 1000, AttractionForce(dist, Volts_Analytic), 'k')
    f1_MSE.append(MSE(AttractionForce(dist, Volts_Analytic), CS(Volts_Analytic)))
    f5.plot(Volts_Analytic / 1000, np.abs(CS(Volts_Analytic) - AttractionForce(dist, Volts_Analytic)), label=f"Case{i + 1:02d}: {dist * 100}cm")

    CS = CubicSpline(Volts/1000, Data_OG[i, :])
    f3.plot(Volts_Analytic/1000,CS(Volts_Analytic/1000))
    f3.scatter(Volts/1000,Data_OG[i,:], label=f"Case{i + 1:02d}: {dist * 100}cm")
    f3.plot(Volts_Analytic / 1000, AttractionForce(dist, Volts_Analytic)/9.81*1000, 'k')



for i, volt in enumerate(Volts):
    CS = CubicSpline(Dists, Data[:, i])
    f2.plot(Dists_Analytic * 100, CS(Dists_Analytic))
    f2.scatter(Dists * 100, Data[:, i], label=f"Case{i + 1:02d}: {volt / 1000}kV")
    f2.plot(Dists_Analytic * 100, AttractionForce(Dists_Analytic, volt), 'k')
    f2_MSE.append(MSE(CS(Dists_Analytic), AttractionForce(Dists_Analytic, volt)))
    f6.plot(Dists_Analytic * 100, np.abs(CS(Dists_Analytic) - AttractionForce(Dists_Analytic, volt)), label=f"Case{i + 1:02d}: {volt / 1000}kV")

    CS=CubicSpline(Dists,Data_OG[:,i])
    f4.plot(Dists_Analytic*100,CS(Dists_Analytic), label=f"Case{i + 1:02d}: {volt / 1000}kV")
    f4.scatter(Dists*100,Data_OG[:,i])
    f4.plot(Dists_Analytic*100,AttractionForce(Dists_Analytic,volt)/9.81*1000,'k')



f1.set_xlabel("Voltage (kV)"), f2.set_xlabel("Distance between plates (cm)")
f3.set_xlabel("Voltage (kV)"), f4.set_xlabel("Distance between plates (cm)")
f5.set_xlabel("Voltage (kV)"), f6.set_xlabel("Distance between plates (cm)")
f1.set_ylabel("Force (N)"), f2.set_ylabel("Force (N)")
f3.set_ylabel("Weight (g)"), f4.set_ylabel("Weight (g)")
f5.set_ylabel("Force Absolute Error (N)"), f6.set_ylabel("Force Absolute Error (N)")
f1.grid(), f2.grid(), f3.grid(), f4.grid(),f5.grid(),f6.grid()
f1.legend(), f2.legend(),f3.legend(),f4.legend(),f5.legend(),f6.legend()

##텍스트박스 설정
String1 = "MSE Experimental vs Theoretical\n"
for i, mse in enumerate(f1_MSE):
    String1 += f"Case{i + 1:02d}: " + str(round(mse, 10))
    if i + 1 != len(f1_MSE):
        String1 += "\n"

String2 = "MSE Experimental vs Theoretical\n"
for i, mse in enumerate(f2_MSE):
    String2 += f"Case{i + 1:02d}: " + str(round(mse, 10))
    if i + 1 != len(f2_MSE):
        String2 += "\n"

TextBox1 = offsetbox.AnchoredText(String1, loc='center left')
TextBox2 = offsetbox.AnchoredText(String2, loc='center right')

f1.add_artist(TextBox1), f2.add_artist(TextBox2)

Fig1.tight_layout(), Fig2.tight_layout(),Fig3.tight_layout()
plt.show()
