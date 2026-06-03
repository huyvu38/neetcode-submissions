class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = min_prod = result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            #negative
            if num < 0:
                #swap
                max_prod, min_prod = min_prod, max_prod
            
            min_prod = min(num, min_prod * num)
            max_prod = max(num, max_prod * num)

            result=max(result, max_prod)

        return result