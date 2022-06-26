from typing import List

'''
Problem:
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Solution: 
- At each level, we calculate the total at each position
- sum at one position is min of that position + above i or i-1
'''
class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		if len(triangle) < 2:
			return triangle[0][0]
		sums = [triangle[0][0]]
		rows = len(triangle)
		for row in range(1, rows):
			sum_row = []
			len_row = len(triangle[row])
			for i in range(0, len_row):
				s1 = sums[i-1] if i > 0 else sums[i]
				s2 = sums[i] if i < len_row-1 else sums[i-1]
				sum_row.append(min(s1, s2) + triangle[row][i])
			sums = sum_row
		return min(sums)
