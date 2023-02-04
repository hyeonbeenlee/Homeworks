from sympy import *

# parameters
t, w, l1, l3, d = symbols('t, w, l2, l3, d')

# generalized coordinates
Rx1, Ry1, TH1 = symbols('Rx1, Ry1, TH1')
Rx2, Ry2, TH2 = symbols('Rx2, Ry2, TH2')
Rx3, Ry3, TH3 = symbols('Rx3, Ry3, TH3')
Rx4, Ry4, TH4 = symbols('Rx4, Ry4, TH4')
q = Matrix([Rx1, Ry1, TH1,
            Rx2, Ry2, TH2,
            Rx3, Ry3, TH3,
            Rx4, Ry4, TH4, ])

# constraint vector
C = zeros(12, 1)
C[0] = Rx1
C[1] = Ry1
C[2] = TH1

C[3] = Rx2 - (l1 / 2) * cos(TH2)
C[4] = Ry2 - (l1 / 2) * sin(TH2)

C[5] = Rx2 + (l1 / 2) * cos(TH2) - Rx3 + (l3 / 2) * cos(TH3)
C[6] = Ry2 + (l1 / 2) * sin(TH2) - Ry3 + (l3 / 2) * sin(TH3)

C[7] = Rx3 + (l3 / 2) * cos(TH3) - Rx4
C[8] = Ry3 + (l3 / 2) * sin(TH3) - Ry4

C[9] = Ry4
C[10] = TH4

C[11] = Rx4 + (l1 / w) * cos(w * t) - d - (l1 / w)

# constraint jacobian
Cq = zeros(len(C), len(q))
for i in range(len(C)):
    for j in range(len(q)):
        Cq[i, j] = diff(C[i], q[j])
"""
\left[\begin{array}{cccccccccccc}1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 1 & 0 & \frac{l^{2} \sin{\left(\theta^{2} \right)}}{2} & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 1 & - \frac{l^{2} \cos{\left(\theta^{2} \right)}}{2} & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 1 & 0 & - \frac{l^{2} \sin{\left(\theta^{2} \right)}}{2} & -1 & 0 & - \frac{l^{3} \sin{\left(\theta^{3} \right)}}{2} & 0 & 0 & 0\\0 & 0 & 0 & 0 & 1 & \frac{l^{2} \cos{\left(\theta^{2} \right)}}{2} & 0 & -1 & \frac{l^{3} \cos{\left(\theta^{3} \right)}}{2} & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & - \frac{l^{3} \sin{\left(\theta^{3} \right)}}{2} & -1 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & \frac{l^{3} \cos{\left(\theta^{3} \right)}}{2} & 0 & -1 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0\end{array}\right]
"""

# dC/dt term
Ct = zeros(len(C), 1)
for i in range(len(C)):
    Ct[i] = diff(C[i], t)
"""
\left[\begin{matrix}0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\- l^{2} \sin{\left(t w \right)}\end{matrix}\right]
"""

# Cq*qDot
"""
\left[\begin{matrix}\dot{R}_1^{1}\\\dot{R}_2^{1}\\\dot{\theta}^{1}\\\dot{R}_1^{2} + \frac{\dot{\theta}^{2} l^{2} \sin{\left(\dot{\theta}^{2} \right)}}{2}\\\dot{R}_2^{2} - \frac{\dot{\theta}^{2} l^{2} \cos{\left(\dot{\theta}^{2} \right)}}{2}\\\dot{R}_1^{2} - \dot{R}_1^{3} - \frac{\dot{\theta}^{2} l^{2} \sin{\left(\dot{\theta}^{2} \right)}}{2} - \frac{\dot{\theta}^{3} l^{3} \sin{\left(\dot{\theta}^{3} \right)}}{2}\\\dot{R}_2^{2} - \dot{R}_2^{3} + \frac{\dot{\theta}^{2} l^{2} \cos{\left(\dot{\theta}^{2} \right)}}{2} + \frac{\dot{\theta}^{3} l^{3} \cos{\left(\dot{\theta}^{3} \right)}}{2}\\\dot{R}_1^{3} - \dot{R}_1^{4} - \frac{\dot{\theta}^{3} l^{3} \sin{\left(\dot{\theta}^{3} \right)}}{2}\\\dot{R}_2^{3} - \dot{R}_2^{4} + \frac{\dot{\theta}^{3} l^{3} \cos{\left(\dot{\theta}^{3} \right)}}{2}\\\dot{R}_2^{4}\\\dot{\theta}^{4}\\\dot{R}_1^{4}\end{matrix}\right]
"""


# velocity equation
qDot = simplify(-Cq.inv() * Ct)
pprint(qDot[5])
"""
\left[\begin{matrix}0\\0\\0\\\frac{l^{2} \sin{\left(\theta^{2} \right)} \sin{\left(t w \right)} \cos{\left(\theta^{3} \right)}}{2 \sin{\left(\theta^{2} - \theta^{3} \right)}}\\- \frac{l^{2} \sin{\left(t w \right)} \cos{\left(\theta^{2} \right)} \cos{\left(\theta^{3} \right)}}{2 \sin{\left(\theta^{2} - \theta^{3} \right)}}\\- \frac{\sin{\left(t w \right)} \cos{\left(\theta^{3} \right)}}{\sin{\left(\theta^{2} - \theta^{3} \right)}}\\\frac{l^{2} \cdot \left(3 \sin{\left(\theta^{2} - \theta^{3} \right)} + \sin{\left(\theta^{2} + \theta^{3} \right)}\right) \sin{\left(t w \right)}}{4 \sin{\left(\theta^{2} - \theta^{3} \right)}}\\- \frac{l^{2} \sin{\left(t w \right)} \cos{\left(\theta^{2} \right)} \cos{\left(\theta^{3} \right)}}{2 \sin{\left(\theta^{2} - \theta^{3} \right)}}\\\frac{l^{2} \sin{\left(t w \right)} \cos{\left(\theta^{2} \right)}}{l^{3} \sin{\left(\theta^{2} - \theta^{3} \right)}}\\l^{2} \sin{\left(t w \right)}\\0\\0\end{matrix}\right]
"""

answer=sin(w*t)/(cos(TH2) * tan(asin(l1 * sin(TH2) / l3)) - sin(TH2))
answer=simplify(answer)
pprint(answer)
