# Trapping Rain Water
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

A=[int[x] for x in raw_input().split()]
if not A:
  print(0)
highestLeftSoFar=[]
highestRightSoFar=[]
for i in range(len(A)):
  highestLeftSoFar.append(A[i] if i==0 else max(A[i], highestLeftSoFar[-1]))
for i in range(len(A)-1, -1, -1):
  highestRightSoFar.insert(0,A[i] if i==len(A)-1 else max(A[i], highestRightSoFar[0]))
totalVolume=0;
for i, currentHeight in enumerate(A):
  minSideHeight=min(highestLeftSoFar[i], highestRightSoFar[i])
  if minSideHeight>currentHeight:
    totalVolume+=(minSideHeight-currentHeight)*1
                
print(totalVolume)
