class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #if it not then compare 
            if nums[left] <= nums[mid]: #left part is sorted
                if nums[left] <= target and target <= nums[mid]:
                    right=mid-1 #target in between left and mid
                else:
                    left=mid+1
            else:
                #Right part is sort
                if nums[mid] <= target and target <= nums[right]:
                    #target in between mid and right
                    left=mid+1
                else:
                    right=mid-1
        #not find
        return -1