# example of sliding window!!!

def lengthOfLongestSubstring(s):
    # sliding window approach
    # runtime: n
    result = 0
    dic = {}
    i = -1
    for j in range(len(s)):
        if s[j] in dic:
            i = max(i, dic[s[j]])
        result = max(result, j - i)
        print(i, j, j-1)
        dic[s[j]] = j
    return result