from typing import List

'''
Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Tips:
- Dynamic programming because it looks complicated and doesn't fall into tree, bfs or dfs
=> Try to think of dynamic programming when the problem:
- doesn't clear
- doesn't fall into DFS, BFS, Tree, pointer
- think if it solable if making the problem simpler? smaller scale?

Solution:
- At each step, we need to decide whether we should rob the next house
- To decide, we check the value of n-2 + n and n-1 to; because the house cannot next to each other
'''
class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		if n < 3:
			return max(nums)

		cached = {}
		cached["0"] = nums[0]
		cached["1"] = nums[0] if nums[0] > nums[1] else nums[1]

		for i in range(2, n):
			m1 = nums[i] + cached[f"{i-2}"]
			m2 = cached[f"{i-1}"]
			cached[f"{i}"] = max(m1, m2)

		return cached[f"{n-1}"]
