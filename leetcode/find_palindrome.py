# Brute force
import math


class Solution1:
    # normal way to check palindrome, no need to use previous checked
    def checkPalindrome(self, s: str) -> bool:
        n = int(len(s))
        for i in range(0, int(n/2)):
            if s[i] != s[n-1-i]:
                return False
        return True

    # brute force, check all sub strings
    def longestPalindrome1(self, s: str) -> str:
        n = int(len(s))
        if n == 1:
            return s
        s_max = ""
        for i in range(0, n):
            for j in range(n, i, -1):
                ss = s[i:j]
                if self.checkPalindrome(ss):
                    if len(ss) > len(s_max):
                        s_max = ss
        return s_max

    # same brute force, but optimize a bit by using queue
    def longestPalindrome2(self, s: str) -> str:
        n = int(len(s))
        if n == 1:
            return s
        checked = {}
        checks = []
        checks.append([0, n])
        while len(checks) > 0:
            c = checks.pop(0)
            i, j = c[0], c[1]
            if self.checkPalindrome(s[i:j]):
                return s[i:j]
            if i+1 < j:
                if f"{i+1}_{j}" not in checked:
                    checked[f"{i+1}_{j}"] = True
                    checks.append([i+1, j])
            if i < j-1:
                if f"{i}_{j-1}" not in checked:
                    checked[f"{i}_{j-1}"] = True
                    checks.append([i, j-1])
        return ""


# Use dynamic programming
class Solution2:
    def checkPalindrome(self, s: str, checked: dict):
        if s in checked:
            return checked[s]
        elif len(s) <= 1:
            # trivial, s is palindrome s is '' or only have 1 char
            if s not in checked:
                checked[s] = True
            return True
        else:
            # s is palindrome if first and last char is the same and the middle string is palindrome
            mid = s[1:len(s)-1]
            is_mid_palindrome = checked[mid]
            if s[0] == s[len(s)-1] and is_mid_palindrome:
                checked[s] = True
                return True
            else:
                checked[s] = False
                return False

    def longestPalindrome(self, s: str) -> str:
        p = ''
        checked = {}
        checked[''] = True
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                ss = s[j:i]
                if self.checkPalindrome(ss, checked) and len(ss) > len(p):
                    p = ss
        return p


# Expand around center
class Solution3:
    # center could be one char or two char, hence left, right
    # return the length of longest palindrome
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        n = len(s)
        l, r = left, right
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_l = 0
        start, end = 0, 0
        for i in range(0, len(s)-1):
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i+1)
            l = max(l1, l2)
            if l > max_l:
                max_l = l
                start = i - math.floor((l - 1) / 2)
                end = i + math.floor((l / 2))
        return s[start:end+1]


# Test

s1 = ["a", "a"]
s2 = ["ab", "a"]
s3 = ["aba", "aba"]
s4 = ["aaa", "aaa"]
s5 = ["abcddcbxyziuia", "bcddcb"]
s6 = ["abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa",
      "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"]


def main():
    sol = Solution3()
    test = [s1, s2, s3, s4, s5, s6]
    # test = [s1]
    for t in test:
        r = sol.longestPalindrome(t[0])
        if len(r) != len(t[1]):
            print(f"wrong length: expected: {t[1]}, get: {r}")
        elif r != t[1]:
            print(f"same length. wrong result: expected: {t[1]}, get: {r}")
        else:
            print(f"success: {t}")


main()
