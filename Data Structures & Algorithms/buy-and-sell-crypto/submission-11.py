class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = len(prices)-1
        maxProfit = 0
        cheapestBuy = prices[l]
        for price in prices:
            cheapestBuy = min(cheapestBuy, price)

            profit = price - cheapestBuy;

            maxProfit = max(maxProfit, profit)
            
        return maxProfit
        
        