
from typing import Any, List, Tuple


class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		r = ""
		for i in range(1, numRows+1):
			print(i)
			if i == 1 or i == numRows:
				for j in range(i, len(s)+1, numRows*2 - 2):
					r += s[j-1]
			else:
				for j in range(i, len(s)+1, numRows*2 - 2):
					r += s[j-1]
					jj = j + (numRows-i)*2
					if jj <= len(s):
						r += s[jj-1]
		return r



class TestCase:
	input: tuple[str, int]
	expected: str

	def __init__(self, input: Any, expected: str) -> None:
		self.input = input
		self.expected = expected

TESTCASES: List[TestCase] = [
	TestCase(("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
	# TestCase(("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.convert(case.input[0], case.input[1])
		if r == case.expected:
			print(f"passed!")
		else:
			print(f"failed! {case.input}, {r}, expected: {case.expected}")
	return

test()

# class Test:
# 	name = "Quan"

# d = Test()
# print(d.name)
