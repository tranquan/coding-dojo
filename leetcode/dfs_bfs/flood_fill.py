from cmath import exp
from typing import List


class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
		if len(image) == 0:
			return image
		len_r = len(image)
		len_c = len(image[0])
		start_color = image[sr][sc]
		visited = {}
		next = [sc, sr]
		while len(next) > 0:
			r = next.pop()
			c = next.pop()
			key = f"{r}_{c}"
			if key in visited:
				continue
			visited[key] = True
			image[r][c] = color
			if r-1 >= 0 and image[r-1][c] == start_color:
				next.insert(0, r-1)
				next.insert(0, c)
			if r+1 < len_r and image[r+1][c] == start_color:
				next.insert(0, r+1)
				next.insert(0, c)	
			if c-1 >= 0 and image[r][c-1] == start_color:
				next.insert(0, r)
				next.insert(0, c-1)
			if c+1 < len_c and image[r][c+1] == start_color:
				next.insert(0, r)
				next.insert(0, c+1)
		return image


class TestCase:
	input_image: List[List[int]]
	input_color: List[int]
	expected: List[List[int]]

	def __init__(self, image: List[List[int]], color: List[int], expected: str) -> None:
		self.input_image = image
		self.input_color = color
		self.expected = expected

	def compare_image(self, img1: List[List[int]], img2: List[List[int]]) -> bool:
		for i in range(0, len(img1)):
			for j in range(0, len(img1[i])):
				if img1[i][j] != img2[i][j]:
					return False
		return True

TESTCASES: List[TestCase] = [
	TestCase([[1,1,1],[1,1,0],[1,0,1]], [1, 1, 2], [[2,2,2],[2,2,0],[2,0,1]]),
	TestCase([[1,0,1],[0,1,0],[1,0,1]], [1, 1, 2], [[1,0,1],[0,2,0],[1,0,1]]),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.floodFill(case.input_image, case.input_color[0], case.input_color[1], case.input_color[2])
		if case.compare_image(case.expected, r):
			print(f"passed")
		else:
			print(f"failed {case.input_image}, {r} != {case.expected}")
	return

test()

