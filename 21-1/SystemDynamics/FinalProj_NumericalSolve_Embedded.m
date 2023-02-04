clc,clear all,format long,format compact
global m2 m3 m4 J2 J3 J4 l2 l3 g h
%% 상수, 초기값 정의
m2=1;   m3=1;   m4=1;
J2=1e-5;    J3=1e-5;    J4=1e-5;
l2=0.15;    l3=0.25;    g=9.81; h=0.01;

%% 시뮬레이션 설정
t=0;    endTime=0.2;    steps=1000;
h=endTime/steps;

%% 초기값 부여 및 체크
Q_0=[deg2rad(45) deg2rad(337.40194)]'; % th2 th3 초기 위치
dQ_0=[0 0]'; % dth2 dth3 초기 속도
Y=[Q_0;dQ_0]; %초기 State Vector 정의

time=0; %시간 배열
%% 시뮬레이션 시작

% 수치적분 비교용
Euler_Y=[Q_0;dQ_0]; 
RK2_Y=[Q_0;dQ_0];
RK4_Y=[Q_0;dQ_0];
Ref_Y=[Q_0;dQ_0];
for i=1:steps
    
    %%%%%%%%%% Euler Method %%%%%%%%%%
    k1=Grad(t,Euler_Y);
    Euler_Y_Next=Euler_Y+k1*h;
    % 기록
    Euler_Q(:,i)=Euler_Y_Next(1:2); %State Vector 위치 th2 th3
    Euler_dQ(:,i)=Euler_Y_Next(3:4); %State Vector 속도 dth2 dth3
    Euler_ddQ(:,i)=k1(3:4); %가속도 ddth2 ddth3
    Euler_R3Q(:,i)=RX3(t,Euler_Y); %바디3 위치 속도 가속도
    % State 벡터 업데이트
    Euler_Y=Euler_Y_Next;
    
    %%%%%%%%%% RK2 Method %%%%%%%%%%
    k1 = Grad(t, RK2_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    k2 = Grad(t + 0.5*h, RK2_Y + h*k1); % +1step의 기울기를 예측
    RK2_Y_Next = RK2_Y + h*(k1+k2)/2;  % 현재, +1step의 기울기 평균값으로 1step 전진
    % 기록
    RK2_Q(:,i)=RK2_Y_Next(1:2); %State Vector 위치 th2 th3
    RK2_dQ(:,i)=RK2_Y_Next(3:4); %State Vector 속도 dth2 dth3
    RK2_ddQ(:,i)=k1(3:4); %가속도 ddth2 ddth3
    RK2_R3Q(:,i)=RX3(t,RK2_Y); %바디3 위치 속도 가속도
    % State 벡터 업데이트
    RK2_Y=RK2_Y_Next;
    
    %%%%%%%%%% RK4 Method %%%%%%%%%%
    k1 = Grad(t, RK4_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    k2 = Grad(t + 0.5*h, RK4_Y + k1*0.5*h); % 현재 기울기 사용 +0.5step 기울기 예측
    k3 = Grad(t + 0.5*h, RK4_Y + k2*0.5*h); % 위에서 예측된 기울기로 +0.5step 기울기 한번 더 예측
    k4 = Grad(t + h, RK4_Y + k3*h); % 위에서 예측된 중간값 기울기로 +1step 기울기 예측
    RK4_Y_Next = RK4_Y + (k1 + 2*k2 + 2*k3 + k4)/6*h;  % 1step 내 4개의 기울기 참조하여 1step 전진
    % 기록
    RK4_Q(:,i)=RK4_Y_Next(1:2); %State Vector 위치 th2 th3
    RK4_dQ(:,i)=RK4_Y_Next(3:4); %State Vector 속도 dth2 dth3
    RK4_ddQ(:,i)=k1(3:4); %가속도 ddth2 ddth3
    RK4_R3Q(:,i)=RX3(t,RK4_Y); %바디3 위치 속도 가속도
    % State 벡터 업데이트
    RK4_Y=RK4_Y_Next;

    
    % 다음 스텝 준비
    t=t+h;
    time(i)=t;
    fprintf('Solving, time=%.5f\n',t)
end

% 레퍼런스 솔루션 RK4
t=0;    h=endTime/10000;
for i=1:10000
    %%%%%%%%%% RK4 Method %%%%%%%%%%
    k1 = Grad(t, Ref_Y); % [1계미분 2계미분]'= Grad(t,[위치 1계미분]'), 현재step 1계 2계 미분
    k2 = Grad(t + 0.5*h, Ref_Y + k1*0.5*h); % 현재 기울기 사용 +0.5step 기울기 예측
    k3 = Grad(t + 0.5*h, Ref_Y + k2*0.5*h); % 위에서 예측된 기울기로 +0.5step 기울기 한번 더 예측
    k4 = Grad(t + h, Ref_Y + k3*h); % 위에서 예측된 중간값 기울기로 +1step 기울기 예측
    Ref_Y_Next = Ref_Y + (k1 + 2*k2 + 2*k3 + k4)/6*h;  % 1step 내 4개의 기울기 참조하여 1step 전진
    % 기록
    Ref_Q(:,i)=Ref_Y_Next(1:2); %State Vector 위치 th2 th3
    Ref_dQ(:,i)=Ref_Y_Next(3:4); %State Vector 속도 dth2 dth3
    Ref_ddQ(:,i)=k1(3:4); %가속도 ddth2 ddth3
    Ref_R3Q(:,i)=RX3(t,Ref_Y); %바디3 위치 속도 가속도
    % State 벡터 업데이트
    Ref_Y=Ref_Y_Next;

    
    % 다음 스텝 준비
    t=t+h;
    ref_time(i)=t;
    fprintf('Reference Solving, time=%.6f\n',t)
end


%% 플롯 1 세타vsRx3
% sgtitle(['System Dynamics Final Project 2015100767 이현빈: ',num2str(steps),' Steps for ', num2str(endTime),'sec'])
% subplot(2,2,1)
% plot(rad2deg(Euler_Q(1,:)),Euler_R3Q(1,:),'linewidth',1)
% hold on
% plot(rad2deg(RK2_Q(1,:)),RK2_R3Q(1,:),'linewidth',1)
% plot(rad2deg(RK4_Q(1,:)),RK4_R3Q(1,:),'linewidth',1)
% plot(rad2deg(Ref_Q(1,:)),Ref_R3Q(1,:),'-*','MarkerIndices',1:100:length(ref_time),'linewidth',1)
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlim([45 600])
% xlabel('\theta^2(deg)')
% ylabel('Position R_x^3(m)')
% 
% subplot(2,2,2)
% plot(rad2deg(Euler_Q(1,:)),Euler_R3Q(2,:),'linewidth',1)
% hold on
% plot(rad2deg(RK2_Q(1,:)),RK2_R3Q(2,:),'linewidth',1)
% plot(rad2deg(RK4_Q(1,:)),RK4_R3Q(2,:),'linewidth',1)
% plot(rad2deg(Ref_Q(1,:)),Ref_R3Q(2,:),'-*','MarkerIndices',1:100:length(ref_time),'linewidth',1)
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlim([45 600])
% xlabel('\theta^2(deg)')
% ylabel('Velocity R_x^3(m/s)')
% 
% subplot(2,2,3)
% plot(rad2deg(Euler_Q(1,:)),Euler_R3Q(3,:),'linewidth',1)
% hold on
% plot(rad2deg(RK2_Q(1,:)),RK2_R3Q(3,:),'linewidth',1)
% plot(rad2deg(RK4_Q(1,:)),RK4_R3Q(3,:),'linewidth',1)
% plot(rad2deg(Ref_Q(1,:)),Ref_R3Q(3,:),'-*','MarkerIndices',1:100:length(ref_time),'linewidth',1)
% legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
% hold off
% grid on
% xlim([45 600])
% xlabel('\theta^2(deg)')
% ylabel('Acceleration R_x^3(m/s^2)')

%% 플롯 시간
sgtitle(['System Dynamics Final Project 2015100767 이현빈: ',num2str(steps),' Steps for ', num2str(endTime),'sec'])
subplot(2,2,1)
plot(time,Euler_R3Q(1,:),'linewidth',1)
hold on
plot(time,RK2_R3Q(1,:),'linewidth',1)
plot(time,RK4_R3Q(1,:),'linewidth',1)
plot(ref_time,Ref_R3Q(1,:),'-*','MarkerIndices',1:200:length(ref_time),'linewidth',1)
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('Time(sec)')
ylabel('Position R_x^3(m)')

subplot(2,2,2)
plot(time,Euler_R3Q(2,:),'linewidth',1)
hold on
plot(time,RK2_R3Q(2,:),'linewidth',1)
plot(time,RK4_R3Q(2,:),'linewidth',1)
plot(ref_time,Ref_R3Q(2,:),'-*','MarkerIndices',1:200:length(ref_time),'linewidth',1)
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('Time(sec)')
ylabel('Velocity R_x^3(m/s)')

subplot(2,2,3)
plot(time,Euler_R3Q(3,:),'linewidth',1)
hold on
plot(time,RK2_R3Q(3,:),'linewidth',1)
plot(time,RK4_R3Q(3,:),'linewidth',1)
plot(ref_time,Ref_R3Q(3,:),'-*','MarkerIndices',1:200:length(ref_time),'linewidth',1)
legend({'Euler','RK2','RK4','Reference'},'Location','southwest','NumColumns',2)
hold off
grid on
xlabel('Time(sec)')
ylabel('Acceleration R_x^3(m/s^2)')

%% 함수 라인
function Moment=M2(t) %외력 모멘트
Moment=100*sin(pi*t/0.1);
end

function d_Y=Grad(t,Y)
global m2 m3 m4 J2 J3 J4 l2 l3 g h
th2=Y(1); th3=Y(2); dth2=Y(3);  dth3=Y(4);

% 계산된 임베디드 식으로부터 ddth2, ddth3 하드코딩함
A=-l2*cos(th2)/(l3*cos(th3));   B=l2*sin(th2)/(l3*cos(th3))*dth2^2+tan(th3)*dth3^2;
ddth2=-(2*g*l2*l3^2*m2*cos(th2) - 4*M2(t)*l3^2*cos(2*th3) - 4*J3*dth2^2*l2^2*sin(2*th2) - 4*J3*dth3^2*l2*l3*sin(th2 + th3) - 4*M2(t)*l3^2 + 2*g*l2*l3^2*m3*cos(th2) + 4*J3*dth3^2*l2*l3*sin(th2 - th3) + dth2^2*l2^2*l3^2*m3*sin(2*th2) + g*l2*l3^2*m2*cos(th2 - 2*th3) + g*l2*l3^2*m2*cos(th2 + 2*th3) + g*l2*l3^2*m3*cos(th2 - 2*th3) + g*l2*l3^2*m3*cos(th2 + 2*th3) + dth3^2*l2*l3^3*m3*sin(th2 + th3) + 2*dth2^2*l2^2*l3^2*m3*sin(2*th2 - 2*th3) + 4*dth2^2*l2^2*l3^2*m4*sin(2*th2 - 2*th3) + 3*dth3^2*l2*l3^3*m3*sin(th2 - th3) + 8*dth3^2*l2*l3^3*m4*sin(th2 - th3))/(4*J2*l3^2 + 4*J3*l2^2 + l2^2*l3^2*m2 + 3*l2^2*l3^2*m3 + 4*l2^2*l3^2*m4 + 4*J3*l2^2*cos(2*th2) + 4*J2*l3^2*cos(2*th3) + l2^2*l3^2*m2*cos(2*th3) - l2^2*l3^2*m3*cos(2*th2) + 2*l2^2*l3^2*m3*cos(2*th3) - 2*l2^2*l3^2*m3*cos(2*th2 - 2*th3) - 4*l2^2*l3^2*m4*cos(2*th2 - 2*th3));
ddth3=A*ddth2+B;

d_Y=[dth2 dth3 ddth2 ddth3]';
end


function Rx_3=RX3(t,Y)
global m2 m3 m4 J2 J3 J4 l2 l3 g
th2=Y(1);   th3=Y(2);   dth2=Y(3);  dth3=Y(4);
dummy=Grad(t,Y);
ddth2=dummy(3);

% 바디3 위치 1번행
Rx3=l2*cos(th2)+l3/2*cos(th3);

% 바디3 속도 2번행
dRx3=-dth2*l2*sin(th2)-dth3*l3/2*sin(th3);

% 바디3 가속도 3번행
A=-l2*cos(th2)/(l3*cos(th3));   B=l2*sin(th2)/(l3*cos(th3))*dth2^2+tan(th3)*dth3^2;

ddRx3=(-l2*sin(th2)-l3/2*sin(th3)*A)*ddth2;
ddRx3=ddRx3+(-l2*cos(th2)*dth2^2-l3/2*cos(th3)*dth3^2-l3/2*sin(th3)*B);

% 위치 속도 가속도 배열 반환
Rx_3=[Rx3 dRx3 ddRx3]';
end



