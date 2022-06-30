class Solution:
	def reverseBits(self, n: int) -> int:
		r = 0
		t = 32
		while t > 0:
			m = n % 2
			n = n // 2
			t = t - 1
			r = r*2 + m
		return r
