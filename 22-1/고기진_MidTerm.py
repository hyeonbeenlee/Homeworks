import numpy as np
import matplotlib.pyplot as plt

def Grad(t, Y):
    global J,C,K
    x = Y[0]
    xDot = Y[1]
    dY = np.zeros((2, 1))
    dY[0] = xDot
    dY[1] = (-C * xDot - K * x) / J
    return dY

def RK4(h, t, Y):
    k1 = Grad(t, Y)
    k2 = Grad(t + h / 2, Y + h * k1 / 2)
    k3 = Grad(t + h / 2, Y + h * k2 / 2)
    k4 = Grad(t + h, Y + h * k3)
    dY = (k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6)
    return dY

def RK5(h, t, Y):
    k1 = Grad(t, Y)
    k2 = Grad(t + h / 4, Y + h * k1 / 4)
    k3 = Grad(t + h / 4, Y + h * k1 / 8 + h * k2 / 8)
    k4 = Grad(t + h / 2, Y - h * k2 / 2 + h * k3)
    k5 = Grad(t + 3 * h / 4, Y + 3 * h * k1 / 16 + 9 * h * k4 / 16)
    k6 = Grad(t + h, Y - 3 * h * k1 / 7 + 2 * h * k2 / 7 + 12 * h * k3 / 7 - 12 * h * k4 / 7 + 8 * h * k5 / 7)
    dY = (7 * k1 + 32 * k3 + 12 * k4 + 32 * k5 + 7 * k6) / 90
    return dY

def Integrate(endtime, h: float = 1e-2, v0: float = 0, p0: float = 0, method: str = 'rk4'):
    t = 0
    steps = int(endtime / h)
    Y = np.array([p0, v0]).reshape((2, 1))
    dY = Grad(t, Y)
    # RK integrate
    rk_time = []
    rk_Y = []
    rk_dY = []
    for idx in range(steps + 1):
        # save
        rk_time.append(t)
        rk_Y.append(Y)
        rk_dY.append(dY)
        
        # calculate gradient
        if method.lower() == 'rk4':
            dY = RK4(h, t, Y)
        elif method.lower() == 'rk5':
            dY = RK5(h, t, Y)
        
        # update
        Y = Y + h * dY
        t = np.around(t + h, decimals=5)
        
        # print
        if (idx + 1) % 10000 == 0:
            print(f"Solving t={t:.5f} sec")
    
    rk_time = np.array(rk_time)
    rk_Y = np.concatenate(rk_Y, axis=1).T  # pos and vel
    rk_dY = np.concatenate(rk_dY, axis=1).T  # update gradients
    return rk_time, rk_Y, rk_dY

def AnalyticSolution(t):
    x = np.exp(-1.2 * t) * (np.cos(np.sqrt(10.56) * t) + 1.2 / np.sqrt(10.56) * np.sin(np.sqrt(10.56) * t))
    return x

def MyPlotTemplate():
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 12
    plt.rcParams['mathtext.fontset'] = 'stix'

def PlotForm():
    plt.xlim(0, 15)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
# Integrate

exp_time=[0,2.89,4.81,6.5,7.93,9.25]
exp_disp=np.deg2rad(np.array([120,61,30,21,12,0]))

Alpha=6
J=0.00053756479
C=0.0006050523
K=0.040542768*np.sin(np.deg2rad(Alpha))

rk_time, rk_Y, rk_dY = Integrate(15, h=0.01, v0=0, p0=np.deg2rad(120), method='rk4')

# Plot
RMSE = np.sqrt(np.mean(np.square(AnalyticSolution(rk_time) - rk_Y[:, 0])))
Fig=plt.figure(figsize=(10,6))
MyPlotTemplate()
plt.subplot(1, 1, 1)
PlotForm()
plt.suptitle("Advanced Mechanical Vibration, Spring 2022\n2022310371 Hyeonbeen Lee", fontsize=18)
plt.title(f"$\\alpha=${Alpha:d}$\degree$\n$J=${J:.10f} $Nm^2$\n$c=${C:.10f} $Ns/m$\n$K=${K:.10f} $N/m$")
plt.plot(rk_time, rk_Y[:, 0], color='red', label='SDOF model')
plt.scatter(exp_time,exp_disp, color='black', label='Experiment')
plt.legend(loc=1)

plt.tight_layout()
plt.show()