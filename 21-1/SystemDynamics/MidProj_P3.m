%% Reference: SeokHee Han's codes of slider-crank mechanism
clc;clear all, format long, format compact
global u1o u2o u2a u3a u3b u4b u4c u1c t th2_0 dth2 l1 l2 l3 l4


%% Analysis Configuration
t=0; %Start time
tend=input('End time: '); %End time
steps=input('Steps: '); %Steps
tsize=(tend-t)/steps; %Step size
etol=input('Error tolerance: '); %Error tolerance

t_log=zeros(1,steps);
th2_log=zeros(3,steps);
th3_log=zeros(3,steps); 
th4_log=zeros(3,steps);

%% Problem Configuration
l1=0.35; l2=0.2; l3=0.35; l4=0.25;
dth2=5; th2_0=deg2rad(57.27);

%% Local Coordinates (Fixed Points)
u1o=[0;0]; u2o=[0;0]; %O
u2a=[l2;0]; u3a=[0;0]; %A
u3b=[l3;0]; u4b=[0;0]; %B
u4c=[l4;0]; u1c=[l1;0]; %C

%% Initial Position Vector(Numeric)
Rx1=0; Ry1=0; th1=0;
Rx2=0; Ry2=0; th2=th2_0;
Rx3=l2*cos(th2); Ry3=l2*sin(th2); th3=deg2rad(9.8);
Rx4=Rx3+l3*cos(th3); Ry4=Ry3+l3*sin(th3); th4=deg2rad(240);

Q=[Rx1 Ry1 th1 Rx2 Ry2 th2 Rx3 Ry3 th3 Rx4 Ry4 th4]';

%% Define Terms
C=Constraint(Q,t);
disp(C)

Cq=CqJacob(Q);
disp(Cq)
Ct=zeros(12,1); Ct(12)=-5;

Cqt=zeros(12,12);
Ctt=zeros(12,1);


%% Simulate
for i=1:steps+1
    %% Position Analysis
    while(true)
        Qvar=linsolve(Cq,-C);
        Q=Q+Qvar;
        C=Constraint(Q,t);
        Cq=CqJacob(Q);
        if ((norm(Qvar)<=etol) || (norm(C)<=etol))
            break
        end
    end

    %% Velocity Analysis
    dQ0=zeros(12,1);
    dQvar=linsolve(Cq,-Ct);
    dQ=dQ0+dQvar;

    %% Acceleration Analysis
    Qd=QdCalc(Q,dQ);
    ddQ=linsolve(Cq,Qd);
    
    %% Write history
    t_log(1,i)=t;
    th2_log(:,i)=[Q(6);dQ(6);ddQ(6)];
    th3_log(:,i)=[Q(9);dQ(9);ddQ(9)];
    th4_log(:,i)=[Q(12);dQ(12);ddQ(12)];
    
    %% Proceed to next tiem step
    fprintf("Solving: %d/%d\n",i,steps)
    t=t+tsize;
end





%% Plotting
subplot(3,3,1);
plot(t_log,th2_log(1,:));
title('Angular Orientation(OA)')
xlabel('Time (t)')
ylabel('Orientation (rad)')
axis tight
grid on

subplot(3,3,4);
plot(t_log,th2_log(2,:));
title('Angular Velocity(OA)')
xlabel('Time (t)')
ylabel('Velocity (rad/s)')
axis tight
grid on

subplot(3,3,7);
plot(t_log,th2_log(3,:));
title('Angular Acceleration(OA)')
xlabel('Time (t)')
ylabel('Acceleration (rad/s^2)')
axis tight
grid on


subplot(3,3,2);
plot(t_log,th3_log(1,:));
title('Angular Orientation(AB)')
xlabel('Time (t)')
ylabel('Orientation (rad)')
axis tight
grid on

subplot(3,3,5);
plot(t_log,th3_log(2,:));
title('Angular Velocity(AB)')
xlabel('Time (t)')
ylabel('Velocity (rad/s)')
axis tight
grid on

subplot(3,3,8);
plot(t_log,th3_log(3,:));
title('Angular Acceleration(AB)')
xlabel('Time (t)')
ylabel('Acceleration (rad/s^2)')
axis tight
grid on


subplot(3,3,3);
plot(t_log,th4_log(1,:));
title('Angular Orientation(BC)')
xlabel('Time (t)')
ylabel('Orientation (rad)')
axis tight
grid on

subplot(3,3,6);
plot(t_log,th4_log(2,:));
title('Angular Velocity(BC)')
xlabel('Time (t)')
ylabel('Velocity (rad/s)')
axis tight
grid on

subplot(3,3,9);
plot(t_log,th4_log(3,:));
title('Angular Acceleration(BC)')
xlabel('Time (t)')
ylabel('Acceleration (rad/s^2)')
axis tight
grid on

sgtitle(sprintf('Analysis Result\nt=[0,%.3f], steps=%d, tolerance=%f',tend,steps,etol)) 














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

C=zeros(12,1);
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
Cq=zeros(12,12);

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

%% Qd Vector
function QdVector=QdCalc(Q,dQ)

global l1 l2 l3 l4
Rx1=Q(1); Ry1=Q(2); th1=Q(3);
Rx2=Q(4); Ry2=Q(5); th2=Q(6);
Rx3=Q(7); Ry3=Q(8); th3=Q(9);
Rx4=Q(10); Ry4=Q(11); th4=Q(12);
dth1=dQ(3);
dth2=dQ(6);
dth3=dQ(9);
dth4=dQ(12);

QdVector=zeros(12,1);
QdVector(6)=dth2^2*l2*cos(th2);
QdVector(7)=dth2^2*l2*sin(th2);
QdVector(8)=dth3^2*l3*cos(th3);
QdVector(9)=dth3^2*l3*sin(th3);
QdVector(10)=l1*cos(th1)*dth1^2 - l4*cos(th4)*dth4^2;
QdVector(11)=l1*sin(th1)*dth1^2 - l4*sin(th4)*dth4^2;
end

