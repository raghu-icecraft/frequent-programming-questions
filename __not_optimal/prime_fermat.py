"""
    Print prime numbers for a given range.
    If input is n, print prime numbers from 2 upto n, where n >= 2
    Time Complexity (Big O): (TODO) n * complexity of 2^n
    (TODO) At this point code is not displaying required prime numbers completely
"""

# Fermat Theorem
def isPrime(n):

    if n == 2:
        return True

    if not n & 1:
        return False

    return pow(2, n-1, n) == 1


n = int(raw_input("Enter a number to display prime number range : "))

for i in range(2, n+1):
    if isPrime(i):
        print i,
