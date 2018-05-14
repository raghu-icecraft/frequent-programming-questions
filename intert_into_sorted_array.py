#Adding element in a sorted array keeping array sorted

import bisect 
a = [1,3,5,7,9] 
bisect.insort(a, 8)
bisect.insort(a, 2)
bisect.insort(a, 6)
print(a)

#Output: [1, 2, 3, 5, 6, 7, 8, 9]
