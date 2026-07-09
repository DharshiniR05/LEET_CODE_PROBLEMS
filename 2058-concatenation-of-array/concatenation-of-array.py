class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for _ in range(2):
            for num in nums:
                ans.append(num)

        return ans
        