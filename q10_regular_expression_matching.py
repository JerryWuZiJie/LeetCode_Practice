# dynamic programming!!!
'''
if some steps need to be process in different ways, better use recursion
dynamic programming saves the previous results
'''


def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


# top down
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = {}

        def dp(i, j):
            if (i, j) not in result:
                if j == len(p):
                    result[(i, j)] = i == len(s)
                    return result[(i, j)]
                match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    result[(i, j)] = dp(i, j + 2) or match and dp(i + 1, j)
                else:
                    result[(i, j)] = match and dp(i + 1, j + 1)
            return result[(i, j)]

        return dp(0, 0)


# bottom up
class Solution2(object):
    def isMatch(self, text, pattern):
        # the number of false doesn't really matter, but need to have enough to store the values, so even len+2 works
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


print(Solution2().isMatch('aaa', 'aa.*a'))
