"""
Desc: given a even number A. Print 2 prime numbers such that sum of those 2 prime numbers = A
If multiple solutions are possible such that (a,b) & (c,d) print (a,b) if a < c and b < d

"""

import math
def isPrime(A):
    if A == 1:
        return False
    for i in range(2, int(math.sqrt(A))+1):
        if A%i == 0:
            return False
    return True

def main(A):
    a = 10**7
    b = 10**7
    for i in range(2, int(math.sqrt(A))+1):
        if isPrime(i):
            j = A - i
            if isPrime(j):
                if i < a and j < b:
                    a = i
                    b = j
    return (a,b)            
            
main(1024) 
# Output: (3, 1021)
    
