%Filter output

clear;
close;

R = 1e3; %10 k resistance
C = 10e-6;%10 uF capacitance
T_0 = 0.01;
T = 0.02; 
f = 1/T;
A = 5; %input amplitude
simlen = 1e3; %time range

t = linspace(0,0.1,simlen); %generating points in t-axis
n = 1:15; %series range

for n = 0:20,
	if n == 0,
		g = A*T_0/T;
	else
		an = 2*A*sin(2*pi*n*f*T_0)./(2*pi*n*f*T); %Computing coefficients
		bn = 2*A*(1 - cos(2*pi*n*f*T_0))./(2*pi*n*f*T); %Computing coefficients
		s = j*2*pi*n*f;
		den = polyval([1 -5 6 1],s*C*R);
		Hn = 1./den; %Frequency response
		thetan = arg(Hn);


		
		cost = cos(2*pi*n*f*t + thetan);%Computing cosine term
		sint = sin(2*pi*n*f*t+ thetan);%Computing sine term


		g = g + abs(Hn)*an*cost + abs(Hn)*bn*sint; %evaluating the summation
	end
end

plot(t,g,"Linewidth",4)
grid 

print -deps -color ../figs/2.5.eps

