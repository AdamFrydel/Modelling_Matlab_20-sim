function blad = ident(X0)
load obiekt;
% global y
t = 0:59;
K = X0(1);
T = X0(2);
n = X0(3);
A = tf([0,K], [T,1], 'OutputDelay', n);
%---------------------------------------- ------%
% tutaj kod, który będzie obliczał %
% odpowiedź skokową obiektu symulowanego %
% o takiej samej długości jak odpowiedź %
% obiektu rzeczywistego %
%---------------------------------------- ------%
yA = step(A,t);
plot(t,y,t,yA), drawnow
title("Porównanie funkcji y z odpowiedzią skokową obiektu inercyjnego I rzędu")
xlabel("Czas [s]")
ylabel("Amplituda")
legend("zanieczyszona funkcja y", "odpowiedź układu inercyjnego I rzędu")
e = y - yA; 
blad = sum(e.^2) / length(e);