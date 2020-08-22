# two pointers!!!
# sometimes nested function helps a lot, say sort()
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:  # if equal, then duplicated
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    sums = nums[i] + nums[j] + nums[k]
                    if sums == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        while j+1 < len(nums) and nums[j] == nums[j+1]:
                            j += 1
                        while k > 0 and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif sums < 0:
                        j +=  1
                    else:
                        k -= 1
            i += 1
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))