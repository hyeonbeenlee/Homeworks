clc,clear all;format short
a=input('Alpha(deg) for Euler Z: '); %RZ
b=input('Beta(deg) for Euler Y: '); %RY
r=input('Gamma(deg) for Euler X: '); %RX
P=input('Position row vector: '); %P
P=P';
a=a/180*pi;b=b/180*pi;r=r/180*pi;

A=[cos(a) -sin(a) 0;sin(a) cos(a) 0;0 0 1]; %RZ(a)  
B=[cos(b) 0 sin(b);0 1 0; -sin(b) 0 cos(b)]; %RY(b)
R=[1 0 0;0 cos(r) -sin(r);0 sin(r) cos(r)]; %RX(r)
EulerAngles=A*B*R;

HT=[EulerAngles P;0 0 0 1]
Target=input('Target to be converted: ');
Target=[Target';1]; %add placeholder
Result=HT*Target;
Result=Result(1:3) %remove placeholder