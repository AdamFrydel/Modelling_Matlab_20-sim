function blad = ident1(X0)
load obiekt;
% global y
global n
t = 0:59;
K = X0(1);
T = X0(2);


[licz1,mian1] = zp2tf([], -1/T * ones(1,n),K/(T^n));
A = tf(licz1,mian1);

%---------------------------------------- ------%
% tutaj kod, który będzie obliczał %
% odpowiedź skokową obiektu symulowanego %
% o takiej samej długości jak odpowiedź %
% obiektu rzeczywistego %
%---------------------------------------- ------%
yA = step(A,t);
plot(t,y,t,yA), drawnow
e = y - yA; 
blad = sum(e.^2) / length(e);