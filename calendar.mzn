%include "global.mzn";

int: S ;


array[1..S-1, 1..S div(2), 1..2] of var 1..S: calendario;

constraint forall(g in 1..S-1)(forall(i,j in 1..S div(2) where i!= j)(forall(k in 1..2)(calendario[g,i,k]!=calendario[g,j,k])));
constraint forall(g in 1..S-1)(forall(i,j in 1..S div(2))(calendario[g,i,1]!=calendario[g,j,2]));


constraint forall(g in 1..S-1)(forall(h in g..S-1 where h!=g)(forall(i in 1..S div(2))(forall(j in 1..S div(2))(forall(k in 1..2 where calendario[g,i,1]==calendario[h,j,k])(calendario[g,i,2]!=calendario[h,j,2div(k)])))));

%constraint forall(s in 1..S)(forall(g in 1..S-1)(forall(h in g..S-1 where h!=g)(forall(i in 1..S div(2) where calendario[g,i,1]==s \/ calendario[g,i,2]==s)(forall(j in 1..S div(2) where calendario[h,j,1]==s \/ calendario[h,j,2]==s)(calendario[h,j,1]+calendario[h,j,2] != calendario[g,i,1]+calendario[g,i,2])))));



function var int: counter(int: s) =  sum ([ 1 | g in 2..S-1,i,j in 1..S div(2) where calendario[g,i,1]==calendario[g-1,j,1] /\ calendario[g,i,1]== s]);
%function var int: countert(int: s) =  sum ([ 1 | g in 2..S-1,i,j in 1..S div(2) where calendario[g,i,2]==calendario[g-1,j,2] /\ calendario[g,i,2]== s]);


%solve ::restart_linear(1000) minimize sum(s in 1..S)(counter(s));
solve satisfy;


   
       