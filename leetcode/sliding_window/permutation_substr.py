class Solution:
	def isPermutation(self, sorted_s1: str, s2: str):
		return sorted_s1 == ''.join(sorted(s2))

	def checkInclusion(self, s1: str, s2: str) -> bool:
		n = len(s1)
		sorted_s1 = ''.join(sorted(s1))
		if n > len(s2):
			return False
		for i in range(0, len(s2) - n + 1):
			if self.isPermutation(sorted_s1, s2[i:i+n]):
				return True
		return False



cases = [
	{"s1": "ab", "s2": "eibaooo12aa", "e": True},
	{"s1": "ab", "s2": "eibbooo12aa", "e": False},
	{"s1": "cab", "s2": "cabzzooo12aa", "e": True},
	{"s1": "cab", "s2": "eibacooo1abc", "e": True},
	{"s1": "adc", "s2": "dcda", "e": True}
]

def test():
	sol = Solution()
	for case in cases:
		r = sol.checkInclusion(case["s1"], case["s2"])
		if r == case["e"]:
			print(f"Passed!")
		else:
			print(f"Failed. {case}, result: {r}")
test()
