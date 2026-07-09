class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter

        result = []
        p_count = Counter(p)
        window_count = Counter()

        for i in range(len(s)):
            window_count[s[i]] += 1

            # Remove left character if window size exceeds len(p)
            if i >= len(p):
                if window_count[s[i - len(p)]] == 1:
                    del window_count[s[i - len(p)]]
                else:
                    window_count[s[i - len(p)]] -= 1

            # Compare counts
            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result
        