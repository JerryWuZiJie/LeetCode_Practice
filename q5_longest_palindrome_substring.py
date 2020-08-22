# check Manacher's Algorithm for a O(n) solution


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''

        i = 0
        result = (0, 0, 1)  # length, first index, last index
        while i < len(s):
            if i + 1 < len(s) and s[i + 1] == s[i]:
                num = 2
                while i + num < len(s) and i - num + 1 >= 0 and s[i + num] == s[i - num + 1]:
                    num += 1
                num -= 1
                if num * 2 > result[0]:
                    result = (num * 2, i - num + 1, i + num + 1)
            if i + 2 < len(s) and s[i + 2] == s[i]:
                i += 1
                num = 2
                while i + num < len(s) and i - num >= 0 and s[i + num] == s[i - num]:
                    num += 1
                num -= 1
                if num * 2 + 1 > result[0]:
                    result = (num * 2 + 1, i - num, i + num + 1)
                i -= 1
            i += 1
        return s[result[1]: result[2]]