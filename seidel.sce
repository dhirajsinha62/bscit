clc;
function[X]=gaussseidel(A,n,N,X,b)
  L=A;
  U=A;
D=A;
    for i=1:1:n
        for j=1:1:n
            if j>i then L(i,j)=0;
                D(i,j)=0;
            end
            if i>j  then U(i,j)=0;
           D(i,j);
end
if i==j then L(i,j)=0;
    U(i,j)=0;
end
    end
end
for k=1:1:N
      X=(D+L)^-1*(-U*X+b);
     disp(X)
end
endfunction
A=[2 -1 0;-1 2 -1;0 -1 2]
b=[7;1;1]
  N=3;    // nbo.of iterations
  n=3;    // order of the matrix is n*n
  X=[0;0;0]      //intial approximation
p=gaussseidel(A,n,N,X,b)    //call the function which performs gauss seidal method to solve the system
disp('answer',p);
