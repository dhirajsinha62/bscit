clc;
x=[1,2,3,4,5,6,7]
y=[0.5,2.5,2,4,3.5,6,5.5];
n=7;
s=0;
xsq=0;
xsum=0;
ysum=0;
for i=1:7
s=s+((x(1,i)))*((y(1,i)));
xsq=xsq+((x(1,i)))^2;
xsum=xsum+(x(1,i));
ysum=ysum+(y(1,i));
end
disp(s,"sum of product ofx and y=")
disp(xsq,"sum of square of x=")
disp(xsum,"sum of all the x=")
disp(ysum,"sum of all the y=")
a=xsum/n;
b=ysum/n;
byx=(n*s-xsum*ysum)/(n*xsq-xsum^2);
disp(byx,"regression coefficient of y on x=")
x1=4;
y1=byx*(x1-a)+b;
disp(y1,x=x1,"the expected value of y when x is: ")
