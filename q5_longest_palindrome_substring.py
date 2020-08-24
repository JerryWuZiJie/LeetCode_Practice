# check Manacher's Algorithm for a O(n) solution
# 11:50 https://www.youtube.com/watch?v=nbTSfrEfo6M&t=2s


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


# Manacher's algorithm
def manacher(s):
    if len(s) == 0:
        return ''

    n = len(s) * 2 + 3
    # s = abc    text = $#a#b#c#@
    text = ['#'] * n
    text[0] = '$'
    text[-1] = '@'
    k = 0
    for i in range(2, n - 2, 2):
        text[i] = s[k]
        k += 1

    length = [0] * n
    c = 0  # center
    r = 0  # right edge
    i_len = [0, 0]  # [index of text, length of palindrome]

    for i in range(2, n - 2):  # starts from first letter and ends with last letter
        if i < r:
            length[i] = min(r - i, length[2 * c - i])

        while text[i - length[i] - 1] == text[i + length[i] + 1]:
            length[i] += 1

        if i + length[i] > r:
            c = i
            r = i + length[i]

        if length[i] > i_len[0]:
            i_len[0] = length[i]
            i_len[1] = i

    # create max palindrome
    start = i_len[1] - i_len[0] + 1
    end = i_len[1] + i_len[0]
    return ''.join([text[t] for t in range(start, end, 2)])
