'''
Problem:
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Solution:
- Meed to know if a char can change case (not a number)
- Use back tracking, pick option at each step, if the char can be case convert, I will visit two of its variant
'''
from typing import List


class Solution:
	def visit(self, combination: str, options: str, results: List[str]):
		if len(options) == 0:
			results.append(combination)
			return
		c = options[0]
		if c.lower() == c.upper():
			self.visit(combination + c, options[1:], results)
		else:
			self.visit(combination + c.lower(), options[1:], results)
			self.visit(combination + c.upper(), options[1:], results)


	def letterCasePermutation(self, s: str) -> List[str]:
		results = []
		self.visit("", s, results)
		return results
