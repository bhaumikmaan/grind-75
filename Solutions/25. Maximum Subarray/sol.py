class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max, total_max = 0, -100001
        for c in nums:
            cur_max = max(c, cur_max + c)
            total_max = max(total_max, cur_max)
        return total_max