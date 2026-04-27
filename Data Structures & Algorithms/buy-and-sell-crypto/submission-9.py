class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = len(prices)-1
        maxProfit = 0
        cheapestBuy = prices[l]
        for i in range(len(prices)-1):
            cheapestBuy = min(cheapestBuy, prices[i])

            profit = prices[i] - cheapestBuy;

            maxProfit = max(maxProfit, profit)
            
        return maxProfit
        
        