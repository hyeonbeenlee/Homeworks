clc,format short e
a=input('Alpha(deg) for Euler Z: '); %RZ
b=input('Beta(deg) for Euler Y: '); %RY
r=input('Gamma(deg) for Euler X: '); %RX
P=input('Position row vector: '); %P
P=P';
a=a/180*pi;
b=b/180*pi;
r=r/180*pi;

R1=[cos(a) -sin(a) 0;sin(a) cos(a) 0;0 0 1]; %RZ(a)  
R2=[cos(b) 0 sin(b);0 1 0; -sin(b) 0 cos(b)]; %RY(b)
R3=[1 0 0;0 cos(r) -sin(r);0 sin(r) cos(r)]; %RX(r)
EulerAngles=R1*R2*R3;

HT=[EulerAngles P;0 0 0 1]

Rt=HT(1:3,1:3)'; %Transposed R from HT
P=HT(1:3,4); %Origin position vector
P=-Rt*P; %New origin position vector
HTinv=[Rt P;0 0 0 1]