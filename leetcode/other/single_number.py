from typing import List


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		checked = dict()
		for n in nums:
			if f"{n}" in checked:
				del checked[f"{n}"]
			else:
				checked[f"{n}"] = n
		return list(checked.values())[0]
