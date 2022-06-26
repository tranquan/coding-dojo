from re import L
from typing import List

'''
Problem:
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Solution:
- Start from cell which value is 0, expand to neighbor cells
- Cells will be visit in order: 0, 1, 2, etc tp make sure the distance is smallest

Pattern:
BFS with special initial conditions: start from vertices is 0
'''
class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		rows = len(mat)
		cols = len(mat[0])
		queue = []
		visited = dict()
		setted = dict()
		
		for i in range(len(mat)):
			for j in range(len(mat[i])):
				if mat[i][j] == 0:
					queue.insert(0, [i, j])
					setted[f"{i}_{j}"]= True

		while len(queue) > 0:
			c = queue.pop()
			if f"{c[0]}_{c[1]}" in visited:
				continue
			visited[f"{c[0]}_{c[1]}"] = True

			i, j = c[0], c[1]
			adj = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
			
			for cell in adj:
				if not (cell[0] >= 0 and cell[0] < rows and cell[1] >= 0 and cell[1] < cols): 
					continue
				key = f"{cell[0]}_{cell[1]}"
				if key not in setted:
					mat[cell[0]][cell[1]] = mat[c[0]][c[1]] + 1
					setted[key] = True
					if key not in visited:
						queue.insert(0, cell)
		return mat


class TestCase:
	input: List[List[int]]
	expected: List[List[int]]

	def __init__(self, input: List[List[int]], expected: List[int]) -> None:
		self.input = input
		self.expected = expected

	def compareMatrix(self, m1: List[List[int]], m2: List[List[int]]):
		for i in range(len(m1)):
			for j in range(len(m1[i])):
				if m1[i][j] != m2[i][j]:
					return False
		return True


TESTCASES: List[TestCase] = [
	TestCase([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
	TestCase([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.updateMatrix(case.input)
		if case.compareMatrix(case.expected, r):
			print(f"passed")
		else:
			print(f"failed {case.input}, {r} != {case.expected}")

test()
