import numpy as np
from numpy import sin, cos, pi, deg2rad, array, zeros
import pandas as pd
import matplotlib.pyplot as plt

# For augmented formulation
def Solver(t, Y):
    q_i = Y[0:3]
    qDot_i = Y[3:6]
    
    Cq = C_q(q_i)
    Qd = Q_d(q_i, qDot_i)
    
    # External force
    Qe = Q_e(t, q_i)
    
    # Augmented formulation
    A = np.concatenate([np.concatenate([Mass, Cq.T], axis=1), np.concatenate([Cq, zeros((2, 2))], axis=1)], axis=0)
    b = np.concatenate([Qe, Qd], axis=0)
    
    # Solve
    x = np.linalg.solve(A, b)
    qDDot = x[:3]
    Lambda = -x[3:5]
    
    YDot = np.concatenate([qDot_i, qDDot], axis=0)
    return YDot, Lambda

def X(q):
    q3 = q[2].item()
    x = l1 * sin(q3)
    y = 2 * l1 - l1 * cos(q3)
    X = np.sqrt(x ** 2 + y ** 2) - l1
    return X

def C_q(q):
    q3 = q[2].item()
    Cq = array([[1, 0, -l1 / 2 * cos(q3)],
                [0, 1, -l1 / 2 * sin(q3)]])
    return Cq

def Q_e(t, q):
    global g
    q3 = q[2].item()
    y = l1 * sin(q3)
    x = 2 * l1 - l1 * cos(q3)
    alpha = np.arctan2(y,x)
    
    M1 = 2 * sin(5 * t)
    
    Qe = array([-k * X(q) * sin(alpha),
                -k * X(q) * cos(alpha) - m1 * g,
                M1 - k * X(q) * cos(alpha) * l1 / 2 * sin(q3) - k * X(q) * sin(alpha) * l1 / 2 * cos(q3)
                ]).reshape(-1, 1)
    return Qe

def Q_d(q, qDot):
    q3 = q[2].item()
    qDot3 = qDot[2].item()
    
    Qd = array([-l1 / 2 * sin(q3) * (qDot3 ** 2),
                l1 / 2 * cos(q3) * (qDot3 ** 2)
                ]).reshape(-1, 1)
    return Qd


# For embedded formulation
def B_i(q):
    q3 = q
    B_i = array([l1 / 2 * cos(q3),
                 l1 / 2 * sin(q3),
                 1]).reshape(-1, 1)
    return B_i

def r_i(q, qDot):
    q3 = q
    qDot3 = qDot
    r_i = array([-l1 / 2 * sin(q3) * qDot3 ** 2,
                 l1 / 2 * cos(q3) * qDot3 ** 2,
                 0]).reshape(-1, 1)
    return r_i

def Q_e_embed(t, q):
    global g
    q3 = q
    
    y = l1 * sin(q3)
    x = 2 * l1 - l1 * cos(q3)
    alpha = np.arctan2(y, x)
    
    M1 = 2 * sin(5 * t)
    Qe = array([-k * X_embed(q) * sin(alpha),
                -k * X_embed(q) * cos(alpha) - m1 * g,
                M1 - k * X_embed(q) * cos(alpha) * l1 / 2 * sin(q3) - k * X_embed(q) * sin(alpha) * l1 / 2 * cos(q3)
                ]).reshape(-1, 1)
    return Qe

def X_embed(q):
    q3 = q
    X = np.sqrt((l1 * sin(q3)) ** 2 + (2 * l1 - l1 * cos(q3)) ** 2) - l1
    return X

def Solver_Embedded(t, Y):
    q_i = Y[0].item()
    qDot_i = Y[1].item()
    
    BiT_M_Bi = B_i(q_i).T @ Mass @ B_i(q_i)
    BiT_M_ri = B_i(q_i).T @ Mass @ r_i(q_i, qDot_i)
    BiT_Qe = B_i(q_i).T @ Q_e_embed(t, q_i)
    
    # Augmented formulation
    A = BiT_M_Bi
    b = BiT_Qe - BiT_M_ri
    
    # Solve
    x = b.item() / A.item()
    qDDot = x
    
    YDot = np.array([qDot_i, qDDot]).reshape(-1, 1)
    return YDot

def Step(time, t0, h0, t1, h1):
    if (time <= t0):
        a = h0
    elif (t0 <= time and time <= t1):
        a = h0 + (h1 - h0) * ((time - t0) / (t1 - t0)) ** 2 * (3 - 2 * ((time - t0) / (t1 - t0)))
    else:
        a = h1
    return a


t = 0
h = 1e-3  # time Step
endTime = 3
step = int(endTime / h)
g = 9.80665

