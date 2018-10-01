clc;
// a scilab to fit poisson distribution for given data
function[expfre]=poissonfit(x,obsfre)
 n=length(x)-1;
 N=sum(obsfre);
 xbar=x*obsfre'/N;
 m=xbar;
 prob(1)=exp(-m);
 for i=1:n
     prob(i+1)=m*prob(i)/(i);
  end
  expfre=round(prob*N);
  disp("expected frequency:");
  return(expfre);
endfunction;
x=[0,1,2,3,4,5];
obsfre=[100,70,45,20,10,5];
z=poissonfit(x,obsfre)
disp(z,"answer");
