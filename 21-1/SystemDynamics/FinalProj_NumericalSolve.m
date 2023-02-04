clear all; clc; close all;  format short;

%% Slider-Crank (Dynamics)
global u1o u2o u2a u3a u3b u4b d2_0 l2 l3 g mass
t = 0;
endTime = 0.2;
step = 120;
orgstep=step;
h = endTime/step; % time Step
orgh=h;


g = -9.81;

%% Initical Config
l2 = 0.15;   l3 = 0.25; H=0.01;
d2_0 = deg2rad(45);
% Crankshaft
Rx2 = l2*cos(d2_0)/2;    Ry2 = l2*sin(d2_0)/2;    d2 = d2_0;
% Connecting rod
d3 = deg2rad(337.40194);	Rx3 = l2*cos(d2)+l3*cos(d3)/2;	Ry3 = l2*sin(d2)+l3*sin(d3)/2; 
% Sliding block
Rx4 = l2*cos(d2) + l3*cos(d3);    Ry4 = H;    d4 = 0;
% M, J
m2 = 1; j2 = 1e-5;
m3 = 1; j3 = 1e-5;
m4 = 1; j4 = 1e-5;

mass = diag([m2, m2, j2, m3, m3, j3, m4, m4, j4]);

%% Local coord - joint origin
u1o = [0 0]';       u2o = [-l2/2 0]';
u2a = [l2/2 0]';    u3a = [-l3/2 0]';
u3b = [l3/2 0]';    u4b = [0 0]';

% Generalized coordinate
Euler_q_i = [Rx2 Ry2 d2 Rx3 Ry3 d3 Rx4 Ry4 d4]';
Euler_qDot_i = zeros(9,1);

RK2_q_i = [Rx2 Ry2 d2 Rx3 Ry3 d3 Rx4 Ry4 d4]';
RK2_qDot_i = zeros(9,1);

RK4_q_i = [Rx2 Ry2 d2 Rx3 Ry3 d3 Rx4 Ry4 d4]';
RK4_qDot_i = zeros(9,1);

Ref_RK4_q_i = [Rx2 Ry2 d2 Rx3 Ry3 d3 Rx4 Ry4 d4]';
Ref_RK4_qDot_i = zeros(9,1);

