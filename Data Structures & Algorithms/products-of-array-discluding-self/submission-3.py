class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        #calculate prefix for left
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]

        #calculate prefix for right
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]

        arr = [0] * len(nums)
        for i in range(0, len(nums)):
            arr[i] = left[i] * right[i]
        return arr