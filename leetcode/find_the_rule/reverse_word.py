'''
Reverse word in a string but keep space and word order the same
Example:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution:
	def reverseWords(self, s: str) -> str:
		words = s.split(' ')
		for i in range(0, len(words)):
			if not words[i].isspace():
				words[i] = words[i][::-1]
		return ' '.join(words)
	
	def reverseWords2(self, s: str) -> str:
		word = []
		r = ''
		for i in range(0, len(s)):
			if s[i].isspace():
				if len(word) > 0:
					rev_word = reversed(word)
					r += ''.join(rev_word)
					word = []
				r += s[i]
			else:
				word.append(s[i])
		if len(word) > 0:
			rev_word = reversed(word)
			r += ''.join(rev_word)
		return r


s = "Let's take LeetCode contest"
e = "s'teL ekat edoCteeL tsetnoc"

def test():
	sol = Solution()
	r = sol.reverseWords(s)
	if r == e:
		print(f"Passed!. {r}")
	else:
		print(f"Failed!. {r}")
test()
