from tkinter import CASCADE
from typing import List

DIGITS = {
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz",
}

# use back tracking with another function, at each step, take a number out
class Solution:
	def visit(self, digits: str, combination: str, results: List[str]):
		if len(digits) == 0 and len(combination) > 0:
			results.append(combination)
		else:
			chars = list(DIGITS[digits[0]])
			for c in chars:
				self.visit(digits[1:], combination+c, results)

	# Back tracking using recursive
	def letterCombinations1(self, digits: str) -> List[str]:
		if len(digits) == 0:
			return []
		results = []
		self.visit(digits, "", results)
		return results

	# Back tracking using stack
	def letterCombinations2(self, digits: str) -> List[str]:
		if len(digits) == 0:
			return []
		results = []
		stack = []
		chars = list(DIGITS[digits[0]])
		for c in chars:
			stack.append({"digits": digits[1:], "combination": c})
		while len(stack) > 0:
			item = stack.pop()
			s_digits = item['digits']
			if len(s_digits) == 0:
				results.append(item['combination'])
			else:
				s_chars = list(DIGITS[s_digits[0]])
				for c in s_chars:
					stack.append({"digits": s_digits[1:], "combination": item['combination']+c})
		return results


TESTCASES = [
	{
		"digits": "23",
		"expected": ["ad","ae","af","bd","be","bf","cd","ce","cf"]
	},
	{
		"digits": "2",
		"expected": ["a", "b", "c"]
	},
	{
		"digits": "",
		"expected": []
	},
]

def test():
	s = Solution()
	for case in TESTCASES:
		e = sorted(case['expected'])
		r = s.letterCombinations2(case['digits'])
		r = sorted(r)
		success = True
		if len(r) != len(e):
			success = False
		else:
			for i in range(0, len(r)):
				if r[i] != e[i]:
					success = False
					break
		if success:
			print(f"passed!")
		else:
			print(f"failed! {case['digits']}, {r}, expected: {e}")
	return

test()

