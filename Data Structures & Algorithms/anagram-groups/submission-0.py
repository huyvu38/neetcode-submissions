class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        if len(strs) == 1:
            return [strs]
        for s in strs:
            #Count frequency of each string
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            if key not in dictionary:
                dictionary[key] = [s]
            else:
                dictionary[key].append(s)
        return list(dictionary.values())

