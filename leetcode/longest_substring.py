
'''
Find the longest substring having unique chars
'''


def getLongestSubstring(s: str) -> int:
    maxLen = 0
    curLen = 0
    istart = 0
    check = {}
    for i in range(len(s)):
        c = s[i]
        if c not in check:
            check[c] = i
            curLen += 1
            if curLen > maxLen:
                maxLen = curLen
        else:
            ic = check[c]
            for j in range(ic, istart-1, -1):
                if s[j] in check:
                    del check[s[j]]
            check[c] = i
            curLen -= ic - istart
            istart = ic + 1
    return maxLen


n = getLongestSubstring("abcabcdabc")
print(n)
