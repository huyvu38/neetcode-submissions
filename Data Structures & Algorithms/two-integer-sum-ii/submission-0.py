class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)
        while left < right:
            if numbers[left-1] + numbers[right-1] == target:
                return [left, right]
            elif numbers[left-1] + numbers[right-1] < target:
                left = left + 1
            else:
                right = right - 1
        return [-1, -1]
        