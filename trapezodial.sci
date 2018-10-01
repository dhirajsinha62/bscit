clc;
function[i]=trapezodial(a,b,n,f)
h=(b-a)/n;
x=(a:h:b);
y=f(x);
m=length(y);
i=y(1)+y(m);
for j=2:m-1
    i=i+2*y(j);
end;
i=(h/2)*i;
return(i);
endfunction
deff('[y]=f(x)','y=exp(x)')
p=trapezodial(0,1,4,f)
disp(p,'answer')
