#Sample Input
#"Hey, do you even code?", said Rahul.
#Sample Output
#A : 2
#C : 1
#D : 3
#E : 4
#H : 2
#I : 1
#L : 1
#N : 1
#O : 3
#R : 1
#S : 1
#U : 2
#V : 1
#Y : 2

#---------------------------Python Code ------------------------------#
import sys
a=sys.stdin.read()
c=a.lower()
b='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
	s=""
	if(c.count(b[i])>0):
		s+=b[i].upper()+" "+":"+" "+str(c.count(b[i]))
		print(s)
