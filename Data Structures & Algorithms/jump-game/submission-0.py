class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            #cannot reach to i
            if i > farthest:
              return False
            
            farthest = max(farthest, i + nums[i])
        
        return True