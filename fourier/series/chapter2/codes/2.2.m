%Filter Characteristics
clear;
close;


R = 1e3; %10K ohm resistance
C = 10e-6;%10 uF capacitance


%Plotting the filter amplitude response

f = linspace(-20,20,1e2);
s = j*2*pi*f;
den = polyval([1 -5 6 1],s*C*R);
H = 1./den;

plot(f,abs(H),"Linewidth",4)
grid minor
xlabel('f')
ylabel('H(f)')

print -deps -color ../figs/2.2.eps



