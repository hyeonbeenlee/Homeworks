%% Initialization
clc; clear all;
syms Rx2 dRx2 ddRx2 Ry2 dRy2 ddRy2 th2 dth2 ddth2 real;
syms Rx3 dRx3 ddRx3 Ry3 dRy3 ddRy3 th3 dth3 ddth3 real;
syms g F M2 M3 l2 l3 m2 m3 J2 J3 Fx12 Fy12 Fx32 Fy32 t real;

%% Basic Variables
R2=[Rx2 Ry2]'; R3=[Rx3 Ry3]';
M=diag([m2 m2 J2 m3 m3 J3]);
q=[Rx2 Ry2 th2 Rx3 Ry3 th3]';
Qe=[0 -m2*g M2 0 -m3*g-F M3]';
uO1=[0 0]';uO2=[-l2/2 0]'; uA2=[l2/2 0]';uA3=[-l3/2 0]';
lambda=[-Fx12 -Fy12 Fx32 Fy32]';

%% Substitution
X=[M2 M3 F th2 th3 dth2 dth3 m2 m3 l2 l3 g J2 J3];
realX=[15 15 10 deg2rad(60) deg2rad(45) 10 5 0.5 1 0.5 1 9.8 2.57195310032267e-002 0.205576980005819];

%% Constraint Vector
C=[R2+A(th2)*uO2;R2+A(th2)*uA2-(R3+A(th3)*uA3)];

%% Constraint Jacobian
Cq=sym(zeros(length(C),length(q)));
for i=1:length(C)
    for j=1:length(q)
        Cq(i,j)=diff(C(i),q(j));
    end
end
Qd=-(dth2^2*[l2/2*cos(th2) l2/2*sin(th2) -l2/2*cos(th2) -l2/2*sin(th2)]'+dth3^2*[0 0 -l3/2*cos(th3) -l3/2*sin(th3)]');

%% Result
AccLambda=inv([M Cq';Cq zeros(4,4)])*[Qe;Qd];
AccLambda_0=vpa(subs(AccLambda,X,realX),6)

%% Independent Partitioning
Bi=sym(zeros(length(q),2));
Bi(1,:)=[-l2/2*sin(th2) 0];
Bi(2,:)=[l2/2*cos(th2) 0];
Bi(3,:)=[1 0];
Bi(4,:)=[-l2*sin(th2) -l3/2*sin(th3)];
Bi(5,:)=[l2*cos(th2) l3/2*cos(th3)];
Bi(6,:)=[0 1];

ri=dth2^2*l2*[-cos(th2)/2 -sin(th2)/2 0 -cos(th2) -sin(th2) 0]';
ri=ri+dth3^2*l3*[0 0 0 -cos(th3)/2 -sin(th3)/2 0]';

Mi=Bi'*M*Bi;
Qi=Bi'*(Qe-M*ri);
qi=inv(Mi)*Qi;

%% Initial Condition Check
qi_0=vpa(subs(qi,X,realX),6)


%% Function
function rotationmatrix=A(theta)
    rotationmatrix=[cos(theta) -sin(theta);sin(theta) cos(theta)];
end

