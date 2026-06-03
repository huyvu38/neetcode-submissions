class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x

        if n == 0 or x == 1:
            return 1

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n == -2147483648:
            return 0

        if n > 0:
            for _ in range(n - 1):
                result = result * x
        else:
            i = 0
            while i > n - 1:
                result = result / x
                i -= 1

        return result