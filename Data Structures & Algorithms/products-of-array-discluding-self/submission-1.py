class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zero_count = 0
        prod_without_zero = 1

        # count zeros and product of non-zero numbers
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod_without_zero *= num

        for num in nums:
            if zero_count > 1:
                # more than one zero → all results are zero
                res.append(0)
            else:
                if zero_count == 1:
                    # exactly one zero
                    if num == 0:
                        res.append(prod_without_zero)
                    else:
                        res.append(0)
                else:
                    # no zeros → normal case
                    res.append(prod_without_zero // num)

        return res

