class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        while len(word1) != 0 and len(word2) != 0:
            s = s + word1[0] + word2[0]
            word1= word1[1:]
            word2 = word2[1:]
        #Append additional
        s = s+ word1 + word2
        return s