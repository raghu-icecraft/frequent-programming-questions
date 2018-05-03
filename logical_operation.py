# To find common elements from two large arrays
l=[int(x) for x in raw_input().split()]
m=[int(y) for y in raw_input().split()]
z=list(set(l) & set(m))
print(z)

# To find non common elements from two large arrays

l1=[int(x) for x in raw_input().split()]
m1=[int(y) for y in raw_input().split()]
z1=list(set(l1) ^ set(m1))
print(z1)

# adding list eliminating the common elements
l2=[int(x) for x in raw_input().split()]
m2=[int(y) for y in raw_input().split()]
z2=list(set(l2) | set(m2))
print(z2)
