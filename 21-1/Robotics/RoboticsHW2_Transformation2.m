clc,format short e, format loose
syms TH1 TH2 TH3 L1 L2 L3;

%Hard coding the sum-of-angle result of T_03
T_03=sym(zeros(4,4));
TH123=TH1+TH2+TH3;
T_03(1,:)=[cos(TH123),-sin(TH123),0,L2*cos(TH1+TH2)+L1*cos(TH1)];
T_03(2,:)=[sin(TH123),cos(TH123),0,L1*sin(TH1)+L2*sin(TH1+TH2)];
T_03(3:4,:)=[0,0,1,0;0,0,0,1];

%Hard coding of T_3H
T_3H=sym(zeros(4,4)); %For calc. with T_03, again symbolically declare
T_3H(1:3,1:3)=sym(eye(3));
T_3H(4,:)=[0,0,0,1];
T_3H(1,4)=L3;

%Calculate T_0H
T_0H=T_03*T_3H;

%Substitution for i)
i_T_03=subs(T_03,[TH1,TH2,TH3,L1,L2,L3],[0,0,0,4,3,2]);
i_T_0H=subs(T_0H,[TH1,TH2,TH3,L1,L2,L3],[0,0,0,4,3,2]);

%Substitution for ii)
ii_T_03=vpa(subs(T_03,[TH1,TH2,TH3],[10,20,30]/180*pi),5);
ii_T_0H=vpa(subs(T_0H,[TH1,TH2,TH3],[10,20,30]/180*pi),5);
ii_T_03=vpa(subs(ii_T_03,[L1,L2,L3],[4,3,2]),5);
ii_T_0H=vpa(subs(ii_T_0H,[L1,L2,L3],[4,3,2]),5);

%Substitution for iii)
iii_T_03=vpa(subs(T_03,[TH1,TH2,TH3],[90,90,90]/180*pi),5);
iii_T_0H=vpa(subs(T_0H,[TH1,TH2,TH3],[90,90,90]/180*pi),5);
iii_T_03=vpa(subs(iii_T_03,[L1,L2,L3],[4,3,2]),5);
iii_T_0H=vpa(subs(iii_T_0H,[L1,L2,L3],[4,3,2]),5);
