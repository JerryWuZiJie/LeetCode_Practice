# example of dictionary!!!


def twoSum(self, nums, target):
    dict_list = {}
    for i in range(len(nums)):
        target_int = target - nums[i]
        if target_int in dict_list:
            # if dict_list[target_int] != i:
            # no need to check, since itself haven't append to the dict
            return (dict_list[target_int], i)
        dict_list[nums[i]] = i


'''
# nested loop, n^2 runtime
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
# hash table, 2n runtime
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict_list = {}
    for i in range(len(nums)):
        dict_list[nums[i]]=i
    for i in range(len(nums)):
        target_int = target - nums[i]
        if target_int in dict_list:
            if dict_list[target_int] != i:
                return (i, dict_list[target_int])
'''
