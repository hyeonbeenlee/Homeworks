import numpy as np
import matplotlib.pyplot as plt
import DataProcessing as DP
def Grad(node, t, Y, forced:bool=False):  # dY
    node -= 1
    x = Y[0]
    xDot = Y[1]
    
    dY = np.empty(2)
    dY[0] = xDot
    diag_C = (alpha * M_d + beta * K_d)
    dY[1] = (-diag_C[node, node] * xDot - K_d[node, node] * x) / M_d[node, node]  # Acceleration spline function
    if forced:
        F0=1000
        omega=2
        dY[1]+=(P@np.array([0,0,F0*np.sin(omega*t)]).reshape(-1,1))[node,0]
    return dY

def RK4(node, h, t, Y,forced:bool=False):
    k1 = Grad(node, t, Y,forced)
    k2 = Grad(node, t + h / 2, Y + h * k1 / 2,forced)
    k3 = Grad(node, t + h / 2, Y + h * k2 / 2,forced)
    k4 = Grad(node, t + h, Y + h * k3,forced)
    dY = (k1 / 6 + k2 / 3 + k3 / 3 + k4 / 6,forced)
    return dY

def RK5(node, h, t, Y,forced:bool=False):
    k1 = Grad(node, t, Y,forced)
    k2 = Grad(node, t + h / 4, Y + h * k1 / 4,forced)
    k3 = Grad(node, t + h / 4, Y + h * k1 / 8 + h * k2 / 8,forced)
    k4 = Grad(node, t + h / 2, Y - h * k2 / 2 + h * k3,forced)
    k5 = Grad(node, t + 3 * h / 4, Y + 3 * h * k1 / 16 + 9 * h * k4 / 16,forced)
    k6 = Grad(node, t + h, Y - 3 * h * k1 / 7 + 2 * h * k2 / 7 + 12 * h * k3 / 7 - 12 * h * k4 / 7 + 8 * h * k5 / 7,forced)
    dY = (7 * k1 + 32 * k3 + 12 * k4 + 32 * k5 + 7 * k6) / 90
    return dY

def Integrate(node, t_0: float = 0, t_end: float = 1, h: float = 1e-2, v0: float = 0, p0: float = 0, method: str = 'rk4',forced:bool=False):
    # Initial conditions
    t = t_0
    steps = int((t_end - t_0) / h)
    Y = np.array([p0, v0])
    dY = Grad(node, t, Y,forced)
    
    # RK integrate
    rk_time = np.empty(steps + 1)
    rk_Y = np.empty((steps + 1, 2))  # pos and vel
    rk_dY = np.empty_like(rk_Y)  # update gradients
    for idx in range(steps + 1):
        # save
        rk_time[idx] = t
        rk_Y[idx] = Y
        rk_dY[idx] = dY
        
        # calculate
        if method.lower() == 'rk4':
            dY = RK4(node, h, t, Y,forced)
        elif method.lower() == 'rk5':
            dY = RK5(node, h, t, Y,forced)
        
        # update
        Y = Y + h * dY
        t = np.around(t + h, decimals=5)
        
        # print
        if (idx + 1) % 10000 == 0:
            print(f"Solving t={t:.5f} ({idx + 1}/{steps + 1})")
    
    return rk_time, rk_Y, rk_dY


def Plot_EigVec():
    DP.PlotTemplate(13)
    fig, ax = plt.subplots(3, 1, figsize=(6, 8))
    for i in range(3):
        ax[i].plot(eigVec[:, i], '-o', color='green')
        ax[i].set(title=f"Mode {i + 1} ($\lambda_{{{i + 1}}}$={eigVal[i]:.4f}, $\omega_{{{i + 1}}}$={np.sqrt(eigVal[i]):.4f}, $f_{{{i + 1}}}$={np.sqrt(eigVal[i]) / (2 * np.pi):.4f})",
                  xlim=(0, 2), xticks=[],
                  ylim=(-1, 1), yticks=[-1, -0.5, 0, 0.5, 1])
        ax[i].grid()
    fig.tight_layout()
    plt.show()

M = np.diag([0.0244, 0.0244, 0.0122])
A = np.array([
    [0.0011, 0.0025, 0.0042],
    [0.0031, 0.0079, 0.013],
    [0.0043, 0.014, 0.025]
])

# A = np.array([
#     [0.0010989, 0.00279789, 0.00459184],
#     [0.00251177, 0.0082291, 0.01428571],
#     [0.00392465, 0.01431863, 0.0255102]
# ])
K = np.linalg.inv(A)

# not sorted
eigVal_, eigVec_ = np.linalg.eig(K @ np.linalg.inv(M))

# sorted
eigVal, eigVec = np.empty(3), np.empty((3, 3))
eigVal = np.sort(eigVal_)
eigVec[:, 0] = eigVec_[:, 2]
eigVec[:, 1] = eigVec_[:, 1]
eigVec[:, 2] = eigVec_[:, 0]
# Plot_EigVec()

P = eigVec_
M_d = P.T @ M @ P
K_d = P.T @ K @ P
print(M_d)
print(K_d)

M_d = np.diag(M_d.diagonal())
K_d = np.diag(K_d.diagonal())
print(M_d)
print(K_d)

alpha = 0.00001
beta = 0.00002
print(alpha * M + beta * K)
init_pos = P @ np.array([0.01, 0.02, 0.07]).reshape(-1, 1)
init_vel = P @ np.array([0, 0, 0]).reshape(-1, 1)
time1, Y1, dY1 = Integrate(1, 0, 45, 1e-3, init_vel[0, 0], init_pos[0, 0], method='rk5',forced=True)
time2, Y2, dY2 = Integrate(2, 0, 45, 1e-3, init_vel[1, 0], init_pos[1, 0], method='rk5',forced=True)
time3, Y3, dY3 = Integrate(3, 0, 45, 1e-3, init_vel[2, 0], init_pos[2, 0], method='rk5',forced=True)
q = np.vstack([Y1[:, 0], Y2[:, 0], Y3[:, 0]])
x = np.linalg.inv(P) @ q


DP.PlotTemplate(16)
fig, ax = plt.subplots(3, 1, figsize=(19, 10))
linewidth = 1
colors = ['green', 'red', 'blue']
for i in range(3):
    ax[i].plot(time1, x[i, :], label=f'$m_{i + 1}$', color=colors[i], linewidth=linewidth)
    ax[i].set(xlim=(0, 45), xlabel='Time (sec)',
              ylim=(-0.11, 0.11), ylabel='Displacement (m)')
    ax[i].grid()
    ax[i].legend(loc=1)
fig.tight_layout()

DP.PlotTemplate(16)
fig, ax = plt.subplots(3, 1, figsize=(19, 10))
linewidth = 2
colors = ['green', 'red', 'blue']
for i in range(3):
    Freq, Amp = DP.FFT(x[i, :], 1e-3)
    ax[i].plot(Freq, Amp, label=f'$m_{i + 1}$', color=colors[i], linewidth=linewidth)
    ax[i].set(xlim=(0, 100), xlabel='Frequency (Hz)', xticks=np.arange(0, 101, 5),
              ylabel='Displacement (m)')
    ax[i].grid()
    ax[i].legend(loc=1)
fig.tight_layout()
plt.show()
