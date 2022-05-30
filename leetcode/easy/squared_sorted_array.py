from typing import List


class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		result = []
		squared_negatives = []
		for num in nums:
			if num < 0:
				squared_negatives.insert(0, num * num)
			elif num >= 0:
				while len(squared_negatives) > 0 and squared_negatives[0] < (num * num):
					result.append(squared_negatives[0])
					del squared_negatives[0]
				result.append(num * num)
		for num in squared_negatives:
			result.append(num)
		return result


def test():
	t = [-4, -1, 0, 3, 10]
	s = Solution()
	r = s.sortedSquares(t)
	print(r)

test()
