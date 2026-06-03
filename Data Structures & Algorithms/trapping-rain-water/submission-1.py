class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        l_max = height[l]
        r_max=height[r]
        total = 0
        while l < r:
            if l_max < r_max:
                total = total + l_max - height[l]
                l=l+1
                l_max=max(l_max, height[l])
            else:
                total = total + r_max - height[r]
                r=r-1
                r_max=max(r_max,height[r])
        return total