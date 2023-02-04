clear all,clc,format compact
syms th2 w2 a2 th3 w3 a3 l2 xp3 dxp3 
thisisforinv=[cos(th3) xp3*sin(th3);sin(th3) xp3*cos(th3)]
rhsv1=[w3^2*xp3*cos(th3);w3^2*xp3*sin(th3)]
rhsv2=[2*w3*dxp3*sin(th3);-2*w3*dxp3*cos(th3)]
rhsv3=[-a2*l2*sin(th2);a2*l2*cos(th2)]
rhsv4=[-w2^2*l2*cos(th2);-w2^2*l2*sin(th2)]
rhs=rhsv1+rhsv2+rhsv3+rhsv4;
result=inv(thisisforinv)*rhs;
pretty(result)