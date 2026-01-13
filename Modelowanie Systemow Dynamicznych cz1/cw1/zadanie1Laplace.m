function zadanie1Laplace(a)
    syms t s

    f = heaviside(t - a);
    
    Fs = laplace(f, t, s)    
    figure; 
    ezplot(f, [0, 5]); 
    title(['Funkcja Heaviside']);
    xlabel('t');
    ylabel('f(t)');
    grid on;
    
    figure; 
    ezplot(Fs, [0, 5]); 
    title(['Transformata Laplace']);
    xlabel('s');
    ylabel('F(s)');
    grid on;
