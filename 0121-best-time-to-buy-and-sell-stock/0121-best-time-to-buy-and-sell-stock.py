class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # l=0
        # max_profit=0
        # for r,price in enumerate(prices):
        #     if price< prices[l]:
        #         l=r
        #     max_profit=max(max_profit,price-prices[l])

        # return max_profit

        #dp
        min_stock=prices[0]
        max_profit=0

        for price in prices[1:]:
            min_stock=min(price, min_stock)
            max_profit=max(max_profit,price-min_stock)

        return max_profit