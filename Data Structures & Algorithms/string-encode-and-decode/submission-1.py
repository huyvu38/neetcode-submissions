class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            num = ""
            while s[i].isdigit():
                num=num+s[i]
                i+=1
            length = int(num)
            #skip the #
            i = i + 1
            res.append(s[i:i+length])
            #move to next digit
            i = i + length

        return res
