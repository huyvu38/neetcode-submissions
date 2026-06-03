from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # dictionary to store last index of each number

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True  # found duplicate within k distance
            # update last index of this number
            seen[num] = i

        return False