clc;
//Mathematical induction
U1=1; // given 
U2=5; // given 
P=[]; 
for i=1:2 
P(i)=3^i-2^i; 
disp(P(i)) 
end 
disp( 'P(1)=U(1) and P(2)=U(2) ');
disp( 'hence Un=3ˆn−2ˆn for a l l n belonging to N/');
