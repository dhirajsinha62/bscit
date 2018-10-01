clc;
//Cardinality
x=1;
y=2; 
z=3;
A=[x,y,z];
a=length(A);
disp(a,'cardinality of set A is : ') 
B=[1,3,5,7,9] 
b=length(B) ;
disp(b,' cardinality of set B is :') 
// 3.9 (b) 
disp( 'the set E has the following elements ') 
E=[2 ,4 ,6 %inf ] // set E is the set of a l l positive even numbers and N is the set of a l l natural numbers 
disp ( ' function f:N to E is defined.So,E has the same cardinality as N')
disp(E, ' set E is countably i n f i n i t e : ') 
for x=2:2:%inf 
y=2*x; 
disp(y) 
end
