function blad = ident2(X0)
load obiekt;
% global y
t = 0:59;
K = X0(1);
T1 = X0(2);
T2 = X0(3);
theta = X0(4);
A = tf([0,K], [T1 * T2,(T1+ T2),1], 'OutputDelay', theta);
%---------------------------------------- ------%
% tutaj kod, który będzie obliczał %
% odpowiedź skokową obiektu symulowanego %
% o takiej samej długości jak odpowiedź %
% obiektu rzeczywistego %
%---------------------------------------- ------%
yA = step(A,t);
plot(t,y,t,yA), drawnow
title("Porównanie funkcji y z odpowiedzią skokową obiektu inercyjnego II rzędu")
xlabel("Czas [s]")
ylabel("Amplituda")
legend("zanieczyszona funkcja y", "odpowiedź układu inercyjnego II rzędu")
e = y - yA; 
blad = sum(e.^2) / length(e);