%% Solve RK4
for i=1:step    
    time(i) = t;
    
    % Euler
    Euler_Y = [Euler_q_i ; Euler_qDot_i]; % [위치 1계미분]'
    Euler_k1 = Grad(t, Euler_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    Euler_Y_Next = Euler_Y+ Euler_k1*h; % Next step [위치 속도]', 현재의 기울기 사용 1step 전진
    
    Euler_q_i = Euler_Y_Next(1:9);
    Euler_qDot_i = Euler_Y_Next(10:18);
    Euler_qDDot_i = Euler_k1(10:18);
    
    
    % RK2
    RK2_Y = [RK2_q_i ; RK2_qDot_i]; % [위치 1계미분]' 
    RK2_k1 = Grad(t, RK2_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    RK2_k2 = Grad(t + 0.5*h, RK2_Y + h*RK2_k1); % +1step의 기울기를 예측
    RK2_Y_Next = RK2_Y + h*(RK2_k1+RK2_k2)/2;  % 현재, +1step의 기울기 평균값으로 1step 전진
    
    RK2_q_i = RK2_Y_Next(1:9);
    RK2_qDot_i = RK2_Y_Next(10:18);
    RK2_qDDot_i = RK2_k1(10:18); 
    
    % RK4
    RK4_Y = [RK4_q_i ; RK4_qDot_i]; % [위치 1계미분]' 
    k1 = Grad(t, RK4_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    k2 = Grad(t + 0.5*h, RK4_Y + k1*0.5*h); % 현재 기울기 사용 +0.5step 기울기 예측
    k3 = Grad(t + 0.5*h, RK4_Y + k2*0.5*h); % 위에서 예측된 기울기로 +0.5step 기울기 한번 더 예측
    k4 = Grad(t + h, RK4_Y + k3*h); % 위에서 예측된 중간값 기울기로 +1step 기울기 예측
    RK4_Y_Next = RK4_Y + (k1 + 2*k2 + 2*k3 + k4)/6*h;  % 1step 내 4개의 기울기 참조하여 1step 전진
    
    RK4_q_i = RK4_Y_Next(1:9);
    RK4_qDot_i = RK4_Y_Next(10:18);
    RK4_qDDot_i = k1(10:18); 
    
    % for External force plot
    Qe = Q_e(m2, m3, m4, t);
    torque(i) = Qe(3);

       
    
    % for plot
    Euler_q(:, i) = Euler_q_i;
    Euler_qDot(:, i) = Euler_qDot_i;
    Euler_qDDot(:, i) = Euler_qDDot_i;
    
    RK2_q(:, i) = RK2_q_i;
    RK2_qDot(:, i) = RK2_qDot_i;
    RK2_qDDot(:, i) = RK2_qDDot_i;
    
    RK4_q(:, i) = RK4_q_i;
    RK4_qDot(:, i) = RK4_qDot_i;
    RK4_qDDot(:, i) = RK4_qDDot_i;
    
    fprintf("t: %d \n",time(i));    
    t = t + h;    
end


%% Reference Solve RK4
t=0;
step = 10000;
h = endTime/step; % time Step
for i=1:10000    
    ref_time(i) = t;

    % RK4
    Ref_RK4_Y = [Ref_RK4_q_i ; Ref_RK4_qDot_i];       
    k1 = Grad(t, Ref_RK4_Y); % t [속도 가속도] 현재의 기울기
    k2 = Grad(t + 0.5*h, Ref_RK4_Y + k1*0.5*h); % 현재 기울기 사용 0.5step 전진 기울기 예측
    k3 = Grad(t + 0.5*h, Ref_RK4_Y + k2*0.5*h); % 위에서 예측된 값으로 0.5step 전진 기울기 한번 더 예측
    k4 = Grad(t + h, Ref_RK4_Y + k3*h); % 위에서 예측된 값으로 1step 전진 기울기 예측
    Ref_RK4_Y_Next = Ref_RK4_Y + (k1 + 2*k2 + 2*k3 + k4)/6*h;  %룬지쿠타 4계방법으로 최종 기울기 취해서 1step 전진
    
    Ref_RK4_q_i = Ref_RK4_Y_Next(1:9);
    Ref_RK4_qDot_i = Ref_RK4_Y_Next(10:18);
    Ref_RK4_qDDot_i = k1(10:18); 
    
    % for External force plot
    Ref_Qe = Q_e(m2, m3, m4, t);
    Ref_torque(i) = Ref_Qe(3);

       
    
    Ref_RK4_q(:, i) = Ref_RK4_q_i;
    Ref_RK4_qDot(:, i) = Ref_RK4_qDot_i;
    Ref_RK4_qDDot(:, i) = Ref_RK4_qDDot_i;
    
    fprintf("t: %d \n",ref_time(i));    
    t = t + h;    
end

%% Plot Degree vs Rx3 Pos Vel Acc

% Plot to time
sgtitle(['Steps :',num2str(orgstep),', Time increment: ',num2str(orgh),', Slider offset: ',num2str(H),'(m)'])
subplot(3,1,1)
plot(rad2deg(Euler_q(3,:)),Euler_q(4,:))
hold on
plot(rad2deg(RK2_q(3,:)),RK2_q(4,:))
plot(rad2deg(RK4_q(3,:)),RK4_q(4,:))
plot(rad2deg(Ref_RK4_q(3,:)),Ref_RK4_q(4,:),'-*','MarkerIndices',1:100:length(ref_time))
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('\theta^2(deg)')
ylabel('R_x^3(Position)')
xlim([45 600])

subplot(3,1,2)
plot(rad2deg(Euler_q(3,:)),Euler_qDot(4,:))
hold on
plot(rad2deg(RK2_q(3,:)),RK2_qDot(4,:))
plot(rad2deg(RK4_q(3,:)),RK4_qDot(4,:))
plot(rad2deg(Ref_RK4_q(3,:)),Ref_RK4_qDot(4,:),'-*','MarkerIndices',1:100:length(ref_time))
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('\theta^2(deg)')
ylabel('R_x^3(Velocity)')
xlim([45 600])

subplot(3,1,3)
plot(rad2deg(Euler_q(3,:)),Euler_qDDot(4,:))
hold on
plot(rad2deg(RK2_q(3,:)),RK2_qDDot(4,:))
plot(rad2deg(RK4_q(3,:)),RK4_qDDot(4,:))
plot(rad2deg(Ref_RK4_q(3,:)),Ref_RK4_qDDot(4,:),'-*','MarkerIndices',1:100:length(ref_time))
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('\theta^2(deg)')
ylabel('R_x^3(Acceleration)')
xlim([45 600])


%% Plot to time
% sgtitle(['Steps :',num2str(orgstep),', Time increment: ',num2str(orgh),', Slider offset: ',num2str(H),'(m)'])
% subplot(2,2,1)
% plot(time,Euler_q(4,:))
% hold on
% plot(time,RK2_q(4,:))
% plot(time,RK4_q(4,:))
% plot(ref_time,Ref_RK4_q(4,:),'-*','MarkerIndices',1:100:length(ref_time))
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlabel('Time(sec)')
% ylabel('R_x^3(Position)')
% 
% subplot(2,2,2)
% plot(time,Euler_qDot(4,:))
% hold on
% plot(time,RK2_qDot(4,:))
% plot(time,RK4_qDot(4,:))
% plot(ref_time,Ref_RK4_qDot(4,:),'-*','MarkerIndices',1:100:length(ref_time))
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlabel('Time(sec)')
% ylabel('R_x^3(Velocity)')
% 
% subplot(2,2,3)
% plot(time,Euler_qDDot(4,:))
% hold on
% plot(time,RK2_qDDot(4,:))
% plot(time,RK4_qDDot(4,:))
% plot(ref_time,Ref_RK4_qDDot(4,:),'-*','MarkerIndices',1:100:length(ref_time))
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlabel('Time(sec)')
% ylabel('R_x^3(Acceleration)')


%% Functions
function YDot = Grad(t, Y) %Y = [q_i ; qDot_i]; 초기위치, 속도, 시간을 부여한다
    global mass 
    
    m2 = mass(1,1); m3 = mass(4,4); m4 = mass(7,7); 
    q_i = Y(1:9); %위치
    qDot_i = Y(10:18); %속도
    
    % Cq, Qd 자코비안과 Qd를 불러와서 행렬구성한다
    Cq = C_q(q_i);
    Qd = Q_d(q_i, qDot_i);

    % External force 외력
    Qe = Q_e(m2, m3, m4, t);
    
    % Symmetric Augmented formulation 포뮬레이션 구성한다
    A = [mass Cq'; Cq zeros(8,8)];
    b = [Qe ; Qd];
    
    % solve 
    x = linsolve(A,b); %역행렬 구한다=가속도와 반력을 구하게된다
    qDDot = x(1:9); %구해진 일반화좌표
    lambda = x(10:length(x)); %라그랑지 멀티플라이어
        
    YDot = [qDot_i ; qDDot]; %속도와 가속도로 이루어진 벡터 반환한다
end

function Qd = Q_d(q, qDot)
    global l2 l3
    q3 = q(3);          q6 = q(6);
    qDot3 = qDot(3);	qDot6 = qDot(6);

    Qd = ...
    [ 0, 0,  (l2*qDot3*cos(q3))/2, 0, 0,                     0, 0, 0, 0;...
      0, 0,  (l2*qDot3*sin(q3))/2, 0, 0,                     0, 0, 0, 0;...
      0, 0, -(l2*qDot3*cos(q3))/2, 0, 0, -(l3*qDot6*cos(q6))/2, 0, 0, 0;...
      0, 0, -(l2*qDot3*sin(q3))/2, 0, 0, -(l3*qDot6*sin(q6))/2, 0, 0, 0;...
      0, 0,                     0, 0, 0, -(l3*qDot6*cos(q6))/2, 0, 0, 0;...
      0, 0,                     0, 0, 0, -(l3*qDot6*sin(q6))/2, 0, 0, 0;...
      0, 0,                     0, 0, 0,                     0, 0, 0, 0;...
      0, 0,                     0, 0, 0,                     0, 0, 0, 0];
  
    Qd = -Qd*qDot;
end

function Qe = Q_e(m2, m3, m4, t)
    global g
    Qt = 100*sin(pi*t/0.1); % torque
    Qe = [0 ; m2*g ; Qt ; 0 ; m3*g ; 0 ; 0 ; m4*g ; 0];
end

function Cq = C_q(q)
    global l2 l3 
    q3 = q(3);  q6 = q(6);
    Cq = [ 1, 0,  (l2*sin(q3))/2,  0,  0,               0,  0,  0, 0;...
           0, 1, -(l2*cos(q3))/2,  0,  0,               0,  0,  0, 0;...
           1, 0, -(l2*sin(q3))/2, -1,  0, -(l3*sin(q6))/2,  0,  0, 0;...
           0, 1,  (l2*cos(q3))/2,  0, -1,  (l3*cos(q6))/2,  0,  0, 0;...
           0, 0,               0,  1,  0, -(l3*sin(q6))/2, -1,  0, 0;...
           0, 0,               0,  0,  1,  (l3*cos(q6))/2,  0, -1, 0;...
           0, 0,               0,  0,  0,               0,  0,  1, 0;...
           0, 0,               0,  0,  0,               0,  0,  0, 1];
end

function a = Step(time, t0, h0, t1, h1)
    if (time<=t0)
        a = h0;        
    elseif (t0<=time && time<=t1)
        a = h0 + (h1 - h0) * ((time - t0)/(t1 - t0))^2 * (3 - 2*((time - t0)/(t1 - t0)));
    else
        a = h1;
    end
end

function matA = A(d)
    matA = [cos(d) -sin(d) ; sin(d) cos(d)]; % Transformation Matrix
end
function matB = B(d)
    matB = [-sin(d) cos(d) ; -cos(d) -sin(d)]; % Transformation Matrix
end



%% Jacobian components
%{
C46 = 0.5*l2*sin(d2);   C56 = -0.5*l2*cos(d2);  C66 = -0.5*l2*sin(d2);  C76 = 0.5*l2*cos(d2);
C69 = -0.5*l3*sin(d3);  C79 = 0.5*l3*cos(d3);   C89 = -0.5*l3*sin(d3);  C99 = 0.5*l3*cos(d3);
%}