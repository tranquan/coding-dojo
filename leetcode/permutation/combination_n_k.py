
'''
Problem:
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

Solution:
- Use stack to backtracking, at each step there should be n options to pick the next number
- Pass the results array to the function, when combinations length =
'''
from typing import Dict, List


class Solution:
	def visit(self, k: int, combination: List[int], options: List[int], results: List[List[int]]):
		if len(combination) == k:
			results.append(combination)
		else:
			for i in range(0, len(options)):
				opt = options[i+1:]
				self.visit(k, combination + [options[i]], opt, results)

	
	def combine(self, n: int, k: int) -> List[List[int]]:
		if k > n:
			return []
		results = []
		self.visit(k, [], list(range(1, n+1)), results)
		return results



class TestCase:
	input: List[int]
	expected: List[List[int]]

	def __init__(self, input: List[int], expected: List[List[int]]) -> None:
		self.input = input
		self.expected = expected

	def toString(self, l: List[List[int]]) -> str:
		d = {}
		for i in range(0, len(l)):
			ll = sorted(l[i])
			ll_str = map(lambda x: str(x), ll)
			d[','.join(ll_str)] = True
		keys = sorted(d.keys())
		return '_'.join(keys)

	def compare(self, m1: List[List[int]], m2: List[List[int]]):
		return self.toString(m1) == self.toString(m2)


TESTCASES: List[TestCase] = [
	TestCase([4,2], [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]),
]

def test():
	s = Solution()
	for case in TESTCASES:
		r = s.combine(case.input[0], case.input[1])
		if case.compare(case.expected, r):
			print(f"passed")
		else:
			print(f"failed {case.input}, {r} != {case.expected}")

test()

# t = TestCase([4,2], [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]])
# print(t.toString([[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]))
# print(':'.join(map([1,2,2,3,4], lambda x: str(x))))

# t = list(range(0, 10))
# print(t)
