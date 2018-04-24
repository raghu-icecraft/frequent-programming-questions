#SAMPLE INPUT 
#8
#-1 -4  4 -2 0 1 4 -5
#SAMPLE OUTPUT 
#7
sum([4 -2 0 1 4])=7
a=int(input())
if(a==0):
	print("0")
else:
	l = [int(x) for x in raw_input().split()]
	s=0
	l1=[]
	for i in range(0,len(l)):
		s+=l[i]
		if(s<0):
			s=0
		l1.append(s)
	print(max(l1))
  
  
