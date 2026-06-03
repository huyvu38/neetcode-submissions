class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            #Find all first sequence
            length = 0
            if (num - 1) not in num_set:
                end = num
                while end in num_set:
                    end = end + 1
                    length = length + 1
            max_length = max(max_length, length)
        return max_length