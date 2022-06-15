from audioop import add
from typing import Counter, Dict, List
from unittest import result


# Simple permutation
# => Can we fix the recursion with loop
class Permutation:
    def visit(self, selected: List[int], candidates: List[int], results: List[int]):
        if len(candidates) == 0:
            results.append(selected)
            return

        for i in range(0, len(candidates)):
            n = selected + [candidates[i]]
            c = candidates[0:i] + candidates[i+1:len(candidates)]
            self.visit(n, c, results)

    def gen_permutations(self, nums: List[int]):
        results = []
        self.visit([], nums, results)
        return results

    def test(self):
        results = self.gen_permutations([1, 2, 3])
        for i in range(0, len(results)):
            print(results[i])


# Permutation with duplicate
# When selecting candidate, we don't select duplicate
# => Can we fix the recursion with loop
class PermutationDistinct:
    def visit(self, selected: List[int], candidates: Dict[int, int], results: List[int]):
        _candidates = dict(filter(lambda x: x[1] > 0, candidates.items()))
        if len(_candidates) == 0:
            results.append(selected)
            return

        for i in _candidates.keys():
            n = selected + [i]
            _candidates[i] = _candidates[i] - 1
            self.visit(n, _candidates, results)
            _candidates[i] = _candidates[i] + 1

    def gen_permutations(self, nums: List[int]):
        results = []
        nums_count = Counter(nums)
        self.visit([], nums_count, results)
        return results

    def test(self):
        results = self.gen_permutations([1, 2, 3])
        for i in range(0, len(results)):
            print(results[i])
