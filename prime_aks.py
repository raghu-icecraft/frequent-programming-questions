"""
AKS primality test (also known as Agrawal-Kayal-Saxena primality test and cyclotomic AKS test)
Referred from https://en.wikipedia.org/wiki/AKS_primality_test
TODO: Add the Time complexity of AKS

To Execute: python prime_aks.py
Sample Output (when n=1000):

Prime numbers from 2 to 1000 are ...

 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269
271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587
593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919
929 937 941 947 953 967 971 977 983 991 997
"""


def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n==3:
        return True
    if (n % 2 == 0) or (n % 3 ==0):
        return False

    i = 5
    w = 2

    # reducing remainder check comparisons to almost square root of n
    # At each step i will be like 5, 7, 11, 13, 17, 19, 23, 25, 29 .....
    while i * i <= n:
        if n % i == 0:
            return False
 
        i += w
        w = 6 - w
 
    return True


# Initialize 'n' here or use raw_input to get from terminal as standard input
a = ""   # to print the output
n = 1000
print "Prime numbers from 2 to %d are ...\n"%n
# 1 is neither prime nor composite
for i in range(2, n):
    if isprime(i):
        a = a + " " + str(i)
print a
