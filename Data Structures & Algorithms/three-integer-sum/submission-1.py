class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            #skip duplicate i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 #left pointer
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    #skip duplicate j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j=j+1
                    while j < k and nums[k] == nums[k - 1]:
                        k=k-1
                    #move to new number for j and k
                    j=j+1
                    k=k-1
                elif nums[i] + nums[j] + nums[k] < 0:
                    #move left pointer to new number
                    j=j+1
                else:
                    #move right pointer to new number
                    k=k-1
        return res