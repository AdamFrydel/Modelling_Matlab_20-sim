licz  = [0 0 1];
mian = [1000 500 400];
syms s;
M = 1000;
alfa = 500;
c = 400;

wspTlum = [0.1 4]
% odp na zadanie 1 a) bieguny nie są rzeczywiste
% odp na zadanie 1 b) układ jest stabilny gdyż wpółczynniki stojące przy
% części rzeczywistej pierwiastków są ujemne,
[z,p,k] = tf2zp(licz,mian)
faktoryzacja = k * prod(s - z) / prod(s - p)
standard = @(c,alfa,M)  (1/c) ./ ((M/c)*s^2 + (alfa./c) * s + 1)

%nowa alfa
alfa1 = wspTlum(1,1) * 2 * sqrt(M * c);
alfa2 = wspTlum(1,2) * 2 * sqrt(M * c);

%transmitancje
transmitancja1 = standard(c, alfa1, M); % układ oscylacyjny
transmitancja2 = standard(c, alfa2, M); % układ tłumiony

display(transmitancja1);
display(transmitancja2);

licz12 = [0 0 1];
mian1 = [M, alfa1, c]; 
mian2 = [M, alfa2, c]; 
oscylacje = tf(licz12, mian1)
tlumienie = tf(licz12, mian2)
step(oscylacje, tlumienie)
legend('oscylacje', 'tlumienie', Location='POLSKA')

