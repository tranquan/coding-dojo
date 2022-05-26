# https://leetcode.com/problems/container-with-most-water/

from tabnanny import check
from typing import List


class Solution:
	def calcArea(self, height: List[int], i: int, j: int) -> int:
		return min(height[i], height[j]) * abs(i-j)


	# brute force
	# O(n^2)
	def maxArea(self, height: List[int]) -> int:
		m = 0
		for i in range(len(height)-1):
			for j in range(i+1, len(height)):
				area = self.calcArea(height, i, j)
				if m < area:
					m = area
		return m


	def maxAreaAtLevel(self, height: List[int], level: int) -> int:
		l, r = 0, len(height)-1
		for i in range(0, r):
			if height[i] >= level:
				l = i
				break
		for i in range(r, l, -1):
			if height[i] >= level:
				r = i
				break
		return self.calcArea(height, l, r)


	# goes from top to bottom, fine largest container at each level
	# O(n x max height)
	def maxArea2(self, height: List[int]) -> int:
		m = 0
		checked = {}
		max_width = len(height) - 1
		height_desc = sorted(height, reverse=True)
		for level in height_desc:
			if level in checked:
				continue
			checked[level] = True
			max_area_possible = level * max_width
			area = self.maxAreaAtLevel(height, level)
			print(level, max_area_possible, area)
			if m < area:
				m = area
			if m >= max_area_possible:
				break
		return m


	# start with max width from both sides, move left or right column into center until l = r
	def maxArea3(self, height: List[int]) -> int:
		l, r = 0, len(height)-1
		m = self.calcArea(height, l, r)
		while l < r:
			if height[l] <= height[r]:
				found = False
				for i in range(l, r):
					if height[i] > height[l]:
						l = i
						found = True
						break
				if not found:
					l = r
			elif height[l] > height[r]:
				found = False
				for i in range(r, l, -1):
					if height[i] > height[r]:
						r = i
						found = True
						break
				if not found:
					r = l
			area = self.calcArea(height, r, l)
			if area > m:
				m = area
		return m


tests = [
	[[1,2,3,15,4,5,12,1,2,5], 36],
	[[1,8,6,2,5,4,8,3,7], 49],
	[[1,2,4,3], 4]
]

def test():
	for test in tests:
		s = Solution()
		v = s.maxArea3(test[0])
		if v == test[1]:
			print(f"{test[0]} pass!")
		else:
			print(f"{test[0]} fail! expected: {test[1]}, get: {v}")

test()

# t = tests[0][0]
# s = Solution()
# v = s.maxAreaAtLevel(t, 3)
# print(v)
