class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        s2_count = Counter()
        window_length = 0
        for right in range(len(s2)):
            if s2[right] not in s2_count:
                s2_count[s2[right]] = 1
            else:
                #s2[right] is a specific char
                s2_count[s2[right]] = s2_count[s2[right]] + 1
            window_length=window_length+1
            if window_length == len(s1):
                #match
                if s1_count == s2_count:
                    return True
                else:
                    window_length= window_length-1
                    #remove left most
                    left_char=s2[right-len(s1)+1]
                    if s2_count[left_char] > 0:
                        s2_count[left_char] = s2_count[left_char] - 1
                    else:
                        del s2_count[left_char]
        return False