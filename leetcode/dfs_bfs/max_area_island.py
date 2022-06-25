from typing import List


class Solution:
	def findAreaSize(self, grid: List[List[int]], sr: int, sc: int) -> int:
		if len(grid) == 0:
			return 0
		len_r = len(grid)
		len_c = len(grid[0])
		visited = {}
		next = [sc, sr]
		size = 0
		while len(next) > 0:
			r = next.pop()
			c = next.pop()
			key = f"{r}_{c}"
			if key in visited:
				continue
			size += 1
			visited[key] = True
			grid[r][c] = 2
			if r-1 >= 0 and grid[r-1][c] == 1:
				next.insert(0, r-1)
				next.insert(0, c)
			if r+1 < len_r and grid[r+1][c] == 1:
				next.insert(0, r+1)
				next.insert(0, c)	
			if c-1 >= 0 and grid[r][c-1] == 1:
				next.insert(0, r)
				next.insert(0, c-1)
			if c+1 < len_c and grid[r][c+1] == 1:
				next.insert(0, r)
				next.insert(0, c+1)
		return size

	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		maxArea = 0
		rows = len(grid)
		cols = len(grid[0])
		for r in range(0, rows):
			for c in range(0, cols):
				if grid[r][c] == 1:
					area = self.findAreaSize(grid, r, c)
					print(f"{r}:{c}: {area}")
					if area > maxArea:
						maxArea = area
		return maxArea


def test():
	t = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
	s = Solution()
	area = s.maxAreaOfIsland(t)
	print(area)

test()