## Initical Config
k = 100
l1 = 1.3
th1_0 = deg2rad(0)
# Rod
x1 = l1 * sin(th1_0) / 2
y1 = -l1 * cos(th1_0) / 2
th1 = th1_0
# M, J
m1 = 0.7
j1 = 1 / 12 * m1 * l1 ** 2 + m1 * (l1 / 2) ** 2
Mass = np.diag([m1, m1, j1])

# Augmented formulation
q_i = array([x1, y1, th1]).reshape(-1, 1)
qDot_i = zeros((len(q_i), 1))

time = np.empty(step)
torque = np.empty(step)
result_q = np.empty((len(q_i), step))
result_qDot = np.empty((len(q_i), step))
result_qDDot = np.empty((len(q_i), step))
result_Lambda = np.empty((2, step))
result_X = np.empty((1, step))
result_Torque = np.empty((1, step))
for i in range(step):
    time[i] = t
    
    Y = np.concatenate([q_i, qDot_i], axis=0)
    k1, Lambda = Solver(t, Y)
    k2, dummy = Solver(t + 0.5 * h, Y + 0.5 * h * k1)
    k3, dummy = Solver(t + 0.5 * h, Y + 0.5 * h * k2)
    k4, dummy = Solver(t + h, Y + h * k3)
    Y_Next = Y + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4)
    
    # for external force plot
    
    q_i = Y_Next[0:3]
    qDot_i = Y_Next[3:6]
    qDDot = k1[3:6]
    
    result_q[:, i] = q_i.flatten()
    result_qDot[:, i] = qDot_i.flatten()
    result_qDDot[:, i] = qDDot.flatten()
    result_Lambda[:, i] = Lambda.flatten()
    result_X[:, i] = X(q_i)
    # result_Qe[:, i] = Qe.flatten()
    
    t = t + h

# Embedded formulation
t = 0
q_i = th1
qDot_i = 0

time = np.empty(step)
torque = np.empty(step)
result_q_embed = np.empty((1, step))
result_qDot_embed = np.empty((1, step))
result_qDDot_embed = np.empty((1, step))
for i in range(step):
    time[i] = t
    
    Y = np.array([q_i, qDot_i]).reshape(-1, 1)
    k1 = Solver_Embedded(t, Y)
    k2 = Solver_Embedded(t + 0.5 * h, Y + 0.5 * h * k1)
    k3 = Solver_Embedded(t + 0.5 * h, Y + 0.5 * h * k2)
    k4 = Solver_Embedded(t + h, Y + h * k3)
    Y_Next = Y + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4)
    
    # for external force plot
    
    q_i = Y_Next[0]
    qDot_i = Y_Next[1]
    qDDot = k1[1]
    
    result_q_embed[:, i] = q_i.item()
    result_qDot_embed[:, i] = qDot_i.item()
    result_qDDot_embed[:, i] = qDDot.item()
    
    t = t + h

# Plot templates
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['mathtext.fontset'] = 'stix'
plotStyle_Py = dict(marker='o', markevery=int(step / 25), fillstyle='none', color='black', label='Python-AugForm')
plotStyle_Py_Embed = dict(marker='o', markevery=int(step / 30), fillstyle='none', color='blue', label='Python-EmbedForm')
plotStyle_RD = dict(marker='x', markevery=int(step / 35), fillstyle='none', color='red', label='RecurDyn')

def plotTemplate():
    plt.xlabel('Time (sec)')
    plt.xlim(time[0], time[-1])
    plt.grid()
    plt.legend(loc=2)


# Load recurdyn data
data_RD = pd.read_csv('./HW4_RD.csv')

# Plot
Fig = plt.figure(figsize=(19, 10))

plt.subplot(221)
plt.title(r'$\theta^1$')
plt.plot(time, np.rad2deg(result_q[2, :]), **plotStyle_Py)
plt.plot(time, np.rad2deg(result_q_embed[0, :]), **plotStyle_Py_Embed)
plt.plot(data_RD.iloc[:, 1], data_RD.iloc[:, 2], **plotStyle_RD)
plotTemplate()

plt.subplot(222)
plt.title(r'$\dot{\theta}^1$')
plt.plot(time, result_qDot[2, :], **plotStyle_Py)
plt.plot(time, result_qDot_embed[0, :], **plotStyle_Py_Embed)
plt.plot(data_RD.iloc[:, 1], data_RD.iloc[:, 3], **plotStyle_RD)
plotTemplate()

plt.subplot(223)
plt.title(r'$\ddot{\theta}^1$')
plt.plot(time, result_qDDot[2, :], **plotStyle_Py)
plt.plot(time, result_qDDot_embed[0, :], **plotStyle_Py_Embed)
plt.plot(data_RD.iloc[:, 1], data_RD.iloc[:, 4], **plotStyle_RD)
plotTemplate()

Fig.tight_layout()
plt.show()
