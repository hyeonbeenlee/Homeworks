clc, clear
syms l2 l3 m2 m3 m4 g h real;
syms Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4 real;
syms Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fx41 Fy41 real;
syms M2 real;

q=[Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4]';
lambda=[Fx12 Fy12 Fx23 Fy23 Fx34 Fy34 Fx41 Fy41]';
Qe=[0 -m2*g M2 0 -m3*g 0 0 -m4*g]';



C=sym(zeros(8,1));
C(1)=Rx2-l2/2*cos(th2);
C(2)=Ry2-l2/2*sin(th2);
C(3)=Rx2+l2/2*cos(th2)-Rx3+l3/2*cos(th3);
C(4)=Ry2+l2/2*sin(th2)-Ry3+l3/2*sin(th3);
C(5)=Rx3+l3/2*cos(th3)-Rx4;
C(6)=Ry3+l3/2*sin(th3)-Ry4;
C(7)=th4;
C(8)=Ry4-h;






Cq=sym(zeros(length(C),length(q)));
for i=1:length(C)
    for j=1:length(q)
        Cq(i,j)=diff(C(i),q(j));
    end
end

EOMtoCqT=sym(zeros(length(q),length(C)));
EOMtoCqT(1,1:4)=[1 0 1 0];
EOMtoCqT(2,1:4)=[0 1 0 1];
EOMtoCqT(3,1:4)=[l2/2*sin(th2) -l2/2*cos(th2) -l2/2*sin(th2) l2/2*cos(th2)];
EOMtoCqT(4,3:6)=[-1 0 1 0];
EOMtoCqT(5,3:6)=[0 -1 0 1];
EOMtoCqT(6,3:6)=[-l3/2*sin(th3) l3/2*cos(th3) -l3/2*sin(th3) l3/2*cos(th3)];
EOMtoCqT(7,5:8)=[-1 0 0 0];
EOMtoCqT(8,5:8)=[0 -1 0 1];
% EOMtoCqT(9,5:8)=[0 0 0 0];




fprintf('뉴턴 오일러 방정식 우변\n')
pretty(EOMtoCqT*lambda+Qe)
fprintf('제약조건 방정식')
C
fprintf('\n뉴턴 오일러 방정식에서 만든 Cq^T')
EOMtoCqT
fprintf('\ndC/dq로 만든 Cq')
Cq
fprintf('\n둘이 맞는지 검증')

EOMtoCqT
Cq'

