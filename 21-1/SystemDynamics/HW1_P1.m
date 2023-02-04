clc,clear all
syms l2 th2 dth2 ddth2 l3 th3 dth3 ddth3;
thisisforinv=[1 l3*sin(th3);0 -l3*cos(th3)]
rhsvec1=[-ddth2*l2*sin(th2);ddth2*l2*cos(th2)]
rhsvec2=[-dth2^2*l2*cos(th2);-dth2^2*l2*sin(th2)]
rhsvec3=[-dth3^2*l3*cos(th3);-dth3^2*l3*sin(th3)]
result=inv(thisisforinv)*(rhsvec1+rhsvec2+rhsvec3);
pretty(result)