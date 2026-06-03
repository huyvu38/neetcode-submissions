class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(0, len(nums)):
            if target - nums[i] not in dictionary:
                dictionary[nums[i]] = i
            else:
                return [dictionary[target - nums[i]], i]