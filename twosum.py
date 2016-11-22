class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        search = {}
        index = 0
        for num in nums:
            if num in search:
                search[num] = [search[num],index]
                index += 1
                continue
            search[num] = index
            index += 1
        for num in search.keys():
            if target - num in search:
                a = search[num]
                b = search[target - num]

                if a == b:
                    return a
                return [min(a,b),max(a,b)]

m = Solution()
res = m.twoSum([-1,-2,-3,-4,-5],-8)
print res