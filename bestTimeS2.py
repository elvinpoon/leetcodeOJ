class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [0]
        for index,price in enumerate(prices):
            if index == 0:
                continue
            s0.append(max(s0[index-1],s2[index-1]))
            s1.append(max(s1[index-1],s0[index-1] -price))
            s2.append(s1[index-1] + price)
        return max(s0[-1],s2[-1])
m = Solution()
print m.maxProfit([1, 2, 3, 0, 2])
