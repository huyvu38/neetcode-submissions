class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        res=0
        left = 0
        freq={}
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            max_freq = max(freq[s[right]], max_freq)
            #right-left+1 is window size
            #cannot do while loop if window size after replace character less than max_freq
            while right - left + 1 - max_freq > k:
                freq[s[left]] -=1
                left=left+1
            res=max(res, right-left+1)
        return res

