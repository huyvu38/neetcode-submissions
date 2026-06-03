class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, number in enumerate(nums):
            if target - number not in dictionary:
                dictionary[number] = index
            else:
                return [dictionary[target - number], index]