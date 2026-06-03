class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency_s = dict()
        frequency_t = dict()
        for c in s:
            if c not in frequency_s:
                frequency_s[c] = 1
            else:
                frequency_s[c] = frequency_s[c] + 1
        for c in t:
            if c not in frequency_t:
                frequency_t[c] = 1
            else:
                frequency_t[c] = frequency_t[c] + 1
        #Compare frequency
        return frequency_s == frequency_t