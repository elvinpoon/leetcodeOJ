class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minbuy = 1e10
        maxprof = 0
        for price in prices:
            profit = price - minbuy
            if price < minbuy:
                minbuy = price
            if profit > maxprof:
                maxprof = profit
        return maxprof

m = Solution()
print m.maxProfit([7, 1, 5, 3, 6, 4])
print m.maxProfit([7, 6, 4, 3, 1])