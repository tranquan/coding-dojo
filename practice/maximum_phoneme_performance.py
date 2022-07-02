from logging import warning
from typing import Dict, List

from typing_extensions import Self


class Score:
	score: float
	phoneme: str

	def __repr__(self) -> str:
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

'''
Dynamic programming: cache scores of previous length to calculate scores for the next length
- Time complex: O(n^2)
- Space complex: O(n)
'''
def calculate_maximum_phoneme_sequence(scores: List[Score]) -> Dict[int, SequenceScore]:
	n = len(scores)
	result: Dict[int, SequenceScore] = {}
	prev_length_scores: List[float] = []
	
	min_score = min(list(map(lambda x: x.score, scores)) + [0])
	reached_min_score = False
	for length in range(1, n+1):

		# A. When we reach min_score: means previous length max_score = min_score
		# [1] We won't able to find any sequence with larger score
		# - Because the sub-sequence always have score >= its longer sequence
		# - If there is a sequence with larger score, its sub-sequence should be catched in the previous check
		# [2] The sequence should start from 0
		# - Because we know there is no sequence can have a larger score based on [1]
		# - We also know the max_score is min_score now, in other words, all sequence has the same score now
		# - So it doesn't matter whether we take the first sequence or next, all has the same score
		# Because if there is a 
		if reached_min_score:
			sequence = scores[0:length]
			result[length] = SequenceScore(min_score, list(map(lambda x: x.phoneme, sequence)))
			continue
		
		# B. Not reached min_score yet => calculate score for all sequences
		cur_length_scores = []
		max_sequence_score = 0
		sequence_start_i = 0

		for s in range(0, n+1-length):
			# For sequence length=1; the score of sequence is the phoneme's score itself
			# Set prev_score=101 so it will get the phoneme's score
			prev_score = 101 if length == 1 else prev_length_scores[s]
			score = min(scores[s+length-1].score, prev_score)
			cur_length_scores.append(score)
			
			if score > max_sequence_score:
				max_sequence_score = score
				sequence_start_i = s

		sequence = scores[sequence_start_i:sequence_start_i+length]
		result[length] = SequenceScore(max_sequence_score, list(map(lambda x: x.phoneme, sequence)))

		prev_length_scores = cur_length_scores
		reached_min_score = max_sequence_score == min_score		

	return result

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


empty_scores = TestCase(
	input = [], 
	expected={})

normal_scores = TestCase(
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
			'sequence': ['/ð/', '/ə/', '/n/']
		},
		4: {
			'max sequence score': 40,
			'sequence': ['/ð/', '/ə/', '/n/', '/ɛ/']
		},
		5: {
			'max sequence score': 37,
			'sequence': ['/ð/', '/ə/', '/n/', '/ɛ/', '/t/']
		},
	})

single_scores = TestCase(
	input = [
		{'phoneme': '/ð/', 'score': 20}, 
	], 
	expected={
		1: {
			'max sequence score': 20,
			'sequence': ['/ð/']
		},
	})

same_scores = TestCase(
	input = [
		{'phoneme': '/ð/', 'score': 90}, 
		{'phoneme': '/a/', 'score': 90},
		{'phoneme': '/t/', 'score': 90},
		{'phoneme': '/n/', 'score': 90},
	], 
	expected={
		1: {
			'max sequence score': 90,
			'sequence': ['/ð/']
		},
		2: {
			'max sequence score': 90,
			'sequence': ['/ð/', '/a/']
		},
		3: {
			'max sequence score': 90,
			'sequence': ['/ð/', '/a/', '/t/']
		},
		4: {
			'max sequence score': 90,
			'sequence': ['/ð/', '/a/', '/t/', '/n/']
		},
	})

one_zero_scores = TestCase(
	input = [
		{'phoneme': '/a/', 'score': 0}, 
		{'phoneme': '/n/', 'score': 80}, 
		{'phoneme': '/t/', 'score': 90}, 
	], 
	expected={
		1: {
			'max sequence score': 90,
			'sequence': ['/t/']
		},
		2: {
			'max sequence score': 80,
			'sequence': ['/n/', '/t/']
		},
		3: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/']
		},
	})

repeat_phoneme_scores = TestCase(
	input = [
		{'phoneme': '/a/', 'score': 80}, 
		{'phoneme': '/n/', 'score': 60}, 
		{'phoneme': '/t/', 'score': 20}, 
		{'phoneme': '/a/', 'score': 70},
	], 
	expected={
		1: {
			'max sequence score': 80,
			'sequence': ['/a/']
		},
		2: {
			'max sequence score': 60,
			'sequence': ['/a/', '/n/']
		},
		3: {
			'max sequence score': 20,
			'sequence': ['/a/', '/n/', '/t/']
		},
		4: {
			'max sequence score': 20,
			'sequence': ['/a/', '/n/', '/t/', '/a/']
		},
	})

many_scores = TestCase(
	input = [
		{'phoneme': '/a/', 'score': 90}, 
		{'phoneme': '/n/', 'score': 80}, 
		{'phoneme': '/t/', 'score': 30}, 
		{'phoneme': '/b/', 'score': 0}, 
		{'phoneme': '/d/', 'score': 99}, 
		{'phoneme': '/f/', 'score': 0}, 
		{'phoneme': '/g/', 'score': 60}, 
		{'phoneme': '/ng/', 'score': 80}, 
		{'phoneme': '/s/', 'score': 50}, 
		{'phoneme': '/r/', 'score': 40}, 
	], 
	expected={
		1: {
			'max sequence score': 99,
			'sequence': ['/d/']
		},
		2: {
			'max sequence score': 80,
			'sequence': ['/a/', '/n/']
		},
		3: {
			'max sequence score': 50,
			'sequence': ['/g/', '/ng/', '/s/']
		},
		4: {
			'max sequence score': 40,
			'sequence': ['/g/', '/ng/', '/s/', '/r/']
		},
		5: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/']
		},
		6: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/', '/f/']
		},
		7: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/', '/f/', '/g/']
		},
		8: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/', '/f/', '/g/', '/ng/']
		},
		9: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/', '/f/', '/g/', '/ng/', '/s/']
		},
		10: {
			'max sequence score': 0,
			'sequence': ['/a/', '/n/', '/t/', '/b/', '/d/', '/f/', '/g/', '/ng/', '/s/', '/r/']
		},
	})

TEST_CASES: List[TestCase] = [
	empty_scores, 
	normal_scores, 
	single_scores, 
	same_scores, 
	one_zero_scores, 
	repeat_phoneme_scores, 
	many_scores
]

def test():
	pass_count = 0
	for test in TEST_CASES:
		print(f'Test case: {test.input}')
		result = calculate_maximum_phoneme_sequence(test.input)
		if TestCase.is_equal(result, test.expected):
			pass_count += 1
			print(f'-> Passed ✓\n')
		else:
			print(f'-> Failed ⚠️')
			print(f'-> Expected: {test.expected}')
			print(f'-> Result  : {result}\n')
	
	print(f'--------------------')
	print(f'Summary: {pass_count}/{len(TEST_CASES)} tests passed')
	print(f'--------------------')

test()
