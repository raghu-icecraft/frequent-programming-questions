def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
 
    i = 5
    w = 2
 
    while i * i <= n:
        if n % i == 0:
            return False
 
        i += w
        w = 6 - w
 
    return True
a=""
n=1000000
for i in range(2, n):
    if isprime(i):
        a = a + " " + str(i)
print a
