class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = Counter(t)
        window_count = {}
        min_length = float('inf')
        min_window=""
        count = 0
        left = 0
        for right, char in enumerate(s):
            if char in t_count:
              window_count[char] = window_count.get(char, 0) + 1
              if window_count[char] == t_count[char]:
                count += 1
            while left<=right and count == len(t_count):
                #update if new size < current size
                if right-left+1 < min_length:
                    min_length=right-left+1
                    min_window=s[left:right+1]
                #move left pointer to next character in s that also appear in t
                #remove current left_char
                left_char=s[left]
                if left_char in t_count:
                    window_count[left_char] = window_count[left_char] - 1
                    if window_count[left_char] < t_count[left_char]:
                        count = count - 1
                left=left+1
        return min_window