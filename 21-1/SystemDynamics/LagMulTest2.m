clc, clear
syms l2 l3 m2 m3 m4 J2 J3 J4 g h real;
syms Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4 real;
syms dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4 dth4 real;
syms ddRx2 ddRy2 ddth2 ddRx3 ddRy3 ddth3 ddRx4 ddRy4 ddth4 real;
syms Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fx41 Fy41 real;
syms M2 real;
%% th4의 회전방정식은 제거한다, 반력요소는 제거하지 않는다
q=[Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4]';
dq=[dRx2 dRy2 dth2 dRx3 dRy3 dth3 dRx4 dRy4]';
ddq=[ddRx2 ddRy2 ddth2 ddRx3 ddRy3 ddth3 ddRx4 ddRy4 ddth4];
F=[Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fx41 Fy41]';
Qe=[0 -m2*g M2 0 -m3*g 0 0 -m4*g]';


%% 제약조건은 일단 걍 먼저 때려박고 L.Multiplier로 맞춘다
%% 운동방정식으로 얻은 CqT랑 실제 dC/dq'랑 비교해서
%% CqT*lambda=운동방정식 우변이 되도록 lambda의 부호를 맞출 것이다
C=sym(zeros(8,1));
C(1)=Rx2-l2/2*cos(th2);
C(2)=Ry2-l2/2*sin(th2);
C(3)=Rx2+l2/2*cos(th2)-Rx3+l3/2*cos(th3);
C(4)=Ry2+l2/2*sin(th2)-Ry3+l3/2*sin(th3);
C(5)=Rx3+l3/2*cos(th3)-Rx4;
C(6)=Ry3+l3/2*sin(th3)-Ry4;
C(7)=th4; %Prismatic 제약조건은 먼저
C(8)=Ry4-h;

Cq=sym(zeros(length(C),length(q)));
for i=1:length(C)
    for j=1:length(q)
        Cq(i,j)=diff(C(i),q(j));
    end
end

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
EOMtoCqT(7,5:8)=[1 0 0 0]; % NO Fx41 마찰력 없으므로 운동방정식 제외
EOMtoCqT(8,5:8)=[0 1 0 -1];


EOMtoCqT;
Cq';
isequal(EOMtoCqT,Cq') %당연히 다를 것, L.Multiplier로 맞춰줄 것이다

%% EOMtoCqT 3열, 4열, 5열,6열, 8열이 Cq'와 부호 반대이므로 아래와 같이
%% L.Multiplier 설정하면 Cq'*lambda=EOM우변-Qe 와 같다.
lambda=[Fx12 Fy12 -Fx23 -Fy23 -Fx34 -Fy34 Fx41 -Fy41]';

Cq'*lambda;
EOMtoCqT*F;
isequal(EOMtoCqT*F,Cq'*lambda)
%위에 양변 Qe를 더하면 동일하게 운동방정식 우변이 도출된다.

%% Bi 입력
Bi=sym(zeros(length(C),2));
Bi(1,:)=[-l2/2*sin(th2) 0];
Bi(2,:)=[l2/2*cos(th2) 0];
Bi(3,:)=[1 0];
Bi(4,:)=[-l2*sin(th2) -l3/2*sin(th3)];
Bi(5,:)=[l2*cos(th2) l3/2*cos(th3)];
Bi(6,:)=[1 0];
Bi(7,:)=[-l2*sin(th2) -l3*sin(th3)];
Bi(8,:)=[l2*cos(th2) l3*cos(th3)]

%% M, qi,ri
M=diag([m2 m2 J2 m3 m3 J3 m4 m4]);
ddqi=[ddth2 ddth3]';