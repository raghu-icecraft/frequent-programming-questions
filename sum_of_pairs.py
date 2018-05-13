#Find pairs which sum up to a particular number.
#Given a integer n.
#Given a list containing various interger values.
#Print total pairs from the list whose sum equals integer n.
# Solution
l = [1,2,4,6,3,10,7,5]
d = {}
n = 9
for i in l:
    if d.has_key(i):
        print i, d[i]
    key = n - i
    d[key] = i
    
#Output:  (3 6) (7 2) (5 4)

