class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = dict()
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] = frequency[num] + 1
        for value in frequency.values():
            if value > 1:
                return True
        return False