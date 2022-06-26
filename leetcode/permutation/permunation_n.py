'''
Problem:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Solution:
- Visit using back tracking
- Since this is permutation, at every step I can choose n-1 options
'''
from typing import List


class Solution:
	def visit(self, combination: List[int], options: List[int], results: List[List[int]]):
		if len(options) == 0:
			results.append(combination)
		else:
			for i in range(0, len(options)):
				opt = options[:i] + options[i+1:]
				self.visit(combination + [options[i]], opt, results)

	def permute(self, nums: List[int]) -> List[List[int]]:
		results = []
		self.visit([], nums, results)
		return results
