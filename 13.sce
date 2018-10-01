clc;
// Permutations
disp( ' finding the number of three−l e t t e r words using only the given six l e t t e r s (A,B,C,D,E,F) without repetition ') 
n=6; // total number of l e t t e r s 
l1=n; //number of ways in which f i r s t l e t t e r of the word can be chosen 
l2=n-1; //number of ways in which second l e t t e r of the word can be chosen
l3= n-2; //number of ways in which third l e t t e r can be chosen
k=l1*l2*l3;
disp(k, 'number of three−l e t t e r words possible ')
