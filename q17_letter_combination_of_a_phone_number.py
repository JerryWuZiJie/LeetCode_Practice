# use recursion is better; it's actually quite easy since time complexity is O(3^n)

from typing import List


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(3^n)
        if not len(digits):
            return ''
        res = ['']
        num_letter = [[], [], 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for num in digits:
            n = int(num)
            temp = res
            res = [letter + num_letter[n][0] for letter in temp]
            for i in range(1, len(num_letter[n])):
                res.extend([letter + num_letter[n][i] for letter in temp])

        return res


print(Solution().letterCombinations('23'))