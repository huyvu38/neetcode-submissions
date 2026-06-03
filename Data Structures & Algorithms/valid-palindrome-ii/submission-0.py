class Solution:
    def validPalindrome(self, s):
        #helper function to check whether palindorme
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                #skip left most or right most
                return (
                    is_palindrome(left + 1, right)
                    or
                    is_palindrome(left, right - 1)
                )

            left += 1
            right -= 1

        return True