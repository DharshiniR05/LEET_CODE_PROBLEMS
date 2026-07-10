class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        target_sum = k * threshold
        window_sum = sum(arr[:k])
        count = 0

        # Check first window
        if window_sum >= target_sum:
            count += 1

        # Slide the window
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]

            if window_sum >= target_sum:
                count += 1

        return count
        