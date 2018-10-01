clc;
//false position method
deff('y=f(x)','y=x^3+2*x-1')
a=0;
b=1;
d=0.01;//for accuracy of root
i=1;
printf('table     .\ta\t\tb\t\tc\t\tf(a)\t\tf(b)\t\tf(c)\n');
while abs(a-b)>d
    c=(a*f(b)-b*f(a))/(f(b)-f(a));
   printf('         \t%f\t%f\t%f\t%f\t%f\t%f\n',a,b,c,f(a),f(b),f(c));
    if f(c)*f(a)>0
        a=c;
        else
        b=c;
    end
i=i+1;//to count number of iteration
end
disp('the solution of equation after %i iteration is%g',i,c)
