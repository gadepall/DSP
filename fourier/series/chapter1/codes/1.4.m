%Filter input: Square Wave and Fourier series

clear;
close;

T_0 = 0.01;
T = 0.02;
f = 1/T;
A = 5;
simlen = 1e3;

t = linspace(0,0.1,simlen); %generating points in t-axis
n = 1:15; %series range

%g = zeros(1,1e2);%initialising sum

for n = 0:20,
	if n == 0,
		g = A*T_0/T;
	else
		cost = cos(2*pi*n*f*t);%Computing cosine term
		sint = sin(2*pi*n*f*t);%Computing sine term

		an = 2*A*sin(2*pi*n*f*T_0)./(2*pi*n*f*T); %Computing coefficients
		bn = 2*A*(1 - cos(2*pi*n*f*T_0))./(2*pi*n*f*T); %Computing coefficients
		g = g + an*cost + bn*sint; %evaluating the summation
	end
end

plot(t,g,"Linewidth",4)
grid 
xlabel('t')
ylabel('g(t)')

print -deps -color ../figs/1.4.eps



