clc, clear
syms l2 l3 m2 m3 m4 J2 J3 J4 g h t real;
syms Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4 real;
syms dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4 dth4 real;

% syms Rx2(t) Ry2(t) th2(t) Rx3(t) Ry3(t) th3(t) Rx4(t) Ry4(t) th4(t) real;

syms ddRx2 ddRy2 ddth2 ddRx3 ddRy3 ddth3 ddRx4 ddRy4 ddth4 real;
syms Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fx41 Fy41 real;
syms M2 real;
%% Ry4, th4의 방정식 및 좌표는 제거한다
q=[Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4]';
dq=[dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4]';
ddq=[ddRx2 ddRy2 ddth2 ddRx3 ddRy3 ddth3 ddRx4 ddRy4]';
F=[Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fy41]';
Qe=[0 -m2*g M2 0 -m3*g 0 0 -m4*g]';



%% 제약조건은 일단 걍 먼저 때려박고 L.Multiplier로 맞춘다
%% 운동방정식으로 얻은 CqT랑 실제 dC/dq'랑 비교해서
%% CqT*lambda=운동방정식 우변이 되도록 lambda의 부호를 맞출 것이다
C=sym(zeros(6,1));
C(1)=Rx2-l2/2*cos(th2);
C(2)=Ry2-l2/2*sin(th2);
C(3)=Rx2+l2/2*cos(th2)-Rx3+l3/2*cos(th3);
C(4)=Ry2+l2/2*sin(th2)-Ry3+l3/2*sin(th3);
C(5)=Rx3+l3/2*cos(th3)-Rx4;
C(6)=Ry3+l3/2*sin(th3)-Ry4;
% C(7)=th4
C(7)=Ry4-h;

Cq=sym(zeros(length(C),length(q)));
for i=1:length(C)
    for j=1:length(q)
        Cq(i,j)=diff(C(i),q(j));
    end
end

%% Qd는 C 2계미분으로부터
Qd=sym(zeros(length(C),1))
Qd(1)=-dth2^2*l2/2*cos(th2);
Qd(2)=-dth2^2*l2/2*sin(th2);
Qd(3)=dth2^2*l2/2*cos(th2)+dth3^2*l3/2*cos(th3);
Qd(4)=dth2^2*l2/2*sin(th2)+dth3^2*l3/2*sin(th3);
Qd(5)=dth3^2*l3/2*cos(th3);
Qd(6)=dth3^2*l3/2*sin(th3);
Qd(7)=0;

%% 운동방정식 세울 때, 각 조인트마다 가해지는 반력(스칼라)로 설정
%% 1. 각 바디 내에서 서로 평형을 이루게 반대 방향으로 맞춰주고
%% 2. 다음 바디에서 이어진 반력에 반작용법칙 적용해 반대방향으로 맞춘다.
%% 3. 1로 돌아가서 다시 반복한다.
EOMtoCqT=sym(zeros(length(q),length(C)));
EOMtoCqT(1,1:4)=[1 0 -1 0];
EOMtoCqT(2,1:4)=[0 1 0 -1];
EOMtoCqT(3,1:4)=[l2/2*sin(th2) -l2/2*cos(th2) l2/2*sin(th2) -l2/2*cos(th2)];
EOMtoCqT(4,3:6)=[1 0 -1 0];
EOMtoCqT(5,3:6)=[0 1 0 -1];
EOMtoCqT(6,3:6)=[l3/2*sin(th3) -l3/2*cos(th3) l3/2*sin(th3) -l3/2*cos(th3)];
EOMtoCqT(7,5:6)=[1 0]; % NO Fx41 마찰력 없으므로 운동방정식 제외
EOMtoCqT(8,5:7)=[0 1 -1];



EOMtoCqT;
Cq';
isequal(EOMtoCqT,Cq') %당연히 다를 것, L.Multiplier로 맞춰줄 것이다

%% EOMtoCqT 3열, 4열, 5열,6열이 Cq'와 부호 반대이므로 아래와 같이
%% L.Multiplier 설정하면 Cq'*lambda=EOM우변-Qe 와 같다.
lambda=[Fx12 Fy12 -Fx23 -Fy23 -Fx34 -Fy34 -Fy41]';

Cq'*lambda;
EOMtoCqT*F;
isequal(EOMtoCqT*F,Cq'*lambda)
%위에 양변 Qe를 더하면 동일하게 운동방정식 우변이 도출된다.

%% Bi 입력
Bi=sym(zeros(length(q),2));

Bi(1,:)=[-l2/2*sin(th2) 0];
Bi(2,:)=[l2/2*cos(th2) 0];
Bi(3,:)=[1 0];
Bi(4,:)=[-l2*sin(th2) -l3/2*sin(th3)];
Bi(5,:)=[l2*cos(th2) l3/2*cos(th3)];
Bi(6,:)=[0 1];
Bi(7,:)=[-l2*sin(th2) -l3*sin(th3)];
Bi(8,:)=[0 0];




Cq*Bi

%% M, ddqi,ri
M=diag([m2 m2 J2 m3 m3 J3 m4 m4]);
ddqi=[ddth2 ddth3]';

ri=sym(zeros(length(C),1));
ri(1)=-l2/2*cos(th2)*dth2^2;
ri(2)=-l2/2*sin(th2)*dth2^2;
ri(3)=0;
ri(4)=-l2*cos(th2)*dth2^2-l3/2*cos(th3)*dth3^2;
ri(5)=-l2*sin(th2)*dth2^2-l3/2*sin(th3)*dth3^2;
ri(6)=0;
ri(7)=-l2*cos(th2)*dth2^2-l3*cos(th3)*dth3^2;
ri(8)=0;

ddqi_Calc=inv(Bi'*M*Bi)*(Bi'*Qe-Bi'*M*ri-Bi'*Cq'*lambda)
variables=[m2 m3 m4 J2 J3 J4 l2 l3 M2];
values=[1 1 1 1e-5 1e-5 1e-5 0.15 0.25 100*sin(pi*t/0.1)];
ddqi_Calc=vpa(subs(ddqi_Calc,variables,values),5);
pretty(vpa(combine(ddqi_Calc),5))

% Ans=inv([M Cq';Cq zeros(7,7)])*[Qe;Qd]
% 
% variables=[m2 m3 m4 J2 J3 J4 g l2 l3];
% values=[1 1 1 1e-5 1e-5 1e-5 9.81 0.15 0.25];
% Ans=vpa(subs(Ans,variables,values),5)
% 
% coords=[th2 th3 M2 dth2 dth3]
% initialvalues=[deg2rad(45) deg2rad(337.40194) 0 0 0]
% Ans=vpa(subs(Ans,coords,initialvalues),5)


