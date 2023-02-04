%% Settings
clc,clear all,format compact
syms th1 th2 th3 x y z real;
%syms L1 L2 L3 real;
L1=4; L2=3; L3=2;
digits(5);  

%% Get input and check
T_0H=Subspace(9,0,0);
% T_0H=Subspace(7.5373,3.9266,deg2rad(60));
% T_0H=[0 1 0 -3;-1 0 0 2;0 0 1 0;0 0 0 1];
% T_0H=Subspace(-3.1245,9.1674,deg2rad(-30));


T_03=T_0H*inv(Translate(L3,0,0)); %변환한다

% Define Phi X Y
x=T_03(1,4); y=T_03(2,4); phi=atan(T_03(2,1)/T_03(1,1));

% Check if goal is origin
if x==y && x==0
    isOrigin=true;
else
    isOrigin=false;
end

%% Calculate Theta2
% Arctangent의 정의역 -pi/2,pi/2 내에서 해를 찾기 때문에 2,3사분면상의 theta1를 찾지 못함
cos_th2=(x^2+y^2-L1^2-L2^2)/(2*L1*L2);

%Case 1
sin_th2_1=sqrt(1-cos_th2^2);
th2_1=atan2(sin_th2_1,cos_th2);

%Case 2
sin_th2_2=-sqrt(1-cos_th2^2);
th2_2=atan2(sin_th2_2,cos_th2);


if sin_th2_1==sin_th2_2 %단일 해 가짐
    isMultiSol=false;
else
    isMultiSol=true; %2개 해 가짐
end

%% Calculate Theta1
if isOrigin
    maxrad=pi;
    minrad=0;
    th1_1=(maxrad-minrad)*rand+minrad;
end


%Case 1
k1_1=L1+L2*cos(th2_1);
k2_1=L2*sin(th2_1);
gamma_1=atan2(k2_1,k1_1);
th1_1=atan2(y,x)-gamma_1;

%Case 2
k1_2=L1+L2*cos(th2_2);
k2_2=L2*sin(th2_2);
gamma_2=atan2(k2_2,k1_2);
th1_2=atan2(y,x)-gamma_2;

%% Calculate Theta3
%Case 1
th3_1=phi-th1_1-th2_1;
%Case 2
th3_2=phi-th1_2-th2_2;

%% Print
if isOrigin
    disp('Theta 1 is arbitrary. Random radian in [0,pi] will be printed.')
else
    disp('Nonarbitrary theta 1 is determined.')
end

if isMultiSol
    disp('Multiple solution found.')
else
    disp('Single solution found.')
end

fprintf('\nIn radian unit\n')
fprintf('%.4f %.4f %.4f\n',vpa([th1_1 th2_1 th3_1]),vpa([th1_2 th2_2 th3_2]))
fprintf('\nIn degree unit\n')
fprintf('%.2f %.2f %.2f\n',vpa(rad2deg([th1_1 th2_1 th3_1])),vpa(rad2deg([th1_2 th2_2 th3_2])))
fprintf('\n')

%% Validation
ValidCalc=Link(0,0,0,th1_1)*Link(L1,0,0,th2_1)*Link(L2,0,0,th3_1)*Translate(L3,0,0)
T_0H
Difference=abs(ValidCalc-T_0H)



%% Functions
%% Link Transformation
% T^(i-1)_(i)=Link(a_(i-1),alpha_(i-1),d_i,theta_i)
function Transform=Link(a,alpha,d,th)
Transform=zeros(4,4);
Transform(4,4)=1;
Transform(1,:)=[cos(th) -sin(th) 0 a];
Transform(2,:)=[sin(th)*cos(alpha) cos(th)*cos(alpha) -sin(alpha) -sin(alpha)*d];
Transform(3,:)=[sin(th)*sin(alpha) cos(th)*sin(alpha) cos(alpha) cos(alpha)*d];
end
%% Translation Transformation
function Transform=Translate(x,y,z)
Transform=zeros(4,4);
Transform(1:3,1:3)=eye(3);
Transform(4,4)=1;
Transform(1:3,4)=[x y z]';
end
%% Subspace Transformation
function Transform=Subspace(x,y,th)
Transform=zeros(4,4); Transform(4,4)=1;
Transform(1:3,1:3)=rotz(th);
Transform(1:2,4)=[x y]';
end
