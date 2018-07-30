clear;
close;
clc;


%Square wave 
A = 5;
T = 0.02;


t = linspace(-2.5*T,2.5*T,1e4);
s = A/2*(1+square(2*pi*t/T));
plot(t,s,"Linewidth",4)
grid
axis([-0.06,0.06,-1,6])
xlabel('t')
ylabel('g(t)')

print -deps -color ../figs/1.1.eps

