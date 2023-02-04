import numpy as np
import matplotlib.pyplot as plt

def Grad(t, Y):
    x = Y[0]
    xDot = Y[1]
    dY = np.zeros((2, 1))
    dY[0] = xDot
    dY[1] = (-12*xDot-60*x)/5
    return dY

def RK4(h, t, Y):
    k1 = Grad(t, Y)
    k2 = Grad(t + h / 2, Y + h*k1 / 2)
    k3 = Grad(t + h / 2, Y + h*k2 / 2)
    k4 = Grad(t + h, Y + h*k3)
    dY = (k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6)
    return dY

def RK5(h, t, Y):
    k1 = Grad(t, Y)
    k2 = Grad(t + h / 4, Y + h*k1 / 4)
    k3 = Grad(t + h / 4, Y + h*k1 / 8 + h*k2 / 8)
    k4 = Grad(t + h / 2, Y - h*k2 / 2 + h*k3)
    k5 = Grad(t + 3 * h / 4, Y + 3 * h*k1 / 16 + 9 * h*k4 / 16)
    k6 = Grad(t + h, Y - 3 * h*k1 / 7 + 2 * h*k2 / 7 + 12 * h*k3 / 7 - 12 * h*k4 / 7 + 8 * h*k5 / 7)
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
    plt.xlim(0,10)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
# Integrate
rk_time, rk_Y, rk_dY = Integrate(10, h=0.5, v0=0, p0=1, method='rk4')

# Plot
RMSE=np.sqrt(np.mean(np.square(AnalyticSolution(rk_time)-rk_Y[:, 0])))
MyPlotTemplate()
plt.subplot(2,1,1)
PlotForm()
plt.suptitle("Advanced Mechanical Vibration, Spring 2022\n2022310371 Hyeonbeen Lee", fontsize=18)
plt.title(f"RMSE={RMSE:.10f}")
plt.plot(rk_time, rk_Y[:, 0],'-*',color='red', label='RK4')
plt.plot(rk_time, AnalyticSolution(rk_time),color='black', label='Analytic')
plt.legend(loc=1)

plt.subplot(2,1,2)
PlotForm()
plt.title(f"Absolute Error")
plt.plot(rk_time,np.abs(AnalyticSolution(rk_time)-rk_Y[:,0]))

plt.tight_layout()
plt.show()