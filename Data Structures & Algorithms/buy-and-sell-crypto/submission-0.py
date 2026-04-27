class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = len(prices)-1
        maxProfit = 0
        while l < r:
            if prices[l]> prices[r]:
                l += 1
            elif prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                r -= 1
            else:
                if prices[l+1] < prices[r]:
                    l += 1
                elif prices[l] < prices[r-1]:
                    r -= 1
        return maxProfit
        
        