#Let's imagine that 'n' people are wearing jerseys with numbers written on their back. We make these 'n' guys stand in a circle.
#I give jersey no. 1 a sword. He kills number jersey 2 and gives the sword to 3. Now 3 kills 4 and gives the sword to 5 
#and the process goes on. Now we need to predict who will be the last man standing?

def bit_not(n):
    return (1 << n.bit_length()) - 1 - n
n=input()
m=bit_not(n)
print(n-m)


