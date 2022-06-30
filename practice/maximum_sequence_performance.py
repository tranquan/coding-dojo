import json
from telnetlib import SE
from typing import Dict, List

from typing_extensions import Self

# What does it mean by all possible N?

# "consecutive phoneme sequence"

'''
Questions:
[1] Could AI return duplicate phoneme? => maybe not

Notes:
[1] Given score array length 10, I have to calculate score for length: 1,2,3,4...10
- It could be there is a length that doesn't found any sequence satisfy
- For each len, find the sequence that have max score

[2] Easy to see, for len = 1, it's the largest score in input

[3] Dynamic programming: 
- store min score at each len, say m
- to calculate score at len m+1, we only need to compare max_score[m] with score[m+1], take the smaller
'''

class Score:
	phoneme: str
	score: float

	def __repr__(self) -> str:
		return f'(Score: phoneme:{self.phoneme} score:{self.score})'
	
	def __json__(self) -> str:
		return f'(Score: phoneme:{self.phoneme} score:{self.score})'

	def __init__(self,  phoneme: str, score: float) -> None:
		self.phoneme = phoneme
		self.score = score


class SequenceScore:
	score: float
	sequence: List[str]

	def __repr__(self) -> str:
		return f'(SequenceScore: score:{self.score} sequence:{self.sequence})'

	def __init__(self, score: float, sequence: List[str]) -> None:
		self.score = score
		self.sequence = sequence

	def is_equal(self, target: Self) -> bool:
		return self.score == target.score and self.sequence == target.sequence

def calculate_maximum_phoneme_performance(scores: List[Score]) -> Dict[int, SequenceScore]:
	return {}

# ------------------------------
# TEST
# ------------------------------

class TestCase:
	input: List[Score]
	expected: Dict[int, SequenceScore]

	def __init__(self, input: List[Dict], expected: Dict[int,Dict]) -> None:
		self.input = list(map(lambda x: Score(x['phoneme'], x['score']), input))
		_expected = dict()
		for k in expected:
			v = expected[k]
			_expected[k] = SequenceScore(v['max sequence score'], v['sequence'])
		self.expected = _expected

	@staticmethod
	def is_equal(e1: Dict[int, SequenceScore], e2: Dict[int, SequenceScore]) -> bool:
		if len(e1) != len(e2):
			return False
		for k in e1:
			if k not in e2:
				return False
			if not e1[k].is_equal(e2[k]):
				return False
		return True


t0 = TestCase(
	input = [], 
	expected={})

t1 = TestCase(
	input = [
		{'phoneme': '/ð/', 'score': 100}, 
		{'phoneme': '/ə/', 'score': 40},
		{'phoneme': '/n/', 'score': 87},
		{'phoneme': '/ɛ/', 'score': 99},
		{'phoneme': '/t/', 'score': 37}
	], 
	expected={
		1: {
			'max sequence score': 100,
			'sequence': ['/ð/']
		},
		2: {
			'max sequence score': 87,
			'sequence': ['/n/', '/ɛ/']
		},
		3: {
			'max sequence score': 40,
			'sequence': ['/ð', '/ə/', '/n/']
		},
		4: {
			'max sequence score': 40,
			'sequence': ['/ð', '/ə/', '/n/', '/ɛ/']
		},
		5: {
			'max sequence score': 37,
			'sequence': ['/ð', '/ə/', '/n/', '/ɛ/', '/t/']
		},
	})


TEST_CASES: List[TestCase] = [t0, t1]

def test():
	for test in TEST_CASES:
		print(f'--------------------')
		print(f'Test: scores: {test.input}')
		result = calculate_maximum_phoneme_performance(test.input)
		if TestCase.is_equal(result, test.expected):
			print(f'Passed')
		else:
			print(f'Failed')
			print(f'-> Expected: {test.expected}')
			print(f'-> Get: {result}')
		print(f'--------------------')
	return

test()
