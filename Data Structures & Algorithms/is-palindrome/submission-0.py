class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for c in s:
            if c.isalnum() == True:
               res=res+c
        res = res.lower()
        print(res)
        for i in range(0, len(res)):
            if res[i] != res[len(res)-1-i]:
              return False
        return True