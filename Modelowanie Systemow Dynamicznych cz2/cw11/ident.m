function blad = ident(X0) 
global n 
t = 0:0.001:10;  
a = X0(1); 
b = X0(2); 
theta = X0(3); 
y = zpk([],ones(1,10) * (-5),5^10);
[licz,mian] = pade(theta,n);

A = tf(licz,mian) * tf([0,1], [a,b,1]); 
%---------------------------------------- ------% 
% tutaj kod, który będzie obliczał % 
% odpowiedź skokową obiektu symulowanego % 
% o takiej samej długości jak odpowiedź % 
% obiektu rzeczywistego % 
%---------------------------------------- ------% 
y1 = step(y,t);
y2 = step(A,t);


plot(t,y1,t,y2), drawnow 
title("Porównanie funkcji y z odpowiedzią skokową obiektu inercyjnego II rzędu") 
xlabel("Czas [s]") 
ylabel("Amplituda") 
legend("oryginalna funkcja y 10 stopnia", "odpowiedź układu inercyjnego II rzędu") 
e = y1 - y2;  
blad = sum(e.^2) / length(e); 