# This code is for 21 spring semester system dynamics course HW4.
# Coded by Hyeonbeen Lee
import numpy as np
import matplotlib.pyplot as plt

# Given constants
global L,g
M = 1
L = 2
g = 9.8
th0 = np.pi / 3
dth0 = 0
y10 = th0
y20 = dth0


# State space vector components
# We want to integrate and plot y1
# First integrate dy2 w.r.t. time then substitute into dy1 and integrate once more.
def dy2(y1):  # Acceleration of theta
    return -g / L * np.sin(y1)


def dy1(y2):  # Velocity of theta
    return y2


def rad2deg(x):
    deg = x / np.pi * 180
    return deg


# Integrator settings
steps = 1000  # Steps
endtime = 2 * np.pi  # End time
h = endtime / steps  # Step size
t = np.linspace(0,endtime,steps)
t = np.append(t,t[-1]+h)

# EulerSolve initial settings
y2 = np.zeros(steps+1)  # Integrated dy2 = velocity
y1 = np.zeros(steps+1)  # Integrated dy1 = theta

y2[0] = y20  # Initial value
y1[0] = y10  # Initial value

# Euler Solve
for i in range(1,steps+1,1):
    y2[i] = y2[i-1]+dy2(y1[i-1]) * h
    y1[i] = y1[i-1]+dy1(y2[i-1]) * h

acceleration = dy2(y1)

y1 = rad2deg(y1)

# Plot
fig = plt.figure(figsize=(15,7))

f1 = fig.add_subplot(221)
f1.set_title('Pos. of theta')
f1.set_xlabel('Time(t)')
f1.set_ylabel('Theta(deg)')
f1.plot(t,y1)
f1.grid()

f2 = fig.add_subplot(222)
f2.set_title('Vel. of theta')
f2.set_xlabel('Time(t)')
f2.set_ylabel('Velocity(rad/s)')
f2.plot(t,y2)
f2.grid()

f3 = fig.add_subplot(223)
f3.set_title('Acc. of theta')
f3.set_xlabel('Time(t)')
f3.set_ylabel('Acceleration(rad/s^2)')
f3.plot(t,acceleration)
f3.grid()

fig.tight_layout
fig.suptitle('Single pendulum integration')
plt.show()
