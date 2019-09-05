%% theoratical calculation
% assume a leftwards L matching network
R = 2.9;
X = 26.3;
f = 5e+8;
Z = 50;
X2(1) = (Z*X + (Z*R^3 - Z^2*R^2 +Z*R*X^2)^(1/2))/(R - Z);
X2(2) = (Z*X - (Z*R^3 - Z^2*R^2 +Z*R*X^2)^(1/2))/(R - Z);
X1(1) = -(R^2*X2(1)+X^2*X2(1)+X*X2(1)^2)/(R^2+(X+X2(1))^2);
X1(2) = -(R^2*X2(2)+X^2*X2(2)+X*X2(2)^2)/(R^2+(X+X2(2))^2);
X1;
X2;
1./(1./(X2.*1j)+1/(R+X*1j))+X1.*1j

disp('solution 1')
if X1(1)>0
    L1_1 = X1(1)/(2*pi*f);
    L1 = L1_1
else
    C1_1 = -1/(2*pi*f*X1(1));
    C1 = C1_1
end
if X2(1)>0
    L2_1 = X2(1)/(2*pi*f);
    L2 = L2_1
else
    C2_1 = -1/(2*pi*f*X2(1));
    C2 = C2_1
end

disp('solution 2')
if X1(2)>0
    L1_2 = X1(2)/(2*pi*f);
    L1 = L1_2
else
    C1_2 = -1/(2*pi*f*X1(2));
    C1 = C1_2
end
if X2(2)>0
    L2_2 = X2(2)/(2*pi*f);
    L2 = L2_2
else
    C2_2 = -1/(2*pi*f*X2(2));
    C2 = C2_2
end

%% actual value
C1_act = 2.45e-12;
C2_act = 7.5e-12;
X1_act = -1/(2*pi*f*C1_act);
X2_act = -1/(2*pi*f*C2_act);
1./(1./(X2_act.*1j)+1/(R+X*1j))+X1_act.*1j