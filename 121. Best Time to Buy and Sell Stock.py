class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        lowest ,res = prices[0], 0
        for price in prices:
            if lowest>price:
                lowest = price
            res = max(price-lowest, res)
        return res
