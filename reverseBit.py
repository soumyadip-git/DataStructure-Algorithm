"""
Reverse the bits of an 32 bit unsigned integer A.

3 - > 3221225472
000..00011 -> 11000..000
"""

def reverseBit(A):
    ans = 0
    for i in range(31, -1, -1):
        if A & (1<<i):
            tmp = 1<<(31-i)
            ans = ans | tmp
    return ans        

print(reverseBit(3))