class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_length = len(nums)
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right-left+1)
                total = total - nums[left]
                left = left + 1
        return min_length