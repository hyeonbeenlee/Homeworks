format long e,clc
l2=0.3;
l3=0.5;
th2=pi/4;
th3=-0.330234;

dth2=100;
dth3=-44.849;
ddth3=3.656824668557173e+03;





a=inv([1 l3*sin(th3);0 -l3*cos(th3)]);
b=-dth2^2*l2*[cos(th2);sin(th2)];
c=-dth3^2*l3*[cos(th3);sin(th3)];
a*(b+c)