"""
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def trap(self, A):
	n = len(A)
    	PM = [0 for i in A]
    	PM[0] = A[0]
    	for i in range(1, n):
            PM[i] = max(PM[i-1], A[i])

    	SM = [0 for i in A]
    	SM[n-1] = A[n-1]
    	for i in range(n-2, -1, -1):
            SM[i] = max(SM[i+1], A[i])

    	s = 0
    	for i in range(1, n-1):
            s += max(min(PM[i-1], SM[i+1]) - A[i], 0) 
    	return s    
