clc, clear all, format loose
syms l1 l2 l3 l4 t th2_0 dth2_0 real;
syms Rx1 Ry1 th1 Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4 real;
syms dRx1 dRy1 dth1 dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4 dth4 real;
global u1o u2o u2a u3a u3b u4b u4c u1c
%% Local Coordinates (Fixed Points)
u1o=[0;0]; u2o=[0;0]; %O
u2a=[l2;0]; u3a=[0;0]; %A
u3b=[l3;0]; u4b=[0;0]; %B
u4c=[l4;0]; u1c=[l1;0]; %C

Q=[Rx1 Ry1 th1 Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4]';
dQ=[dRx1 dRy1 dth1 dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4 dth4]';

%% C
C=Constraint(Q,t)

%% Cq = d(C)/d(Q)
Cq_calc=sym(zeros(12,12));
for i=1:size(C,1)
	for j=1:size(Q,1)
        Cq_calc(i,j)=diff(C(i),Q(j));
    end
end
Cq=CqJacob(Q) %Manually input constraint Jacobian library
Cq==Cq_calc %Symbolic math


%% (Cq*dQ)q = d(Cq*dQ)/d(Q)
CqQdot=Cq_calc*dQ;
CqQdot_q=sym(zeros(12,12));
for i=1:size(CqQdot,1)
	for j=1:size(Q,1)
        CqQdot_q(i,j)=diff(CqQdot(i),Q(j));
    end
end
CqQdot_q
%% Qd
Qd=-CqQdot_q*dQ


%% Functions
%Angle transformation
function matA=A(d)
matA=[cos(d) -sin(d);sin(d) cos(d)];
end

%Differentiated transformation
function matAt=At(d)
matAt=[-sin(d) -cos(d);cos(d) -sin(d)];
end

%Driving constraint
function theta2=drive(t)
global dth2
theta2=dth2*t;
end

%% Constraint Vector
function C=Constraint(Q,t)
global u1o u2o u2a u3a u3b u4b u4c u1c th2_0

Rx1=Q(1); Ry1=Q(2); th1=Q(3);
Rx2=Q(4); Ry2=Q(5); th2=Q(6);
Rx3=Q(7); Ry3=Q(8); th3=Q(9);
Rx4=Q(10); Ry4=Q(11); th4=Q(12);

C=sym(zeros(12,1));
C(1:3)=[Rx1;Ry1;th1]; %Ground constraint
C(4:5)=[Rx1;Ry1]+A(th1)*u1o-[Rx2;Ry2]-A(th2)*u2o; %Rev O
C(6:7)=[Rx2;Ry2]+A(th2)*u2a-[Rx3;Ry3]-A(th3)*u3a; %Rev A
C(8:9)=[Rx3;Ry3]+A(th3)*u3b-[Rx4;Ry4]-A(th4)*u4b; %Rev B
C(10:11)=[Rx1;Ry1]+A(th1)*u1c-[Rx4;Ry4]-A(th4)*u4c; %Rev C
C(12)=th2-th2_0-drive(t); %Driving
end

%% Constraint Jacobian Matrix
function Cq=CqJacob(Q)

global u1o u2o u2a u3a u3b u4b u4c u1c
Rx1=Q(1); Ry1=Q(2); th1=Q(3);
Rx2=Q(4); Ry2=Q(5); th2=Q(6);
Rx3=Q(7); Ry3=Q(8); th3=Q(9);
Rx4=Q(10); Ry4=Q(11); th4=Q(12);
Cq=sym(zeros(12,12));

%Standard constraint libraries
for k=1:3
    Cq(k,k)=1; %Ground
end
Cq(4:5,1:6)=[eye(2),At(th1)*u1o,-eye(2),-At(th2)*u2o]; %R1-R2, RevO
Cq(6:7,4:9)=[eye(2),At(th2)*u2a,-eye(2),-At(th3)*u3a];%R2-R3, RevA
Cq(8:9,7:12)=[eye(2),At(th3)*u3b,-eye(2),-At(th4)*u4b]; %R3-R4, RevB
Cq(10:11,1:3)=[eye(2),At(th1)*u1c]; Cq(10:11,10:12)=[-eye(2),-At(th4)*u4c]; %R1-R4, RevC
Cq(12,6)=1; %Driving
end