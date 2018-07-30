%Filter output

clear;
close;

R = 1e3; %10 k resistance
C = 10e-6;%10 uF capacitance
T=0.02;
f = 1/T;


for n = 0:20,

		s = j*2*pi*n*f;
		den = polyval([1 -5 6 1],s*C*R);
		H(n+1) = 1./den; %Frequency response

end

stem(0:20,abs(H),"Linewidth",4)
xlabel('n')
ylabel('H(nf)')
grid 

print -deps -color ../figs/2.6.eps

