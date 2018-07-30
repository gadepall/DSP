%Filter Characteristics
clear;
close;

flag = 2;

R = 10e3; %1K ohm resistance
C = 10e-6;%10 uF capacitance


%Plotting the filter amplitude response
if flag == 2

f = linspace(-50,50,1e2);
s = j*2*pi*f;
den = polyval([1 -5 6 1],s*C*R);
H = 1./den;

plot(f,abs(H))
grid minor

print -deps -color lpf.eps

end

%finding 3 dB bandwidth numerically
if flag == 2

sqrt(roots([1  13  46  -1]))/(2*pi*R*C)

end


%finding 3 dB bandwidth theoretically
if flag == 2

q = -31/3;
r = -1015/27;

sqrt((-r/2 + sqrt(r^2/4 +q^3/27))^(1/3) + (-r/2 - sqrt(r^2/4 +q^3/27))^(1/3) - 13/3)/(2*pi*R*C)

end
