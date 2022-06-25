from typing import List

INT_TO_ROMAN = {
	1: "I",
	4: "IV",
	5: "V",
	9: "IX",
	10: "X",
	40: "XL",
	50: "L",
	90: "XC",
	100: "C",
	400: "CD",
	500: "D",
	900: "CM",
	1000: "M",
}

ROMANS = sorted(INT_TO_ROMAN.keys(), reverse=True)

class Solution:
	# Has to split the numb into sum of int that can be convert to roman
	# - Check if the number is on the map
	# - Yes: return it, No: split the number into 2
	def intToRoman(self, num: int) -> str:
		if num in INT_TO_ROMAN:
			return INT_TO_ROMAN[num]
		else:
			for r in ROMANS:
				if num > r:
					return self.intToRoman(r) + self.intToRoman(num-r)
			return ""


class TestCase:
	input: int
	expected: str

	def __init__(self, i: int, e: str) -> None:
		self.input = i
		self.expected = e

TESTCASES: List[TestCase] = [
	TestCase(1, "I"),
	TestCase(2, "II"),
	TestCase(5, "V"),
	TestCase(4, "IV"),
	TestCase(12, "XII"),
	TestCase(113, "CXIII"),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.intToRoman(case.input)
		if r == case.expected:
			print(f"passed")
		else:
			print(f"failed {case.input}, {r} != {case.expected}")
	return

test()

