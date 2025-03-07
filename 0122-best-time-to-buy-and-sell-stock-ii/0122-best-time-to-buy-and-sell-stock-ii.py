class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        max_profit=0
        for r, price in enumerate(prices):
            if price>prices[l]:
                max_profit+=price-prices[l]
                l=r
            else:
                l=r
        return max_profit