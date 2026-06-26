class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 6 4

        profit = 0
        n = len(prices)
        i = 0
        while i < len(prices) - 1:
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
            
            i += 1
        
        return profit

        