from typing import List
from datetime import datetime


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            v = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == v:
                    return [i, j]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i in range(len(nums)):
            c = target - nums[i]
            if c in complements:
                return [complements.get(c), i]
            else:
                complements[nums[i]] = i
        return []


inputs = [
    [[3, 2, 3, 4], 6, [0, 2]],
    [[2, 3, 4], 6, [0, 2]],
    [[1, 2, 3, 4, 5, 6], 7, [0, 5]],
]


start = datetime.now().microsecond

for test in inputs:
    r = Solution().twoSum2(test[0], test[1])
    if r[0] == test[2][0] and r[1] == test[2][1]:
        print(f'passed: {test[0]}')
    else:
        print(f'wrong: {test[0]} expected: {test[2]} get: ${r}')

end = datetime.now().microsecond
print(f'time: {end-start}')
