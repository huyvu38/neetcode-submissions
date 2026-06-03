class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        left = 0
        char_dict = dict()
        for right in range(len(s)):
            if s[right] in char_dict and char_dict[s[right]] >=left:
                left=char_dict[s[right]] + 1
            #Always update the last index of every character
            char_dict[s[right]]=right
            max_length = max(max_length, right-left+1)
        return max_length