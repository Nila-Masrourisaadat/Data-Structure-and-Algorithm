class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        max_profit=0
        for r,price in enumerate(prices):
            if price< prices[l]:
                l=r
            else:
                max_profit=max(max_profit,price-prices[l])

        return max_profit