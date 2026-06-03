class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            #no profit
            if prices[i] <= minValue:
                minValue=prices[i]
                continue
            else:
                profit=max(profit, prices[i] - minValue)
        return profit