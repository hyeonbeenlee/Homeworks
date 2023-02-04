%% Setting
clc,clear all;
L1=4; L2=3; L3=2;

%% Make robot object
% DH Table이 기준이 아닌, 링크를 기준으로 대입한다
% 각 링크의 길이, 낮은번호 조인트 변수들 입력한다
link1=Link('a',L1,'alpha',0,'d',0);
link2=Link('a',L2,'alpha',0,'d',0);
link3=Link('a',L3,'alpha',0,'d',0);
Robot=SerialLink([link1 link2 link3],'name','HW3 3R Manipulator')

%% Inputs
%Robot.fkine(deg2rad([0 0 0]))
T0H_1=Subspace(9,0,0);

%Robot.fkine(deg2rad([10 20 30])) or Robot.fkine(deg2rad([27.1 -20 52.9]))
T0H_2=Subspace(7.5373,3.9266,deg2rad(60));

%Robot.fkine(deg2rad([90 90 90])) or Robot.fkine(deg2rad([163.7 -90 -163.7]))
T0H_3=[0 1 0 -3;-1 0 0 2;0 0 1 0;0 0 0 1];

%Out of ROM
T0H_4=Subspace(-3.1245,9.1674,deg2rad(-30));

%% Case i
% Robot.ikine(T0H변환행렬, 뉴턴랩슨 초기예측값(deg), 마스크벡터 x y z rx ry rz)
qi_1=Robot.ikine(T0H_1,'q0',[0.1 0.1 0.1],'mask',[1 1 0 0 0 1]);
qi_1=rad2deg(qi_1);

%% Case ii
% Robot.ikine(T0H변환행렬, 뉴턴랩슨 초기예측값(deg), 마스크벡터 x y z rx ry rz)
% Solution 1
qi_2_1=Robot.ikine(T0H_2,'q0',[8 19 28],'mask',[1 1 0 0 0 1]);
qi_2_1=rad2deg(qi_2_1);

% Solution 2
qi_2_2=Robot.ikine(T0H_2,'q0',[25 -18 60],'mask',[1 1 0 0 0 1]);
qi_2_2=rad2deg(qi_2_2);

%% Case iii
% Robot.ikine(T0H변환행렬, 뉴턴랩슨 초기예측값(deg), 마스크벡터 x y z rx ry rz)
% Solution 1
qi_3_1=Robot.ikine(T0H_3,'q0',[88 92 87],'mask',[1 1 0 0 0 1]);
qi_3_1=rad2deg(qi_3_1);

% Solution 2
qi_3_2=Robot.ikine(T0H_3,'q0',[163 -89 -163],'mask',[1 1 0 0 0 1]);
qi_3_2=rad2deg(qi_3_2);

%% Case iv
% Robot.ikine(T0H변환행렬, 뉴턴랩슨 초기예측값(deg), 마스크벡터 x y z rx ry rz)
% Solution 1
qi_4=Robot.ikine(T0H_4,'q0',[0 0 0],'mask',[1 1 0 0 0 1]);
qi_4=rad2deg(qi_4);

%% Print
fprintf('For case i:\n')
fprintf('[%.2f %.2f %.2f]\n',qi_1)
fprintf('\nFor case ii:\n')
fprintf('[%.2f %.2f %.2f]\n',qi_2_1,qi_2_2)
fprintf('\nFor case iii:\n')
fprintf('[%.2f %.2f %.2f]\n',qi_3_1,qi_3_2)
fprintf('\nFor case iv:\n')
fprintf('[%d]\n',qi_4)

%% Functions
%% Link Transformation
% T^(i-1)_(i)=Link(a_(i-1),alpha_(i-1),d_i,theta_i)
function Transform=LinkT(a,alpha,d,th)
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
