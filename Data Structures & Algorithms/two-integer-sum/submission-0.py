class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in dictionary:
                return [dictionary[diff], index]
            dictionary[num] = index
