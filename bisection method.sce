clc;
//bisection method
deff('y=f(x)','y=x^3-x-1')
a=5;
b=6;
d=0.0001;//for accuracy of root
i=1;
printf('table.\ta\t\tb\t\tc\t\tf(a)\t\tf(b)\t\tf(c)\n');
while abs(a-b)>d
    c=(a+b)/2;
   printf('\t%f\t%f\t%f\t%f\t%f\t%f\n',a,b,c,f(a),f(b),f(c));
    if f(c)*f(a)>0
        a=c;
        else
        b=c;
    end
i=i+1;//to count number of iteration
end
disp('the solution of equation  iteration is',i,c)
