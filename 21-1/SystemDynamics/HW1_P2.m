clc;clear all
syms l1 l2 l3 l4 th2
k1=l1/l2;
k2=l1/l4;
k3=(l1^2+l2^2-l3^2+l4^2)/(2*l2*l4);
A=k3-k2*cos(th2)-k1-cos(th2);
B=2*sin(th2);
C=k3-k2*cos(th2)-k1+cos(th2);
th4=2*atan(-B+sqrt(B^2-4*A*C)/(2*A));
dth4=diff(th4,th2);
ddth4=diff(dth4,th2);
pretty(th4)
pretty(dth4)
pretty(ddth4)