class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        #After sort -> List of number increasing from l to r
        for i in range (0, len(nums) - 1):
            if (nums[i] == nums[i+1]):
                return True
        return False
