import math

'''
Tips: 
- Think of how number is stored in bit
- The easy way is to divide by 2
- Could we use bit operator to check somehow? pow of 2 suppose to have ony one bit on
'''
class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		if n == 0:
			return False
		if n == 1:
			return True
		while n > 1:
			m = n//2
			if m * 2 != n:
				return False
			n = m
		return True



