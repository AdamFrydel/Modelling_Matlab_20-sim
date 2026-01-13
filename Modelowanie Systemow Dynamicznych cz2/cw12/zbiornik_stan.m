function dx = zbiornik_stan(t,x,wi,w,Ti,Q)
% Argumenty wejściowe:
% t - czas
% x - wektor stanu układu
% wi - dopływ
% w - wypływ
% Ti - temperatura cieczy dopływającej
% Q - moc dostarczana (grzanie)
%----------------------------- zmienne stanu ------------------------------
x1 = x(1); % objętość
x2 = x(2); % temperatura
%------------------------------- parametry --------------------------------
C = 4200; % ciepło właściwe [J/(Kg*K)]
ro = 1000; % gęstość [kg/m3]
%%---------------------------- równania stanu -----------------------------
dx1 = 1 / ro * (wi-w);
dx2 = wi * (Ti - x2) / (ro * x1) + Q / (ro * x1 * C);
dx = [dx1;dx2]; % pochodne stanu