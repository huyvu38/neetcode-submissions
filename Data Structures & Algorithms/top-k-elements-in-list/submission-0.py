class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1
        res = []
        for key, value in freq.items():
            res.append([value, key])
        #ascending sort
        res.sort()
        return [item[1] for item in res[-k:]]