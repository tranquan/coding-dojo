from re import L
from typing import List

'''
Problem:
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Solution:
- Because it ask for minimum, we need to start from all rotten orange first
- We stop when there's no new rotten is create

'''
class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		times = 0
		queue = []

		for i in range(0, rows):
			for j in range(0, cols):
				if grid[i][j] == 2:
					queue.insert(0, [i, j])

		while True:
			new_rotten = False
			next_queue = []
			while len(queue) > 0:
				cell = queue.pop()
				i, j = cell[0], cell[1]
				adj = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
				for c in adj:
					if c[0] >= 0 and c[0] < rows and c[1] >= 0 and c[1] < cols:
						if grid[c[0]][c[1]] == 1:
							new_rotten = True
							grid[c[0]][c[1]] = 2
							next_queue.insert(0, [c[0], c[1]])
			if not new_rotten:
				break
			times += 1
			queue.extend(next_queue)

		for i in range(0, rows):
			for j in range(0, cols):
				if grid[i][j] == 1:
					return -1

		return times


class TestCase:
	input: List[List[int]]
	expected: List[List[int]]

	def __init__(self, input: List[List[int]], expected: List[int]) -> None:
		self.input = input
		self.expected = expected

	def compareMatrix(self, m1: List[List[int]], m2: List[List[int]]):
		for i in range(0, len(m1)):
			for j in range(0, len(m1[i])):
				if m1[i][j] != m2[i][j]:
					return False
		return True


TESTCASES: List[TestCase] = [
	TestCase([[2,1,1],[1,1,0],[0,1,1]], 4),
	TestCase([[2,1,1],[0,1,1],[1,0,1]], -1),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.orangesRotting(case.input)
		if case.expected == r:
			print(f"passed")
		else:
			print(f"failed {case.input}, {r} != {case.expected}")

test()
