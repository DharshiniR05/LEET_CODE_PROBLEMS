class Solution(object):
    def minSwaps(self, nums):
        ones = sum(nums)

        # If there are 0 or 1 ones, no swaps needed
        if ones <= 1:
            return 0

        # Create circular array
        nums = nums + nums

        # Count zeros in first window
        zeros = nums[:ones].count(0)
        min_swaps = zeros

        # Slide the window
        for i in range(ones, len(nums)):
            if nums[i - ones] == 0:
                zeros -= 1

            if nums[i] == 0:
                zeros += 1

            min_swaps = min(min_swaps, zeros)

        return min_swaps
        