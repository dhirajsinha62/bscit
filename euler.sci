clc;
//euler
function[y0]=euler(x0,y0,h,yest,f)
    //x0,y0,h have usual meaning and yest is value for which y is to be obtained.
    n=(yest-x0)/h 
    for i=1:n
        y0=y0+f(x0,y0)*h;
        x0=x0+h;
        disp(y0)
    end;
endfunction
deff('[y]=f(a,b)','y=b-a*b+a');
p=euler(0,1,0.2,1,f)
disp(p,'answar')
