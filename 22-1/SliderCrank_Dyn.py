import numpy as np
from numpy import sin, cos, pi, deg2rad, array, zeros
import matplotlib.pyplot as plt

def Solver(t, Y):
    global Mass
    m2 = mass[0, 0]
    m3 = mass[3, 3]
    m4 = mass[6, 6]
    q_i = Y[0:9]
    qDot_i = Y[9:18]
    
    Cq = C_q(q_i)
    Qd = Q_d(q_i, qDot_i)
    
    # External force
    Qe = Q_e(m2, m3, m4, t)
    
    # Augmented formulation
    A = np.concatenate([np.concatenate([mass, Cq.T], axis=1),
                        np.concatenate([Cq, zeros((8, 8))], axis=1)], axis=0)
    b = np.concatenate([Qe, Qd], axis=0)
    
    # Solve
    x = np.linalg.solve(A, b)
    qDDot = x[0:9]
    Lambda = x[9:18]
    
    YDot = np.concatenate([qDot_i, qDDot], axis=0)
    return YDot, Lambda


def Q_d(q, qDot):
    global l1, l3
    q3 = q[2].item()
    q6 = q[5].item()
    qDot3 = qDot[2].item()
    qDot6 = qDot[5].item()
    
    Qd = array([[0, 0, (l2 * qDot3 * cos(q3)) / 2, 0, 0, 0, 0, 0, 0],
                [0, 0, (l2 * qDot3 * sin(q3)) / 2, 0, 0, 0, 0, 0, 0],
                [0, 0, -(l2 * qDot3 * cos(q3)) / 2, 0, 0, -(l3 * qDot6 * cos(q6)) / 2, 0, 0, 0],
                [0, 0, -(l2 * qDot3 * sin(q3)) / 2, 0, 0, -(l3 * qDot6 * sin(q6)) / 2, 0, 0, 0],
                [0, 0, 0, 0, 0, -(l3 * qDot6 * cos(q6)) / 2, 0, 0, 0],
                [0, 0, 0, 0, 0, -(l3 * qDot6 * sin(q6)) / 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    Qd = -Qd @ qDot
    return Qd

def Q_e(m2, m3, m4, t):
    global g
    # Qt = Step(t, 0, 0, 0.05, 1) * 100
    Qt = 100 * sin(pi / 0.1 * t)
    Qe = array([0, m2 * g, Qt, 0, m3 * g, 0, 0, m4 * g, 0]).reshape(-1, 1)
    return Qe

def C_q(q):
    global l1, l3
    q3 = q[2].item()
    q6 = q[5].item()
    Cq = array([[1, 0, (l2 * sin(q3)) / 2, 0, 0, 0, 0, 0, 0],
                [0, 1, -(l2 * cos(q3)) / 2, 0, 0, 0, 0, 0, 0],
                [1, 0, -(l2 * sin(q3)) / 2, -1, 0, -(l3 * sin(q6)) / 2, 0, 0, 0],
                [0, 1, (l2 * cos(q3)) / 2, 0, -1, (l3 * cos(q6)) / 2, 0, 0, 0],
                [0, 0, 0, 1, 0, -(l3 * sin(q6)) / 2, -1, 0, 0],
                [0, 0, 0, 0, 1, (l3 * cos(q6)) / 2, 0, -1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1]])
    return Cq

def Step(time, t0, h0, t1, h1):
    if (time <= t0):
        a = h0
    elif (t0 <= time and time <= t1):
        a = h0 + (h1 - h0) * ((time - t0) / (t1 - t0)) ** 2 * (3 - 2 * ((time - t0) / (t1 - t0)))
    else:
        a = h1
    return a


t = 0
h = 1e-4  # time Step
endTime = 0.1
step = int(endTime / h)
g = -9.80665

## Initical Config
l1 = 0.15
l3 = 0.25
d2_0 = deg2rad(45)
# Crankshaft
Rx2 = l1 * cos(d2_0) / 2
Ry2 = l1 * sin(d2_0) / 2
d2 = d2_0
# Connecting rod
d3 = 5.888774749545362
Rx3 = l1 * cos(d2) + l3 * cos(d3) / 2
Ry3 = l1 * sin(d2) + l3 * sin(d3) / 2
# Sliding block
Rx4 = l1 * cos(d2) + l3 * cos(d3)
Ry4 = l1 * sin(d2) + l3 * sin(d3)
d4 = 0
# M, J
m2 = 1
j2 = 1e-004
m3 = 1
j3 = 1e-004
m4 = 1
j4 = 1e-004

Mass = np.diag([m2, m2, j2, m3, m3, j3, m4, m4, j4])

# Local coord - joint origin
u1o = array([0, 0]).reshape(-1, 1)
u2o = array([-l1 / 2, 0]).reshape(-1, 1)
u2a = array([l1 / 2, 0]).reshape(-1, 1)
u3a = array([-l3 / 2, 0]).reshape(-1, 1)
u3b = array([l3 / 2, 0]).reshape(-1, 1)
u4b = array([0, 0]).reshape(-1, 1)

# Generalized coordinate
q_i = array([Rx2, Ry2, d2, Rx3, Ry3, d3, Rx4, Ry4, d4]).reshape(-1, 1)
qDot_i = zeros((9, 1))

# for results
time = np.empty(step)
torque = np.empty(step)
result_q = np.empty((len(q_i), step))
result_qDot = np.empty((len(q_i), step))
result_qDDot = np.empty((len(q_i), step))
result_Lambda = np.empty((8, step))
result_Qe = np.empty((len(q_i), step))

# Solve RK4
for i in range(step):
    time[i] = t
    
    # RK4
    Y = np.concatenate([q_i, qDot_i], axis=0)
    k1, Lambda = Solver(t, Y)
    k2, dummy = Solver(t + 0.5 * h, Y + 0.5 * h * k1)
    k3, dummy = Solver(t + 0.5 * h, Y + 0.5 * h * k2)
    k4, dummy = Solver(t + h, Y + h * k3)
    Y_Next = Y + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4)
    
    # for external force plot
    Qe = Q_e(m2, m3, m4, t)
    torque[i] = Qe[2]
    
    q_i = Y_Next[0:9]
    qDot_i = Y_Next[9:18]
    qDDot = k1[9:18]
    
    # for plot
    result_q[:, i] = q_i.flatten()
    result_qDot[:, i] = qDot_i.flatten()
    result_qDDot[:, i] = qDDot.flatten()
    result_Lambda[:, i] = Lambda.flatten()
    result_Qe[:, i] = Qe.flatten()
    
    print(f"t: {time[i]:.5f}")
    t = t + h

# Plot
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['mathtext.fontset'] = 'stix'
def plotTemplate():
    plt.xlabel('Time (sec)')
    plt.xlim(time[0], time[-1])
    plt.grid()
    plt.legend(loc=1)
plotStyle = dict(marker='o', markevery=int(step / 20), fillstyle='none', color='black', label='Python')

Fig = plt.figure(figsize=(19, 10))

plt.subplot(221)
plt.title('Driving Torque')
plt.plot(time, torque, **plotStyle)
plotTemplate()

plt.subplot(222)
plt.title('Connecting rod position (x)')
plt.plot(time, result_q[3, :], **plotStyle)
plotTemplate()

plt.subplot(223)
plt.title('Connecting rod velocity (x)')
plt.plot(time, result_qDot[3, :], **plotStyle)
plotTemplate()

plt.subplot(224)
plt.title('Connecting rod acceleration (x)')
plt.plot(time, result_qDDot[3, :], **plotStyle)
plotTemplate()

Fig.tight_layout()
plt.show()
