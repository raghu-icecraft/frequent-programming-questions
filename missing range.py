l=[int(x) for x in raw_input().split()]
l.sort()
m=[]
for i in range(len(l)-1):
	if(l[i+1]-l[i]!=1):
		if(l[i+1]-1!=l[i]+1):
			m.append(str(l[i]+1)+'->'+str(l[i+1]-1))
		else:
			m.append(str(l[i]+1))
print(m)
# Input: [0,1,3,49,50,52,75]
#Output : ['2', '4->48', '51', '53->74']
