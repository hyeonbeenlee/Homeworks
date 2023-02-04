import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import Functions as MyF


A = np.array([[1, 1, -1], [100, 0, 200], [0, 100, 200]])
b = np.array([0, 3, 1.5])
I_analytic = np.linalg.solve(A, b)  # i1, i2, i3
R_analytic = [100, 100, 200]  # r1,r2,r3
V_analytic = np.abs(I_analytic * R_analytic)  # v1,v2,v3
print(V_analytic)
## 순방향
V_r = np.array([0.0002, 0.0196, 0.1201, 0.4146, 1.320, 2.284, 3.275, 4.240])
V_d = np.array([0.3214, 0.499, 0.587, 0.648, 0.703, 0.728, 0.744, 0.755])
I = [0, 0.00042, 0.00178, 0.00406, 0.01369, 0.02348, 0.03278, 0.04230]
V = [0.3, 0.5, 0.7, 1, 2, 3, 4, 5]

## 역방향
V_rev = np.array([1, 2, 3, 4, 5])
V_r_rev = np.zeros(5)
V_d_rev = np.array([-0.0321, -0.0340, -0.0353, -0.0361, -0.0369])
I_rev = np.full(5, -0.00001)

## 역방향 뒤집기
V_rev=np.flip(-V_rev)
V_r_rev=np.flip(V_r_rev)
V_d_rev=np.flip(V_d_rev)
I_rev=np.flip(I_rev)

Fig1 = plt.figure(figsize=(10, 5))
MyF.MyPlotTemplate()
plt.subplot(2, 1, 1)
plt.plot(np.hstack([V_rev,V]), np.hstack([V_d_rev,V_d]), '-o', label='Diode', color='k')
plt.plot(np.hstack([V_rev,V]), np.hstack([V_r_rev,V_r]), '-o', label='Resistance', color='r')
plt.ylabel('Voltage $(V)$'), plt.xlabel('Voltage $(V)$')
plt.grid()
plt.xticks(np.hstack([V_rev,np.zeros(1),V]),fontsize=10)
plt.legend(loc=2)

plt.subplot(2, 1, 2)
plt.plot(np.hstack([V_rev,V]),np.hstack([V_d_rev,V_d])+ np.hstack([V_r_rev,V_r]), '-o', label='Diode+Resistance', color='b')
plt.plot(np.hstack([V_rev,V]),np.hstack([V_rev,V]),label='Applied voltage',color='y')
plt.ylabel('Voltage $(V)$'), plt.xlabel('Voltage $(V)$')
plt.grid()
plt.xticks(np.hstack([V_rev,np.zeros(1),V]),fontsize=10)
plt.yticks(np.hstack([V_rev,np.zeros(1),V]),fontsize=10)
plt.legend(loc=2)

# plt.subplot(2, 1, 2)
# plt.plot(np.hstack([V_rev,V]), np.hstack([I_rev,I]), '-o', color='k')
# plt.ylabel('Current $(A)$'), plt.xlabel('Voltage $(V)$')
# plt.grid()
# plt.xticks(np.hstack([V_rev,np.zeros(1),V]),fontsize=10)

# Fig2 = plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.plot(V_rev, V_d_rev, '-o', label='Diode', color='k')
# plt.plot(V_rev, V_r_rev, '-o', label='Resistance', color='r')
# plt.ylabel('Voltage $(V)$'), plt.xlabel('Voltage $(V)$')
# plt.grid()
# plt.xticks(V)
# plt.legend(loc=5)
#
# plt.subplot(1, 2, 2)
# plt.plot(V_rev, I_rev, '-o', color='k')
# plt.ylabel('Current $(A)$'), plt.xlabel('Voltage $(V)$')
# plt.grid()
# plt.ylim(-0.00002,0)
# plt.xticks(V)
# plt.suptitle("Reverse bias case")

plt.tight_layout()
plt.show()
