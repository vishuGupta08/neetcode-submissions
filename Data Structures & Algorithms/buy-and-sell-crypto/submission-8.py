class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = len(prices)-1
        maxProfit = 0
        while l < r:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                if (prices[r] - prices[l+1]) > (prices[r-1] - prices[l]):
                    l += 1
                elif (prices[r-1] - prices[l]) > (prices[r] - prices[l+1]):
                    r -= 1
                else:
                    l +=1
        return maxProfit
        
        