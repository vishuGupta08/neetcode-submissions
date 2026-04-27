class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = len(prices)-1
        maxProfit = 0
        while l < r:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                if prices[l+1] < prices[r]:
                    l += 1
                else:
                    r -= 1
        return maxProfit
        
        