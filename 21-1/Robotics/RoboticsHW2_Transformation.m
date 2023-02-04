clc, format compact, format short e
syms L1 L2 L3 D1 D2 D3 TH1 TH2 TH3;
a=input('Link length of link (i-1): ');
alp=input('Link twist(rad) of link (i-1): ');
d=input('Link offset at axis (i): ');
th=input('Joint angle(rad) at axis (i): ');
R=sym(zeros(3,3));
R(1,:)=[cos(th),-sin(th),0];
R(2,:)=[sin(th)*cos(alp),cos(th)*cos(alp),-sin(alp)];
R(3,:)=[sin(th)*sin(alp),cos(th)*sin(alp),cos(alp)];
Transl=[a;-sin(alp)*d;cos(alp)*d];
Dummy=[0 0 0 1];
T=sym(zeros(4,4));
T(1:3,1:3)=R;
T(1:3,4)=Transl;
T(4,:)=Dummy;
T=vpa(T,4)
