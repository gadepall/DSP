%Filter Characteristics
clear;
close;


R = 1e3; %1K ohm resistance
C = 10e-6;%10 uF capacitance

%finding 3 dB bandwidth numerically
sqrt(roots([1  13  46  -1]))/(2*pi*R*C)



