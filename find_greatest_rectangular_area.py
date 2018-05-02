#find the greatest rectangular area formed by consecutive square buildings

#The first line contains N, the number of buildings altogether. The second line contains space-separated integers, each representing the height of a building.
# input
#5
#1 2 3 4 5
# output
#9

def largestRectangleArea(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  

    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans
a=input()
l=[int(x) for x in raw_input().split()]
print(largestRectangleArea(l))
